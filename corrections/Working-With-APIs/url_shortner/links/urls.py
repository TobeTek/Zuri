from django.urls import path
from . import views

app_name = "link"

urlpatterns = [
    path("active/", views.ActiveLinkView.as_view(), name="active_link"),
    path("recent/", views.RecentLinkView.as_view(), name="recent_link"),

    path("create/", views.LinkCreateApi.as_view(), name="api_create"),
    path("update/<int:pk>", views.LinkUpdateApi.as_view(), name="api_update"),
    path("delete/<int:pk>", views.LinkDeleteApi.as_view(), name="api_delete"),
    path("", views.LinkListApi.as_view(), name="api_list"),

]