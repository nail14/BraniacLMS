from django.shortcuts import HttpResponse, render
from django.views.generic import TemplateView

# def hello_view(request):
#     return HttpResponse("Hello world")


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class ContactPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"
