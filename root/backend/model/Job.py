from typing import Dict, Tuple


class Job(object): 
    def __init__(self, name: str): 
        self.name = name
        self.keywords: Dict[str, float] = {}
        
    def set_keywords(self, keywords): 
        self.keywords = keywords
        
    
    
    def load_from_csv_data(self, csv_data: str): 
        """Loads keyword scores from a pretrained csv file"""
        if len(csv_data) == 0:
            self.keywords['CV'] = 1.0 # Dummy value to make sure operations should work ok
            return
        for line in csv_data.split("\n"):
            word, score = line.split(",")
            self.keywords[word] = float(score)
        
        
    def weights_to_csv(self) -> str: 
        """Output the trained weights as csv format"""
    
    def save_to_gs_bucket(self): 
        """Save model to gs bucket for reuse"""
        pass
    
    
