from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def classify(request):
    # Get the message
    message = request.POST['message'].strip()
    print(message)
    return render(request, 'pages/index.html')
