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
#     path("login/", LoginPageView.as_view(), name='login'),
#     path("doc_site/", DocSitePageView.as_view(), name='docs'),
#     path("contacts/", ContactsPageView.as_view(), name='contacts'),
#     path("news/", NewsPageView.as_view(), name='news'),
#     path("news/<int:pk>", NewsPageDetailView.as_view(), name='news_detail'),
#     path("courses/", CoursesListView.as_view(), name="courses"),
#     path("courses/<int:pk>/", CoursesDetailView.as_view(), name="courses_detail",),
#     path("courses_list/", CoursesListView.as_view(), name='courses'),
# ]
from django.urls import path

from authapp import views
from authapp.apps import AuthappConfig

app_name = AuthappConfig.name

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path(
        "profile_edit/<int:pk>/",
        views.ProfileEditView.as_view(),
        name="profile_edit",
    ),
]