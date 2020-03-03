import re

def removeLinks(line):
    line = str(line)
    #HTML and links
    regy1 = r'http\S+'
    regy2 = r'pic.twitter.com\/[a-zA-Z0-9]+'
    new_text = re.sub(regy1, '', line)
    new_text = re.sub(regy2, '', new_text)
    return new_text

from cltk.corpus.arabic.utils.pyarabic import araby
def normalize(line):
    string = line.split()
    new_string = []
    for s in string:
        newr = s
        newr = araby.normalize_hamza(newr)
        newr = araby.normalize_ligature(newr)
        newr = araby.strip_harakat(newr)
        newr = araby.strip_tatweel(newr)
        newr = araby.strip_tashkeel(newr)
        newr = araby.strip_shadda(newr)

        haa = r'ه|ة'
        newHaa = r'ه'
        newr = re.sub(haa, newHaa, newr)
        
        haa = r'ء'
        newHaa = r'ا'
        newr = re.sub(haa, newHaa, newr)
        
        new_string.append(newr)

    new_res = " ".join(new_string)
    
    return new_res

def removeDCaracters(line):
    regy1 = r'([ا-ي])\1+'
    new_text = re.sub(regy1, r'\1', line)
    return new_text

def removeEnglishLetters(line):
    regy1 = r'[a-zA-Z]'
    new_text = re.sub(regy1, r'', line)
    return new_text

from nltk.stem.snowball import ArabicStemmer
steme = ArabicStemmer()
def stemmer(line):
    string = line.split()
    new_string = []
    for s in string:
        new_string.append(steme.stem(s))
    new_res = " ".join(new_string)
    return new_res

def textRemoveNumbers(input_str):
    return re.sub(r'\d', '', input_str)

def textRemovePunctuation(input_str):
    import string
    table = str.maketrans({key: None for key in string.punctuation})
    return input_str.translate(table)

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

def textRemoveStopWords(input_str):
    
    stop_words = set(stopwords.words('arabic'))
    
    stop_words.add(',')
    stop_words.add('لس')
    stop_words.add('ب')
    stop_words.add('لس،')
    
    word_tokens = word_tokenize(input_str) 
    
    result = [i for i in word_tokens if not i in stop_words]
    
    
    
    filtered_string = ""
    for word in result:
        filtered_string = filtered_string + word + " "
    return filtered_string
