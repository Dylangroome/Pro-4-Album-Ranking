from . import views
from django.urls import path

urlpatterns = [
    path("", views.AlbumList.as_view(), name="home"),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('contact/', views.ContactTemplateView.as_view(), name='contact'),
    path('<slug:slug>/', views.PostTemplateView.as_view(), name='post'),
    # path('post/', views.PostTemplateView.as_view(), name='post')
]