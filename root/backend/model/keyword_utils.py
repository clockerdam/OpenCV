"""
Util functions for dealing with keywords 
"""

from typing import List, Tuple
from keybert import KeyBERT

import random
def title_description_field_to_list_of_text_label_pair(field: List[dict]) -> List[Tuple[str, float]]: 
    return [
        (
            f"{experience_point['value']['title']} \n {experience_point['value']['description']}",
            #experience_point['label']
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
    res += title_description_field_to_list_of_text_label_pair(resume['experience']['value'])
        
    # Extract education
    res += title_description_field_to_list_of_text_label_pair(resume['education']['value'])
    # summary 
    res += [(resume['summary']['value'], resume['summary']['label'])]

    # interests
    res += list_of_text_label_pairs_from_key_val_list(resume['interests']['value'])

    # Accomplishements
    res += title_description_field_to_list_of_text_label_pair(resume['accomplishments']['value'])

    # projects
    res += title_description_field_to_list_of_text_label_pair(resume['projects']['value'])

    # languages
    res += list_of_text_label_pair_from_skill_based_list(resume['languages']['value'])

    # softSkills
    res += list_of_text_label_pair_from_skill_based_list(resume['softSkills']['value'])

    # hard skills
    res += list_of_text_label_pair_from_skill_based_list(resume['hardSkills']['value'])

    #certifications
    res += title_description_field_to_list_of_text_label_pair(resume['certifications']['value'])

    # patents
    res += list_of_text_label_pairs_from_key_val_list(resume['patents']['value'])

    # extracurriculars 
    res += title_description_field_to_list_of_text_label_pair(resume['extracurriculars']['value'])
    return res



def extract_keywords_from_text(texts: List[str]) -> List[Tuple[str, float]]:
    """Takes in text and outputs the most relevant keywords with an attached score
    
    Based on the keybert model
    """
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(texts, # passing all texts to process in paralell 
                                         keyphrase_ngram_range=(1, 2),  # using up to 2-grams
                                         top_n=40, # how many keywords we max want to find from each text
                                         stop_words='english', 
                                         use_mmr=True, diversity=0.8, # high value to make the keywords as distinct as possible
                                        )
    
    
    return keywords

def find_frequency_of_term_in_texts(term: str, texts: List[str]) -> float:
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(texts, candidates=[term])
    
    return keywords