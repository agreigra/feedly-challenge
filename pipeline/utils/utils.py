import re
import nltk
from nltk.corpus import stopwords
import string


def intersection(tokens1, tokens2):
    """Finds the number of tokens shared by two nodes
    
    Parameters
    ----------
    node1, node2 : node
    
    Returns
    -------
    int: number of tokens shared by the two nodes
    """
    return len(list(set(tokens1) & set(tokens2)))



    # removing HTML tags from the articles
def remove_tags(text):
    """Remove HTML tags from a given text
    
    Parameters
    ----------
    text: str
        text to clean from html tags
        
    Returns
    -------
        : str
        clean text
    """
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)


def extract_tokens(text):
    """Extracts tokens from a given text
    
    Parameters
    ----------
    text: str
        text to be splited to tokens
    Returns
    -------
    res : list
        list of tokens in the text
    """
    res = []
    for sent in nltk.sent_tokenize(text):
        tmp_res = nltk.word_tokenize(sent)
        for token in tmp_res:
            res += re.split("[\./]", token)
    return res


def clean_tokens(tokens):
    """Removes punctuation marks from tokens
    Parameters
    ----------
    tokens: list
        list to be cleaned from punctuation marks
    
    Returns
    -------
    list:
        list cleaned from punctuation marks
    """
    return [token.lower() for token in tokens if token not in string.punctuation]


def remove_stop_words(tokens):
    """Removes stopwords from our tokens
    
    Parameters
    ----------
    tokens: list 
        list of tokens to be cleaned from stopwords
        
    Returns
    -------
        :list
        list cleaned from stopwords
    """
    GARBAGE = {"'s", "n't", '...', 'oh',"'m", "'re", "'", "''", "'ve", "'ll", "'d", "``" }
    STOP_WORDS = set(stopwords.words('english')).union(GARBAGE)
    return [token for token in tokens if token not in STOP_WORDS]

def text2tokens(text):
    """Used to combine three previous functions in one operation.
    Parameters
    ----------
    Text: str
        text to be cleaned
    Returns
    -------
    tokens: list
        list of tokens cleaned
    """
    text = remove_tags(text)
    tokens = extract_tokens(text)
    tokens = clean_tokens(tokens)
    tokens = remove_stop_words(tokens)
    return tokens
