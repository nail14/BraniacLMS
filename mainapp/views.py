from django.shortcuts import HttpResponse, render
from django.views.generic import TemplateView  # , ListView
from datetime import datetime
from django.core.paginator import Paginator
from mainapp.models import News
from django.shortcuts import get_object_or_404
from mainapp import models as mainapp_models


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


# class NewsPageView(TemplateView):
#     template_name = "mainapp/news.html"
#
#     def get_context_data(self, **kwargs):
#         # Get all previous data
#         context = super().get_context_data(**kwargs)
#         # Create your own data
#         context["news_qs"] = mainapp_models.News.objects.all()[:3]
#         return context
class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"
    paginated_by = 8

    def get_context_data(self, **kwargs):
          page_number = self.request.GET.get(
              'news_qs',
              1
          )
          paginator = Paginator(News.objects.all(), self.paginated_by)
          news_qs = paginator.get_page(page_number)
          context = super().get_context_data(**kwargs)
          context['news_qs'] = news_qs
          return context


class NewsPageDetailView(TemplateView):
    template_name = "mainapp/news_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(mainapp_models.News, pk=pk)
        return context


class CoursesListView(TemplateView):
    template_name = "mainapp/courses_list.html"

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["objects"] = mainapp_models.Courses.objects.all()[:7]
        return context


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(mainapp_models.Courses, pk=pk)
        context["lessons"] = mainapp_models.Lesson.objects.filter(course=context["course_object"])
        context["teachers"] = mainapp_models.CourseTeachers.objects.filter(course=context["course_object"])
        return context


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"




# # def hello_view(request):
# #     return HttpResponse("Hello world")
#
#
# class MainPageView(TemplateView):
#     template_name = "mainapp/index.html"
#
#
# class ContactPageView(TemplateView):
#     template_name = "mainapp/contacts.html"
#
#
# class CoursesPageView(TemplateView):
#     template_name = "mainapp/courses_list.html"
#
#     # def get(self, request, word, *args, **kwargs):
#     #     super(CoursesPageView, self).get()
#
#
# class DocSitePageView(TemplateView):
#     template_name = "mainapp/doc_site.html"
#
#
# class LoginPageView(TemplateView):
#     template_name = "mainapp/login.html"
#
#
# class NewsPageView(TemplateView):
#     template_name = "mainapp/news.html"
#     paginated_by = 3
#
#     def get_context_data(self, **kwargs):
#         page_number = self.request.GET.get(
#             'page',
#             1
#         )
#         paginator = Paginator(News.objects.all(), self.paginated_by)
#         page = paginator.get_page(page_number)
#
#         context = super().get_context_data(**kwargs)
#
#         context['page'] = mainapp_models.News.objects.all()[:5] # page
#         return context
#
# # class NewsPageView2(TemplateView):
# #     template_name = "mainapp/news.html"
# #
# #     def get_context_data(self, **kwargs):
# #     # Get all previous data
# #     context = super().get_context_data(**kwargs)
# #     # Create your own data
# #     context["news_qs"] = mainapp_models.News.objects.all()[:5]
# #     return context
# class NewsPageDetailView(TemplateView):
#     template_name = "mainapp/news_detail.html"
#     def get_context_data(self, pk=None, **kwargs):
#     context = super().get_context_data(pk=pk, **kwargs)
#     context["page"] = get_object_or_404(mainapp_models.News, pk=pk)
#     return context
#
#
# class NewsDetailsPageView(TemplateView):
#     template_name = "mainapp/news_detail.html"
#
#     def get_context_data(self, pk=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         # qs News.objects.filter(pk=pk)
#         # if qs:
#         #     context['news_obj'] = qs[0]
#         # else:
#         #     return HttpResponseNotFound()
#         context['news_object'] = get_object_or_404(News, pk=pk)
#         return context
