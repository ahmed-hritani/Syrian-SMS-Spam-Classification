from pages.util.preprocessing import *

def cleanUserInputData(string):
    
    newString = string[:]
    newString = removeLinks(newString)
    newString = normalize(newString)
    newString = removeDCaracters(newString)
    newString = stemmer(newString)
    newString = textRemoveNumbers(newString)
    newString = removeEnglishLetters(newString)
    newString = textRemovePunctuation(newString)
    newString = textRemoveStopWords(newString)
    
    return newString

def featureExtractionUserInputData(feModel, message):
    return feModel.transform(message)

def classify(message, classifier):
    if classifier.predict(message) == 1:
        return 'SPAM'
    else:
        return 'HAM'

def readInputAndClassify(feModel, classifier, ch2, message):
    message = cleanUserInputData(message)
    message = featureExtractionUserInputData(feModel, [message])
    message = featureExtractionUserInputData(ch2, message)
    return classify(message, classifier)
