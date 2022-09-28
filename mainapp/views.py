from django.http import HttpResponseNotFound
from django.shortcuts import HttpResponse, render
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from datetime import datetime
from .models import News
from django.shortcuts import get_object_or_404


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
    paginated_by = 3

    def get_context_data(self, **kwargs):
          page_number = self.request.GET.get(
              'page',
              1
          )
          paginator = Paginator(News.objects.all(), self.paginated_by)
          page = paginator.get_page(page_number)
          context = super().get_context_data(**kwargs)
          context['page'] = page
          return context


class NewsDetailsPageView(TemplateView):
    template_name = ""

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # qs News.objects.filter(pk=pk)
        # if qs:
        #     context['news_obj'] = qs[0]
        # else:
        #     return HttpResponseNotFound()
        context['news_obj'] = get_object_or_404(News, pk=pk)
        return context



        # try:
        #     context['news_obj'] = News.objects.get(pk=pk)
        # except Exception:
        #     return HttpResponseNotFound("Not Found")

    #     context = super().get_context_data(**kwargs)
    #
    #     # context['news_title'] = 'Новость'
    #     # context['description'] = 'Предварительное описание новости'
    #     # context['news_date'] = datetime.now()
    #     context['news'] = News.objects.all()
    #     # context['range'] = range(5)
    #     return context

    # def get_context_data(self, pk=None, **kwargs):
    #     context = super().get_context_data(pk=pk, **kwargs)
    #
    #     context["news_object"] = get_object_or_404(mainapp_models.News, pk=pk)
    #     return context
