# Chap02-03/twitter_term_frequency.py
import sys
import string
import json
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
    """Process the text of a tweet:
    - Lowercase
    - Tokenize
    - Stopword removal
    - Digits removal
    Return: list of strings
    """ 
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return [tok for tok in tokens if tok not in stopwords and not
    tok.isdigit()]

def normalize_contractions(tokens):
 token_map = {
 "i'm": "i am",
 "you're": "you are",
 "it's": "it is",
 "we're": "we are",
 "we'll": "we will",
 }
 for tok in tokens:
    if tok in token_map.keys():
     for item in token_map[tok].split():
        yield item
    else:
     yield tok

if __name__ == '__main__': 
 fname = sys.argv[1]
 tweet_tokenizer = TweetTokenizer()
 punct = list(string.punctuation)
 stopword_list = stopwords.words('english') + punct + ['rt','via', '...']
 tf = Counter()
 with open(fname, 'r') as f:
     for line in f:
        tweet = json.loads(line)
        tokens = process(text=tweet['text'],
        tokenizer=tweet_tokenizer,
        stopwords=stopword_list)
        tf.update(tokens)
     for tag, count in tf.most_common(40):
        print("{}: {}".format(tag, count))
 

