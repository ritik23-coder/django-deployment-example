from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method=='POST':
      form = forms.FormName(request.POST)
      if form.is_valid():
          print("VALIDATION SUCCESS")
          form.cleaned_data("NAME: "+form.cleaned_data['name'])
          form.cleaned_data("EMAIL: "+form.cleaned_data['email'])
          form.cleaned_data("NAME: "+form.cleaned_data['text'])

    return render(request,'basicapp/form_page.html',{'form':form})
