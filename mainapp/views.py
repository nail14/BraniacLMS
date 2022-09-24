from django.shortcuts import HttpResponse, render
from django.views.generic import TemplateView, ListView
from datetime import datetime


# def hello_view(request):
#     return HttpResponse("Hello world")


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class ContactPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"

    # def get(self, request, word, *args, **kwargs):
    #     super(CoursesPageView, self).get()


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['news_title'] = 'Новость'
        context['description'] = 'Предварительное описание новости'
        context['news_date'] = datetime.now()
        context['range'] = range(5)
        return context
