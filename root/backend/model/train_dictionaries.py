from typing import List
from model.Job import Job
from model import keyword_utils
import pandas as pd

# Modify this in order to change which positions we train for
job_titles = [
    "Data scientist"
]


   
def flatten(l: List) -> List: 
    return [item for sublist in l for item in sublist] # flattening the resulting listprint(resume_text_base)
    
    
def train_keywords_for_job_title(job_title: str, dataset: List[dict]) -> Job: 
    """Trains the keyword scores for a job title given the dataset
    The dataset should be a list of labeled resumes, where the title of the labeling was the job title"""
    job: Job = Job(job_title)
    resume_text_base = [keyword_utils.get_section_texts_with_score_from_resume(resume) for resume in dataset]
    resume_text_base = flatten(resume_text_base)
    keywords = keyword_utils.extract_keywords_from_text([v[0] for v in resume_text_base])

    flat_keywords = []
    for i, row in enumerate(keywords): 
        for kw in row:
            flat_keywords.append(kw + (resume_text_base[i][1],))
    frame = pd.DataFrame(flat_keywords, columns=["word", "score", "paragraph_score"])

    frame['weighted_score'] = frame.score * frame.paragraph_score

    frame = frame.groupby('word', as_index=True).mean().sort_values(by=['weighted_score'], ascending=False)
    most_important = frame[frame.weighted_score > 0.2]

    m = most_important.weighted_score
    
    job.set_keywords(m.to_dict())

    
    return job

    
    