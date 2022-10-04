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
from django.contrib.auth import views as auth_views
from authapp.views import *
# from .views import *
from authapp.apps import AuthappConfig

app_name = AuthappConfig.name


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),

    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile_edit/", ProfileEditView.as_view(), name="profile_edit"),
]