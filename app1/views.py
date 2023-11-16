from django.shortcuts import render

# Create your views here.
def virat(request):
    d={'totalcenturies':80}
    return render(request,'virat.html',context=d)