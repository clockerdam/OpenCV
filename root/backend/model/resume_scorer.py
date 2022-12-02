from typing import List, Tuple
from model.keyword_utils import extract_keywords_from_text
from model.Job import Job
import numpy as np
import math
import pandas as pd
import re

from model.embedding import embedding_for_keyword_list, closest_keyword_index


class ResumeScorer():
    def __init__(self, job: Job):
        self.job = job

        self.job_kw_embeddings = embedding_for_keyword_list(self.job.keywords) 

    def score_text_based_on_keywords(self, keywords: List[Tuple[str, float]]) -> float:
        """Scores a piece of text based on the relevance to the job"""

        if len(keywords) == 0:
            return 0.0

        scores = []
        for kw in keywords:
            if kw[0] in self.job.keywords:
                scores.append(kw[1] * self.job.keywords[kw[0]])
            else:
                closest, cos_sim = closest_keyword_index(
                    kw[0], self.job_kw_embeddings)
                if kw[0] == "english":
                    print("Closest keyword to '{}' is '{}' with cosine similarity {}\n".format(
                        kw[0], list(self.job.keywords.keys())[closest], cos_sim))
                relevance = list(self.job.keywords.values())[
                    closest] * kw[1] * cos_sim
                scores.append(relevance)

        # take the mean of the scores to make sure all keywords can contribute
        # and that we don't favor longer texts (which would have more keywords)
        return np.mean(scores)

    def get_evaluation_text_for_df_row(self, df: pd.DataFrame) -> pd.DataFrame:
        """Generates the text we will use for evaluation for each row type"""
        df.loc[df['type'].isin([
            'experience',
            'education',
            'certifications',
            'accomplishments',
            'projects',
            'extracurriculars',
            'patents',
            ]), ['scoring_text']] = df['title'] + " " + df['description']

        value_proficiency_fields = [
            'softSkills',
            'hardSkills',
            'languages',
            ]
        df.loc[df['type'].isin(value_proficiency_fields), ['scoring_text']] = df['name']
        df.loc[df['type'].isin([
            'summary',
            'patents',
            'interests'
            ]), ['scoring_text']] =  df['value']

        df.loc[df['type'].isin([
            'contactInfo'
        ]), ['scoring_text']]= ''

        df['multiplier']= (df['proficiency'] / 5.0).fillna(1.0)
        df.loc[df['type'] == 'languages', ['multiplier']] *= 0.4
        return df

    def score_resume_as_dataframe(self, resume: pd.DataFrame) -> pd.DataFrame:
        """Takes a resume with labels (can be set to zero) and returns the same resume
        with labels updated according to our model"""

        # Generate the text based on each column type
        resume= self.get_evaluation_text_for_df_row(resume)


        # Each row gets a score based on its generated text
        resume['keywords']= resume.apply(lambda x: extract_keywords_from_text([x['scoring_text']]), axis=1)
        resume['score']=resume.apply(lambda x: self.score_text_based_on_keywords(
            x['keywords']) * x['multiplier'], axis=1)
        resume.loc[resume['type'] == 'contactInfo', ['score']]=1

        resume['label']=resume['score']
        resume.drop('score', axis=1, inplace=True)

        return resume

def _quota_key_for_type(type: str) -> str:
    if type in ["education", "experience", "extracurricular"]:
        return "body"
    elif type in ["summary"]:
        return "summary"
    elif type in ["hardSkills", "softSkills", "languages"]:
        return "skill"
    else:
        return "body"

def add_covered_keywords_for_requirements_to_resume_df(row: pd.DataFrame, requiremnets: List[str]):
    kw=set(row['raw_keywords'])
    cov=kw.intersection(requiremnets)
    return list(cov)


def shorten_resume(resume: pd.DataFrame, job_description_keywords: List[str]) -> Tuple[pd.DataFrame, dict]:
    """Takes a fully scored resume and returnes a one-pager
    based on those scores and other heuristics

    Returns a tuple consisting of (one-pager, statistics)
    the resume is a dtaframe, the stats is a dictionary
    """

    # Representing the content limits on each type of section
    quotas={
        "body": 258 * 7,
        "skill": 3 * 70,
        "summary": 120,
    }

    # Storing how much we have used for each type
    used = dict.fromkeys(quotas, 0)

    # Copy the input as to not ruin it
    src: pd.DataFrame = resume.copy()
    output: pd.DataFrame = src.copy().iloc[:0]

    requirements = set(job_description_keywords)
    covered = set()

    # Extracting some keyword information
    src['raw_keywords'] = src['keywords'].map(lambda x: [v[0] for v in x])
    all_keywords_in_resume = set(src['raw_keywords'].sum())

    # Do any heuristics on the scores
    # We set these to inf to make sure that we will always include them in the output
    src[['education_heuristic', 'experience_heuristic']] = 0
    src.loc[src["type"].isin(['education', 'contactInfo']),
                             "education_heuristic"] = math.inf
    src.loc[src["type"].isin(['experience', 'contactInfo']),
                             "experience_heuristic"] = math.inf



    # Give large penalty to interests
    src['interest_heuristic'] = src.apply(
        lambda x: -0.5 if x['type'] == 'interests' else 0, axis=1)

    # Make sure to remove any row that does not have content
    src = src.loc[src['scoring_text'] != ""]


    # Iteratively build up our resume
    can_add_more = len(src) != 0
    while can_add_more:
        # Update heuristics of included keywords
        src['covered_keywords'] = src.apply(
            lambda x: add_covered_keywords_for_requirements_to_resume_df(
                x, requirements.difference(covered)),
            axis = 1
        )
        src['keyword_cover_heuristic'] = src['covered_keywords'].map(
            lambda x: len(x) * 0.5)

        # Update scores based on our heuristics
        src['score'] = (
            # Adding up all heuristic scores
            src.loc[:, [
                True if re.search('heuristic', column) else False for column in src.columns
            ]].sum(axis=1) +

            # also using the score from our model
            src['label']
        )

        # Sort the src on the current scores
        src = src.sort_values('score', ascending=False)
        
        # Find the currently best rated 
        best_item = src.iloc[[0]]
        item_len = len(best_item.iloc[0]['scoring_text'])
        
        quota_key = _quota_key_for_type(best_item.iloc[0]['type'])
        space_for_item = quotas[quota_key] - used[quota_key]

        # Check if we have room for the highest scored item
        if space_for_item >= item_len:
            # We have space
            output = pd.concat([output, best_item])
            used[quota_key] += item_len
            
            # Update scores based on heuristics
            # limit number of education points
            len_edu = len(output[output['type'] == 'education'])
            if len_edu >= 3: 
                src.loc[src['type'] == 'education', 'education_heuristic'] = 0

            # limit number of experience points
            len_exp = len(output[output['type'] == 'experience'])
            if len_exp >= 3: 
                src.loc[src['type'] == 'experience', 'experience_heuristic'] = 0
                
            # Update covered topics
            kw = set(best_item['raw_keywords'].iloc[0])
            relevant = kw.intersection(requirements)
            covered.update(relevant)
        
        # Remove the point no matter if it was included or not
        # this enables us to fill up the cv even though we can't 
        # fit one good point
        src = src.iloc[1:]
        can_add_more = len(src) != 0

    output = output.sort_values(['score', 'type', 'time_since'], ascending=[False, True, True])
    
    print(f"Space used: {used}")
    print(f"Total space: {quotas}")
    
    stats = {
        "included_keywords": list(covered),
        "removed_keywords": list(all_keywords_in_resume.difference(covered)),
        "missing_keywords": list(requirements.difference(all_keywords_in_resume)),
    }
    
    return output, stats
    