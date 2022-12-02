from typing import Dict, List


class Job(object):
    def __init__(self, name: str):
        self.name = name
        self.keywords: Dict[str, float] = {}

    def set_keywords(self, keywords):
        self.keywords = keywords

    def load_from_csv_data(self, csv_data: str):
        """Loads keyword scores from a pretrained csv file"""
        if len(csv_data) == 0:
            # Dummy value to make sure operations should work ok
            self.keywords['CV'] = 1.0
            return
        for line in csv_data.split("\n"):
            word, score = line.split(",")
            self.keywords[word.lower()] = float(score)

    def update_keywords_from_description(self, description_keywords: List[str]):
        """Uppdates the keyword dict with values from a job description"""
        for kw in description_keywords:
            # For now we use a baseline of 0.3 for non-included keywords
            # This is to prevent issues were we extract wierd keywords
            # from the description, and to make sure that an overlap
            # would indicate high importance for a word
            # The numeical values are heuristic
            prev_score = self.keywords.get(kw, 0.3)
            self.keywords[kw] = prev_score + 0.6
    
