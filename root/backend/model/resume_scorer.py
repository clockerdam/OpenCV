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
                relevance = list(self.job.keywords.values())[
                    closest] * kw[1] * cos_sim
                scores.append(relevance)

        # take the mean of the scores to make sure all keywords can contribute
        # and that we don't favor longer texts (which would have more keywords)
        return float(np.mean(scores))

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
        df.loc[df['type'].isin(value_proficiency_fields), [
            'scoring_text']] = df['name']
        df.loc[df['type'].isin([
            'summary',
            'patents',
            'interests'
        ]), ['scoring_text']] = df['value']

        df.loc[df['type'].isin([
            'contactInfo'
        ]), ['scoring_text']] = ''
        df.loc[df['type'] == 'contactInfo', ['scoring_text']] = df['name']

        df['multiplier'] = (df['proficiency'] / 5.0).fillna(1.0)
        df.loc[df['type'] == 'languages', ['multiplier']] *= 0.4
        return df

    def score_resume_as_dataframe(self, resume: pd.DataFrame) -> pd.DataFrame:
        """Takes a resume with labels (can be set to zero) and returns the same resume
        with labels updated according to our model"""

        res = resume.copy()
        # Generate the text based on each column type
        res = self.get_evaluation_text_for_df_row(resume)

        # Each row gets a score based on its generated text
        res['keywords'] = res.apply(
            lambda x: extract_keywords_from_text([x['scoring_text']]), axis=1)
        res['score'] = res.apply(lambda x: self.score_text_based_on_keywords(
            x['keywords']) * x['multiplier'], axis=1)
        res.loc[res['type'] == 'contactInfo', ['score']] = 1

        res['label'] = res['score']
        res.drop('score', axis=1, inplace=True)

        return res


def point_duration_heuristic_bost(duration: float) -> float:
    """Takes a duration for experience
    and returns a heuristic addition to the score"""
    if duration == 0:
        return 0.01
    if duration <= 12:
        return 0.014
    elif duration <= 24:
        return 0.019
    elif duration <= 60:
        return 0.030
    else:
        return 0.035

def time_since_heuristic_boost(time_since: float) -> float:
    """Takes a time_since for education and 
    returns a heurstic addition to the score"""
    if time_since == 0:
        return 1
    return 1/(time_since**2)

def education_level(title: str) -> float:
    """Gives a boost to higher level education"""
    if 'Ph.D' in title:
        return 0.5
    if 'MBA' in title:
        return 0.1
    return 0

    
    
    
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
    kw = set(row['raw_keywords'])
    cov = kw.intersection(requiremnets)
    return list(cov)


def _add_heuristics_to_src_dataframe(src: pd.DataFrame) -> pd.DataFrame:
    # Do any heuristics on the scores
    # We set these to inf to make sure that we will always include them in the output
    src[['education_heuristic', 'experience_heuristic', 'contact_heuristic']] = 0
    src.loc[src["type"].isin(['education']),
            #"education_heuristic"] = src.apply(lambda x: point_duration_heuristic_bost(x['duration']), axis=1)
            "education_heuristic"] = src.apply(lambda x: time_since_heuristic_boost(x['time_since']) + education_level(x["title"]) if x["type"] == "education" else 0, axis=1)
    src.loc[src["type"].isin(['experience']),
            "experience_heuristic"] = src.apply(lambda x: point_duration_heuristic_bost(x['duration'] if x["type"] == "experience" else 0), axis=1)

    # Make sure that we always add the contact information
    src.loc[src['type'] == 'contactInfo', ['contact_heuristic']] = math.inf

    # Give large penalty to interests
    src['interest_heuristic'] = src.apply(
        lambda x: -0.5 if x['type'] == 'interests' else 0, axis=1)

    # Make sure to remove any row that does not have content
    src = src.loc[src['scoring_text'] != ""]

    return src


def space_required_for_adding(row: pd.DataFrame, included: dict) -> int:
    space_required = len(row.iloc[0]['scoring_text']) // 140
    type = row.iloc[0]['type']

    section_added = included[type]

    if type in ['experience', 'education', 'certifications', 'accomplishments', 'projects', 'extracurriculars', 'patents']:
        if not section_added:
            space_required += 4
        else:
            space_required += 1
    elif type in ['summary']:
        space_required += 1
    elif type in ['hardSkills', 'softSkills', 'languages']:
        if not section_added:
            space_required += 3
        else:
            space_required = 0
    elif type in ['contactInfo']:
        space_required = 0

    return space_required


def shorten_resume(resume: pd.DataFrame, job_description_keywords: List[str]) -> Tuple[pd.DataFrame, dict]:
    """Takes a fully scored resume and returnes a one-pager
    based on those scores and other heuristics

    Returns a tuple consisting of (one-pager, statistics)
    the resume is a dtaframe, the stats is a dictionary
    """

    included = dict.fromkeys(set(resume['type']), False)

    total_space = 40
    space_used = 0

    # Storing how much we have used for each type

    # Copy the input as to not ruin it
    src: pd.DataFrame = resume.copy()
    output: pd.DataFrame = src.copy().iloc[:0]

    requirements = set(job_description_keywords)
    covered = set()

    # Extracting some keyword information
    src['raw_keywords'] = src['keywords'].map(lambda x: [v[0] for v in x])
    all_keywords_in_resume = set(src['raw_keywords'].sum())

    src = _add_heuristics_to_src_dataframe(src)

    # Iteratively build up our resume
    can_add_more = len(src) != 0
    while can_add_more:
        # Update heuristics of included keywords
        src['covered_keywords'] = src.apply(
            lambda x: add_covered_keywords_for_requirements_to_resume_df(
                x, requirements.difference(covered)),
            axis=1
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
        item_len = space_required_for_adding(best_item, included)

        space_for_item = total_space - space_used

        # Check if we have room for the highest scored item
        if space_for_item >= item_len:
            # We have space
            output = pd.concat([output, best_item])

            # update included map
            included[best_item.iloc[0]['type']] = True
            space_used += item_len

            # Update scores based on heuristics
            # limit number of education points
            len_edu = len(output[output['type'] == 'education'])
            if len_edu >= 2:
                src.loc[src['type'] == 'education',
                        'education_heuristic'] = -0.1

            # limit number of experience points
            len_exp = len(output[output['type'] == 'experience'])
            if len_exp >= 2:
                src.loc[src['type'] == 'experience',
                        'experience_heuristic'] = 0

            # Update covered topics
            kw = set(best_item['raw_keywords'].iloc[0])
            relevant = kw.intersection(requirements)
            covered.update(relevant)

        # Remove the point no matter if it was included or not
        # this enables us to fill up the cv even though we can't
        # fit one good point
        src = src.iloc[1:]
        can_add_more = len(src) != 0

    output = output.sort_values(
        ['type', 'time_since', 'score'], ascending=[True, True, False])

    stats = {
        "included_keywords": list(covered),
        "removed_keywords": list(all_keywords_in_resume.difference(covered)),
        "missing_keywords": list(requirements.difference(all_keywords_in_resume)),
        "all_original_keywords": list(all_keywords_in_resume),
    }

    return output, stats
