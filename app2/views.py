from django.shortcuts import render

# Create your views here.
def rohit(request):
    k={'worldcup':'3rd'}
    return render(request,'rohit.html',context=k)
