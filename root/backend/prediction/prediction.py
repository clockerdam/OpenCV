from model.resume_scorer import ResumeScorer
from model.Job import Job
from persistence.cloud_storage.cloud_storage import read_job_keywords
from util.json_to_df import create_df, get_resume_dict_from_dataframe


def improve_cv(payload: dict) -> dict:
    job_title = payload["title"]
    resume = payload
    job_keywords_csv = read_job_keywords(job_title)
    job = Job(job_title)
    job.load_from_csv_data(job_keywords_csv)

    scorer: ResumeScorer = ResumeScorer(job)

    resume_df, md = create_df(resume)

    scored = scorer.score_resume_as_dataframe(resume_df)

    cut = scorer.shorten_resume(scored)

    finished_resume = get_resume_dict_from_dataframe(cut, md)

    return finished_resume
