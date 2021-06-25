from django.urls import path
from . import views

urlpatterns = [
    path("social-list/", views.SocialList.as_view()),
    path("social-create/", views.SocialLinkCreate.as_view()),
]
