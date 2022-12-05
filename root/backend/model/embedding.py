from typing import List, Tuple
from gensim.models import Word2Vec
import numpy as np

model = Word2Vec.load("model/embedding/model_skill_extraction")
word_vec = model.wv


def embedding_for_keyword_list(keywords: List[str]) -> List[np.ndarray]:
    """Returns a list of embeddings for the keywords"""
    return [embedding_for_word(kw) for kw in keywords]


def embedding_for_word(word: str) -> np.ndarray:
    """Tries to find an embedding for a word. 
    If it can't, it returns a zero vector, or the closest
    vector it can based on vector addition of splitting
    on spaces"""
    try:
        return word_vec[word]
    except:
        # The exact word is not in our vocabulary
        # First solution is to try and split, and use
        # Vector addition to get the best embedding
        embedding = np.zeros(300)
        for split_word in word.split(" "):
            try:
                part = np.array(word_vec[split_word])
                embedding += part
            except:
                # There was a part of the phrase that is not included
                # We just ignore it.
                # If the entire phrase is then not included, the
                # result will be the null-vector
                pass
        return embedding


def closest_keyword_index(sample: str, embedded_keywords: List[np.ndarray]) -> Tuple[int, float]:
    """Returns the index of the closest keyword from the list, together
    with the cosine similarity between the sample and the keyword"""
    sample_embedding = embedding_for_word(sample)

    sims = word_vec.cosine_similarities(sample_embedding, embedded_keywords)
    sims = sims[~np.isnan(sims)]
    if len(sims) == 0:
        return -1, 0.0
    closest = np.argsort(sims)[::-1][0]
    closest_sim = sims[closest]

    return closest, closest_sim
