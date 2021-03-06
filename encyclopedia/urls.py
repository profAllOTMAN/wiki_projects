from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/",views.search,name="search"),
    path("wiki/<str:title>",views.wiki,name="wiki"),
    path("creat-new-page/",views.create_page, name="create-page"),
]
