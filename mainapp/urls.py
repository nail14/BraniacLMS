from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path("news/", views.NewsListView.as_view(), name="news"),
    path("news/create/", views.NewsCreateView.as_view(), name="news_create"),
    path(
        "news/<int:pk>/detail",
        views.NewsDetailView.as_view(),
        name="news_detail",
    ),
    path(
        "news/<int:pk>/update",
        views.NewsUpdateView.as_view(),
        name="news_update",
    ),
    path(
        "news/<int:pk>/delete",
        views.NewsDeleteView.as_view(),
        name="news_delete",
    ),
    path("courses/", views.CoursesListView.as_view(), name="courses"),
    path(
        "courses/<int:pk>/",
        views.CoursesDetailView.as_view(),
        name="courses_detail",
    ),
    path(
        "course_feedback/",
        views.CourseFeedbackFormProcessView.as_view(),
        name="course_feedback",
    ),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("doc_site/", views.DocSitePageView.as_view(), name="doc_site"),
]




# from django.urls import path
#
# from .views import *
# # from mainapp import views
# from mainapp.apps import MainappConfig
#
# app_name = MainappConfig.name
#
# urlpatterns = [
#     path("", MainPageView.as_view(), name='main'),
#     # path("login/", LoginPageView.as_view(), name='login'),
#     path("doc_site/", DocSitePageView.as_view(), name='docs'),
#     path("contacts/", ContactsPageView.as_view(), name='contacts'),
#     path("news/", NewsPageView.as_view(), name='news'),
#     path("news/<int:pk>", NewsPageDetailView.as_view(), name='news_detail'),
#     # path("courses/", CoursesListView.as_view(), name="courses"),
#     path("courses/<int:pk>/", CoursesDetailView.as_view(), name="courses_detail",),
#     path("courses_list/", CoursesListView.as_view(), name='courses'),
# ]
