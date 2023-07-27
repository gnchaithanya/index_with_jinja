from django.shortcuts import render

# Create your views here.
def index(request):
    d={'name':'chaithu','age':20,'marks':400}
    return render(request,'index.html',context=d)
