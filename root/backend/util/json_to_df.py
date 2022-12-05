import numpy as np
import pandas as pd
from pandas import json_normalize
from typing import Tuple, Dict
from datetime import datetime


def get_resume_dict_from_dataframe(resume: pd.DataFrame, metadata: dict = {}) -> dict:
    """ REturns the json / dict representation of a dataframe-resume"""

    df = resume
    if (set(['scoring_text', 'multiplier']).issubset(df.columns)):
        df = df.drop(['scoring_text', 'multiplier'], axis=1)

    output = {**metadata}

    # contact_info
    contact = df[df['type'] == 'contactInfo']
    contact.drop(['type', 'label'], axis=1, inplace=True)
    contact = contact[contact.columns[~contact.isnull().all()]]
    contact_dict = contact.to_dict('records')
    if len(contact_dict) == 1:
        output['contactInfo'] = contact_dict[0]

    summary = df[df['type'] == 'summary']
    summary.drop(['type'], axis=1, inplace=True)
    summary = summary[summary.columns[~summary.isnull().all()]]
    summary_dict = summary.to_dict('records')
    if len(summary_dict) == 1:
        output['summary'] = summary_dict[0]

    # experience
    output['experience'] = convert_list_field_to_json('experience', df)

    # education
    output['education'] = convert_list_field_to_json('education', df)

    # interest
    output['interests'] = convert_list_field_to_json(
        'interests', df)
    # accomplishment
    output['accomplishments'] = convert_list_field_to_json(
        'accomplishments', df)
    # language
    output['languages'] = convert_list_field_to_json('languages', df)
    # project
    output['projects'] = convert_list_field_to_json('projects', df)
    # soft_skill
    output['softSkills'] = convert_list_field_to_json('softSkills', df)
    # hard_skill
    output['hardSkills'] = convert_list_field_to_json('hardSkills', df)
    # certification
    output['certifications'] = convert_list_field_to_json('certifications', df)
    # patent
    output['patents'] = convert_list_field_to_json('patents', df)
    # extracurricular
    output['extracurriculars'] = convert_list_field_to_json(
        'extracurriculars', df)

    return output


def convert_list_field_to_json(list_field_name: str, df: pd.DataFrame) -> dict:
    field = df[df['type'] == list_field_name]
    field = field.drop(['type'], axis=1)
    field = field[field.columns[~field.isnull().all()]]

    field_rows = field.to_dict('records')

    val = []
    if list_field_name in ['interests', 'patents']:
        # Special handling for direct values
        val = field_rows

    else:
        for rec in field_rows:
            label = rec['label']
            del rec['label']
            val.append({"value": rec, "label": label})

    output = {
        "value": val,
        "label": 0,
    }

    return output


def create_df(resume: Dict) -> Tuple[pd.DataFrame, dict]:
    """Creates a pandas DataFrame from the json representation of the resume
    Returns a tuple (dataframe, metadata), where the metadata contains the _id and title 
    that does not fit well into the dataframe, and that might be useful 
    for reconstructing it later
    """
    summary_df = get_summary_df(resume)
    contact_info_df = get_contact_info_df(resume)
    experience_df = get_experience_df(resume)
    education_df = get_education_df(resume)
    interest_df = get_interests_df(resume)
    accomplishment_df = get_accomplishments_df(resume)
    language_df = get_languages_df(resume)
    project_df = get_projects_df(resume)
    soft_skill_df = get_soft_skills_df(resume)
    hard_skill_df = get_hard_skills_df(resume)
    certification_df = get_certifications_df(resume)
    patent_df = get_patents_df(resume)
    extracurricular_df = get_extracurricular_df(resume)
    total_df = pd.concat([summary_df, contact_info_df, experience_df, education_df, interest_df, accomplishment_df, language_df,
                         project_df, soft_skill_df, hard_skill_df, certification_df, patent_df, extracurricular_df], ignore_index=True)
    total_df['label'] = total_df['label'].fillna(0)

    metadata = {
        "title": resume['title'],
        "_id": resume['_id'],
    }
    return total_df, metadata

# help functions


def get_summary_df(resume: Dict) -> pd.DataFrame:
    summary = resume['summary']
    df = json_normalize(summary)
    df['type'] = 'summary'
    return df


def get_contact_info_df(resume: Dict) -> pd.DataFrame:
    contact_info = resume['contactInfo']
    contact_info_df = json_normalize(contact_info)
    contact_info_df['type'] = 'contactInfo'
    return contact_info_df


def get_experience_df(resume: Dict) -> pd.DataFrame:
    experience = resume['experience']['value']
    experience_df = pd.DataFrame()
    for exp in experience:
        df = json_normalize(exp['value'])
        df['label'] = exp['label']
        df['type'] = 'experience'
        df['duration'] = time_of_experience(df)
        df['time_since'] = time_since_experience(df)
        experience_df = pd.concat([experience_df, df], ignore_index=True)
    return experience_df


def get_education_df(resume: Dict) -> pd.DataFrame:
    education = resume['education']['value']
    education_df = pd.DataFrame()
    for edu in education:
        df = json_normalize(edu['value'])
        df['label'] = edu['label']
        df['type'] = 'education'
        df['duration'] = time_of_education(df)
        df['time_since'] = time_since_education(df)
        education_df = pd.concat([education_df, df], ignore_index=True)
    return education_df


def get_interests_df(resume: Dict) -> pd.DataFrame:
    interest = resume['interests']['value']
    interest_df = pd.DataFrame()
    for i in interest:
        df = json_normalize(i)
        df['label'] = i['label']
        df['type'] = 'interests'
        interest_df = pd.concat([interest_df, df], ignore_index=True)
    return interest_df


def get_accomplishments_df(resume: Dict) -> pd.DataFrame:
    accomplishment = resume['accomplishments']['value']
    accomplishment_df = pd.DataFrame()
    for acc in accomplishment:
        df = json_normalize(acc['value'])
        df['label'] = acc['label']
        df['type'] = 'accomplishments'
        accomplishment_df = pd.concat(
            [accomplishment_df, df], ignore_index=True)
    return accomplishment_df


def get_languages_df(resume: Dict) -> pd.DataFrame:
    language = resume['languages']['value']
    language_df = pd.DataFrame()
    for lan in language:
        df = json_normalize(lan['value'])
        df['label'] = lan['label']
        df['type'] = 'languages'
        language_df = pd.concat([language_df, df], ignore_index=True)
    return language_df


def get_projects_df(resume: Dict) -> pd.DataFrame:
    project = resume['projects']['value']
    project_df = pd.DataFrame()
    for pro in project:
        df = json_normalize(pro['value'])
        df['label'] = pro['label']
        df['type'] = 'projects'
        project_df = pd.concat([project_df, df], ignore_index=True)
    return project_df


def get_soft_skills_df(resume: Dict) -> pd.DataFrame:
    soft_skill = resume['softSkills']['value']
    soft_skill_df = pd.DataFrame()
    for ss in soft_skill:
        df = json_normalize(ss['value'])
        df['label'] = ss['label']
        df['type'] = 'softSkills'
        soft_skill_df = pd.concat([soft_skill_df, df], ignore_index=True)
    return soft_skill_df


def get_hard_skills_df(resume: Dict) -> pd.DataFrame:
    hard_skill = resume['hardSkills']['value']
    hard_skill_df = pd.DataFrame()
    for hs in hard_skill:
        df = json_normalize(hs['value'])
        df['label'] = hs['label']
        df['type'] = 'hardSkills'
        hard_skill_df = pd.concat([hard_skill_df, df], ignore_index=True)
    return hard_skill_df


def get_certifications_df(resume: Dict) -> pd.DataFrame:
    certification = resume['certifications']['value']
    certification_df = pd.DataFrame()
    for cert in certification:
        df = json_normalize(cert['value'])
        df['label'] = cert['label']
        df['type'] = 'certifications'
        certification_df = pd.concat([certification_df, df], ignore_index=True)
    return certification_df


def get_patents_df(resume: Dict) -> pd.DataFrame:
    patent = resume['patents']['value']
    patent_df = pd.DataFrame()
    for p in patent:
        df = json_normalize(p)
        df['label'] = p['label']
        df['type'] = 'patents'
        patent_df = pd.concat([patent_df, df], ignore_index=True)
    return patent_df


def get_extracurricular_df(resume: Dict) -> pd.DataFrame:
    extracurricular = resume['extracurriculars']['value']
    extracurricular_df = pd.DataFrame()
    for extra in extracurricular:
        df = json_normalize(extra['value'])
        df['label'] = extra['label']
        df['type'] = 'extracurriculars'
        extracurricular_df = pd.concat(
            [extracurricular_df, df], ignore_index=True)
    return extracurricular_df



def time_of_experience(experience: pd.DataFrame) -> int:
    try:
        fromDate = experience.iloc[0]['fromDate']
        toDate = experience.iloc[0]['toDate']
        present_list = ['today', 'present']
        if toDate.lower() in present_list:
            datetime_object_to = datetime.today()
        else:
            datetime_object_to = datetime.strptime(toDate, '%B %Y')

        datetime_object_from = datetime.strptime(fromDate, '%B %Y')    

        diff = datetime_object_to - datetime_object_from
        seconds_per_month = 86400*30
        months = int(np.floor(diff.total_seconds()/seconds_per_month))
        if months == 0: #one month
            months = 1
        return months
    except: #set it to a year if something is wrong
        months = 12
        return months
    
def time_of_education(education: pd.DataFrame) -> int:
    try:
        fromDate = education.iloc[0]['fromDate']
        toDate = education.iloc[0]['toDate']
        present_list = ['today', 'present']
        if toDate.lower() in present_list:
            datetime_object_to = datetime.today()
        else:
            datetime_object_to = datetime.strptime(toDate, '%Y')

        datetime_object_from = datetime.strptime(fromDate, '%Y')    

        diff = datetime_object_to - datetime_object_from
        seconds_per_month = 86400*30
        months = int(np.floor(diff.total_seconds()/seconds_per_month))
        if months == 0: #one month
            months = 1
        return int(months)
    except: #set it to a year if something is wrong
        months = 12
        return int(months)
    

    
def time_since_experience(experience: pd.DataFrame) -> int:
    try:
        toDate = experience.iloc[0]['toDate']
        present_list = ['today', 'present']
        if toDate.lower() in present_list:
            datetime_object_to = datetime.today()
        else:
            datetime_object_to = datetime.strptime(toDate, '%B %Y')
        diff = datetime.today() - datetime_object_to
        seconds_per_month = 86400*30
        months = int(np.floor(diff.total_seconds()/seconds_per_month))
        return int(months)
    except:
        months = 12
        return int(months)

def time_since_education(experience: pd.DataFrame) -> int:
    try:
        toDate = experience.iloc[0]['toDate']
        present_list = ['today', 'present']
        if toDate.lower() in present_list:
            datetime_object_to = datetime.today()
        else:
            datetime_object_to = datetime.strptime(toDate, '%Y')
        diff = datetime.today() - datetime_object_to
        seconds_per_month = 86400*30
        months = int(np.floor(diff.total_seconds()/seconds_per_month))
        return int(months)
    except:
        months = 12
        return int(months)
    
    
    