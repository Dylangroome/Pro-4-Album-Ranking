from . import views
from django.urls import path

urlpatterns = [
    path("", views.AlbumList.as_view(), name="home"),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('<slug:slug>/', views.AlbumDetail.as_view(), name='album_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('artist_slug/<int:pk>', views.ArtistDetail.as_view(), name='artist'),

    path('403', views.Page403.as_view(), name='403'),
    path('404', views.Page404.as_view(), name='404'),
    path('500', views.Page500.as_view(), name='500'),
]