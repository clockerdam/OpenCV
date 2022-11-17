from model.keyword_utils import extract_keywords_from_text
from model.Job import Job
from gensim.test.utils import datapath
from gensim.models.fasttext import load_facebook_model
import numpy as np
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
    
    def shorten_resume(self, resume: pd.DataFrame) -> pd.DataFrame: 
        return resume.sort_values('label')[:-10]
        