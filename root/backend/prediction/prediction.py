from model.resume_scorer import ResumeScorer, shorten_resume
from model.Job import Job
from persistence.cloud_storage.cloud_storage import read_job_keywords
from util.json_to_df import create_df, get_resume_dict_from_dataframe
from model.keyword_utils import extract_requirements_JD


def improve_cv(payload: dict) -> dict:
    # Get the job title and description
    job_title = payload.get("title", "")
    job_description = payload.get("description", "")
    print(f"Starting prediciton for {job_title}")

    # Extract keywords / requirements from the description
    description_keywords = extract_requirements_JD(job_description)

    # retrieve our pretrained / heuristic keyword dictionary for the job title
    print("Extracting keywords")
    job_keywords_csv = read_job_keywords(job_title)
    job = Job(job_title)
    job.load_from_csv_data(job_keywords_csv)

    orig_keywords = set(job.keywords.keys())
    jd_keyword_set = set(description_keywords)
    kw = list(orig_keywords.intersection(jd_keyword_set))

    # Update the keywords for the job based on the description
    job.update_keywords_from_description(description_keywords)

    scorer: ResumeScorer = ResumeScorer(job)

    resume = payload
    resume_df, md = create_df(resume)

    print("Scoring resume")
    scored = scorer.score_resume_as_dataframe(resume_df)

    print("Cutting resume")
    cut, stats = shorten_resume(scored, kw)

    # Filter out unwanted fields

    cut = cut[resume_df.columns]
    cut = cut.drop("keywords", axis=1)

    finished_resume = get_resume_dict_from_dataframe(cut, md)

    return {
        **finished_resume,
        "stats": {
            **stats
        }
    }
