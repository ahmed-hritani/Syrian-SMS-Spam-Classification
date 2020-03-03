from django.shortcuts import render
from pages.util.preprocessing import removeLinks, normalize
from pages.util.classifier import readInputAndClassify
from .apps import PagesConfig

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def classify(request):
    # Get the message
    message = request.POST['message']
    prediction = readInputAndClassify(PagesConfig.featureExtraction, PagesConfig.svm, PagesConfig.chi2, message)
    print(prediction)
    return render(request, 'pages/index.html')
