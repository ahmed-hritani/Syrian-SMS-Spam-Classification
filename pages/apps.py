from django.apps import AppConfig
from django.conf import settings
import os
import pickle

class PagesConfig(AppConfig):
    name = 'pages'

    # Path to the models
    path = os.path.join(settings.MODELS, 'models.p')

    # Extract the models from the pickle jar :)
    with open(path, 'rb') as pickled:
       models = pickle.load(pickled)

    featureExtraction = models['featureExtraction']
    chi2 = models['chi2']
    svm = models['svm']
