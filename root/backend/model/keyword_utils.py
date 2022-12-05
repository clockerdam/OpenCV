"""
Util functions for dealing with keywords 
"""

from typing import List, Tuple

import random
import os


import re
import spacy
# nlp = spacy.load("en_core_sci_sm")
nlp = spacy.load("en_core_web_sm")
# cache_dir="/model"
# model_path="en_core_web_sm"
# try:
#     nlp = spacy.load(os.path.join(cache_dir,model_path))
# except OSError:
#     spacy.cli.download(model_path)
#     nlp = spacy.load(model_path)
#     nlp.to_disk(os.path.join(cache_dir,model_path))


def title_description_field_to_list_of_text_label_pair(field: List[dict]) -> List[Tuple[str, float]]:
    return [
        (
            f"{experience_point['value']['title']} \n {experience_point['value']['description']}",
            # experience_point['label']
            # Using some fake scores for now
            random.uniform(0, 1)
        ) for experience_point in field
    ]


def list_of_text_label_pairs_from_key_val_list(key_val_list: List[dict]) -> List[Tuple[str, float]]:
    return [tuple(v.values()) for v in key_val_list]


def list_of_text_label_pair_from_skill_based_list(l: List[dict]) -> List[Tuple[str, float]]:
    return [(row['value']['name'], row['label']) for row in l]


def get_section_texts_with_score_from_resume(resume: dict) -> Tuple[str, float]:
    res = []
    # Extract experiences
    res += title_description_field_to_list_of_text_label_pair(
        resume['experience']['value'])

    # Extract education
    res += title_description_field_to_list_of_text_label_pair(
        resume['education']['value'])
    # summary
    res += [(resume['summary']['value'], resume['summary']['label'])]

    # interests
    res += list_of_text_label_pairs_from_key_val_list(
        resume['interests']['value'])

    # Accomplishements
    res += title_description_field_to_list_of_text_label_pair(
        resume['accomplishments']['value'])

    # projects
    res += title_description_field_to_list_of_text_label_pair(
        resume['projects']['value'])

    # languages
    res += list_of_text_label_pair_from_skill_based_list(
        resume['languages']['value'])

    # softSkills
    res += list_of_text_label_pair_from_skill_based_list(
        resume['softSkills']['value'])

    # hard skills
    res += list_of_text_label_pair_from_skill_based_list(
        resume['hardSkills']['value'])

    # certifications
    res += title_description_field_to_list_of_text_label_pair(
        resume['certifications']['value'])

    # patents
    res += list_of_text_label_pairs_from_key_val_list(
        resume['patents']['value'])

    # extracurriculars
    res += title_description_field_to_list_of_text_label_pair(
        resume['extracurriculars']['value'])
    return res


def extract_keywords_from_text(texts: List[str]) -> List[Tuple[str, float]]:
    """Takes in text and outputs the most relevant keywords with an attached score

    """
    res = []
    for t in texts:
        kws = extract_entities_from_text(t)
        for kw in kws:
            res.append((kw, 1.0))
    return res


#################### extract requirements from JD (suited for JD_SE2) ###########


def extract_requirements_JD(jd: str) -> list:
    """Takes in JD in text format and finds requirements, experience and qualifications
    and returns a list with keywords from these 3 fields"""
    splitted_jd = split_jd(jd)
    pot_req_found = find_req(splitted_jd)
    req = extract_entities(pot_req_found)
    req = list(filter(lambda x: x != "", [v.strip() for sublist in [x.split(",") for x in req]
                                          for v in sublist]))
    return req


def split_jd(jd: str) -> list:
    regex_split_jd = r"(?s).+?(?=^$)"
    matches = re.finditer(regex_split_jd, jd, re.MULTILINE)
    jd_list = []
    for match in matches:
        jd_list.append(match.group())
    return jd_list


def find_req(jd_list: list) -> list:
    regex_find_req = "((\s.*[Ee]xperience.*:)|(\s.*[Qq]ualification.*:)|(\s.*[Rr]equire.*:))"
    req = []
    for (i, line) in enumerate(jd_list):
        match = re.match(regex_find_req, line)
        if match != None:
            pot_req = jd_list[i+1].split('•')
            for r in range(len(pot_req)):
                pot_req[r] = pot_req[r].strip()
            pot_req.remove('')
            req = req+pot_req
    return req


def extract_entities(req: list) -> list:
    return extract_entities_from_text("\n".join(req))


def extract_entities_from_text(text: str) -> List[str]:
    """Extracts all entities from the text"""

    entity_list = []
    entities_to_remove_list = []

    doc = nlp(text)
    for chunk in doc.noun_chunks:
        entities_to_remove_list.append(chunk.text.lower())
    for token in doc:
        if token.pos_ == "VERB":
            entities_to_remove_list.append(token.lemma_.lower())
    for entity in doc.ents:
        entity_list.append(entity.text.lower())

    entity_list = list(dict.fromkeys(entity_list))  # remove duplicates
    entity_list_copy = entity_list.copy()
    for ent in entity_list:
        regex = '.* {ent}.*'.format(ent=ent)
        for ne in entities_to_remove_list:
            match = re.match(regex, ne)
            if match != None:
                entity_list_copy.remove(ent)
                break
    entity_list = entity_list_copy
    return entity_list
