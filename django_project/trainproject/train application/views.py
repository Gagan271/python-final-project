from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
 return render(request,'train/timings.html')

