from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home.html')
def group(request):
    return render(request, 'groups.html')
def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

