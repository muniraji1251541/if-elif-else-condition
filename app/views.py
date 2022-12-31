from django.shortcuts import render

# Create your views here.
def numb(request):
    d={'a':45,'b':24,'c':36}
    return render(request,'numb.html',d)