from model.keyword_utils import extract_keywords_from_text, title_description_field_to_list_of_text_label_pair
from model.Job import Job
from copy import deepcopy
import numpy as np


class ResumeScorer():
    def __init__(self):
        pass
    
     
    def score_text(self, text: str, job: Job) -> float: 
        """Scores a piece of text based on the relevance to the job"""
        keywords = extract_keywords_from_text([text])
        
        scores = []
        for kw in keywords:
            if kw[0] in job.keywords: 
                scores.append(kw[1] * job.keywords[kw[0]])
            else: 
                scores.append(0.0) #TODO: update this
                # use embedding similarity measure for computing score
                pass
                
        
        # scores =  sum(list([job.keywords.get(k[0], 0) * k[1] for k in keywords]))
        return np.mean(scores)
            
    
    
    
    def score_title_description_field(self, field_name: str, output: dict, job: Job): 
        """Takes a field name and output dict and updates the score of the filed
        Works only for fields where we use title + description"""
        texts = title_description_field_to_list_of_text_label_pair(output[field_name]['value'])
        for i, t in enumerate(texts):
            score = self.score_text(t[0], job)
            output[field_name]['value'][i]['label'] = score
            
    def score_name_proficiency_field(self, field_name: str, output: dict, job: Job): 
        """Takes a field name and output dict and updates the score of the filed
        Works only for a name + proficiency field"""
        for field in output[field_name]['value']:
            relevance = self.score_text(field['value']['name'], job ) * field['value']['proficiency'] / 5
            field['label'] = relevance
            
    def score_pure_text_field(self, field_name: str, output: dict, job: Job):
        for field in output[field_name]['value']:
            score = self.score_text(field['value'], job)
            field['label'] = score
        
    def score_resume(self, resume: dict, job: Job) -> dict:
        """Takes a resume with labels (can be set to zero) and returns the same resume
        with labels updated according to our model"""


        # Create a deep copy for the output to make sure
        # we dont modify the input data in any way 
        output = deepcopy(resume)
        
        # summary 
        summary_score = self.score_text(resume['summary']['value'], job)
        output['summary']['label'] = summary_score
        
        
        #experience
        self.score_title_description_field('experience', output, job)

        # Education
        self.score_title_description_field('education', output, job)

        # Skills
        ## hard
        self.score_name_proficiency_field('hardSkills', output, job)
        
        ## soft
        self.score_name_proficiency_field('softSkills', output, job)
        
        # languages
        self.score_name_proficiency_field('languages', output, job)
            
        # certifications
        self.score_title_description_field('certifications', output, job)
            
        # accomplishements
        self.score_title_description_field('accomplishments', output, job)
            
        # projects
        self.score_title_description_field('projects', output, job)
            
        # extracurriculars
        self.score_title_description_field('extracurriculars', output, job)
        
        # patents
        self.score_pure_text_field('patents', output, job)
        
        
        # interests 
        self.score_pure_text_field('interests', output, job)
        
        return output
        