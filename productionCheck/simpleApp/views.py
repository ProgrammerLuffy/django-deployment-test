from django.shortcuts import render


from django.views.generic import TemplateView



class hello(TemplateView):
    template_name = "simpleApp/home.html"
    