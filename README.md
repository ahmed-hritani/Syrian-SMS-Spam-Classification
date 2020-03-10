# Syrian-SMS-Spam-Classification

The building of this project consisted of two main parts:
1. Creating the machine learning model
2. Creating the app that puts this model into action

I will start by discussing the first part, the machine learning model consists of five main parts:
1. Data Acquisition:
   - the data was collected from the phones of friends and family and it contains private messages, for that reason the messages can not be shared, however you can use the pickeled feature extractor, feature engineering  and classification models
   
   
2. Text Preprocessing(you can find the implementation for the folowing steps in preprocessing.py):
   - Links removal
   - Characters normalization
   - Repeated characters removal
   - English letters removal
   - Light stemming
   - Numbers removal
   - Stopwords removal
   - Specefic characters removal(these characters were chosen based on my knowledge of the language)
   
   
3. Feature Extraction:
   - Bag of words
   - TF-IDF
   
Bag of words was chosen because it had achived higher precision rates than TF-IDF


4. Feature Selection:
   - Chi2
   
   
5. Classification Model:
   - Naive Bayes
   - SVM
   - ANN
   
Support Vector Machine was chosen because it had achived higher precision rates than TF-IDF.

The web application consists of one app(in Django's language), the controller interacts with the preprocessing fucntions in the preprocessing.py file by calling **readInputAndClassify** function, which takes the pickled models and the message and returns the class of the message
