from typing import List, Dict


class Job(object): 
    def __init__(self, name: str): 
        self.name = name
        self.keywords: Dict[str, float] = {}
        
    def set_keywords(self, keywords): 
        self.keywords = keywords
        
    def relevance(self, keyword_list: List[str]) -> float:
        return sum(list([self.keywords.get(k, 0) for k in keyword_list]))
        
        