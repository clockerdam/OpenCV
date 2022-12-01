from model.keyword_utils import extract_keywords_from_text
from model.Job import Job
from gensim.test.utils import datapath
from gensim.models.fasttext import load_facebook_model
import numpy as np
import math
import pandas as pd


class ResumeScorer():
    def __init__(self, job: Job):
        self.cap_path = datapath("crime-and-punishment.bin")
        self.fb_model = load_facebook_model(self.cap_path)
        self.job = job
        
        self.job_kw_embeddings = np.asarray([self.fb_model.wv[kw] for kw in self.job.keywords])

    def closest_keyword_index(self, sample: str) -> str: 
        """Takes the keyword list as embeddings form a job, and a sample. Finds the closest keyword
        
        Implements a KNN algorithm for finding the closest one"""
        sample_embedding = self.fb_model.wv[sample]
        dist_2 = np.sum((self.job_kw_embeddings - sample_embedding) ** 2)
        return np.argmin(dist_2)
     
    def score_text(self, text: str) -> float: 
        """Scores a piece of text based on the relevance to the job"""
        keywords = extract_keywords_from_text([text])
        
        if len(keywords) == 0:
            return 0.0
        
        scores = []
        for kw in keywords:
            if kw[0] in self.job.keywords: 
                scores.append(kw[1] * self.job.keywords[kw[0]])
            else: 
                closest = self.closest_keyword_index(kw[0])
                relevance = list(self.job.keywords.values())[closest] * kw[1]
                scores.append(relevance)
        
        # take the mean of the scores to make sure all keywords can contribute
        # and that we don't favor longer texts (which would have more keywords)
        return np.mean(scores)

    def get_evaluation_text_for_df_row(self, df: pd.DataFrame) -> pd.DataFrame: 
        """Generates the text we will use for evaluation for each row type"""
        df.loc[ df['type'].isin([
            'experience', 
            'education', 
            'certifications',
            'accomplishments',
            'projects',
            'extracurriculars',
            'patents',
            ]), ['scoring_text']] =  df['title']  + " " + df['description']

        value_proficiency_fields = [
            'softSkills',
            'hardSkills',
            'languages',
            ]
        df.loc[ df['type'].isin( value_proficiency_fields ), ['scoring_text']] = df['name']
        df.loc[ df['type'].isin ( [
            'summary',
            'patents',
            'interests'
            ] ), ['scoring_text']] =  df['value']
        
        df.loc[df['type'].isin([
            'contactInfo'
        ]), ['scoring_text']] = ''
        
        df['multiplier'] = (df['proficiency'] / 5.0).fillna(1.0)
        return df
        
    def score_resume_as_dataframe(self, resume: pd.DataFrame) -> pd.DataFrame:
        """Takes a resume with labels (can be set to zero) and returns the same resume
        with labels updated according to our model"""
        
        # Generate the text based on each column type
        resume = self.get_evaluation_text_for_df_row(resume)
        
        # Each row gets a score based on its generated text
        resume['score'] = resume.apply(lambda x: self.score_text(x['scoring_text']) * x['multiplier'], axis=1)
        resume.loc[resume['type'] == 'contactInfo', ['score']] = 1
        
        resume['label'] = resume['score']
        resume.drop('score', axis=1, inplace=True)

        return resume
    
def shorten_resume(resume: pd.DataFrame) -> pd.DataFrame: 
    """Takes a fully scored resume and returnes a one-pager 
    based on those scores and other heuristics"""

    max_len = 1500
    current_content_len = 0
    # COpy the input as to not ruin it 
    src: pd.DataFrame = resume.copy()
    output: pd.DataFrame = src.copy().iloc[:0]

    # Do any heuristics on the scores
    src["heuristic_addition"] = 0
    src.loc[src["type"].isin(['education', 'contactInfo']), "heuristic_addition"] = math.inf
    
    # Iteratively build up our resume
    content_added = True
    while content_added:
        content_added = False
        # Sort the src on the current scores
        
        if len(src) == 0:
            break
        src['score'] = src['heuristic_addition'] + src['label']
        src = src.sort_values('score', ascending=False)
        
        # Find the currently best rated 
        best_item = src.iloc[[0]]
        item_len = len(best_item.iloc[0]['scoring_text'])

        # Check if we have room for the highest scored item
        if  item_len + current_content_len <= max_len: 
            # We have space
            output = pd.concat([output, best_item])
            src = src.iloc[1:]
            current_content_len += item_len
            
            content_added = True
            
            # Update scores based on heuristics
            # limit number of education points
            len_edu = len(output[output['type'] == 'education'])
            if len_edu >= 3: 
                src.loc[src['type'] == 'education', 'heuristic_addition'] = -10

    output = output.sort_values(['score', 'type', 'time_since'], ascending=[False, True, True])
    return output
    