from . import views
from django.urls import path

urlpatterns = [
    path("", views.AlbumList.as_view(), name="home"),
    path('<slug:slug>/', views.AlbumDetail.as_view(), name='album_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('artist_slug/<int:pk>', views.ArtistDetail.as_view(), name='artist'),
    path('<slug:slug>/<int:pk>/delete_comment/',
         views.CommentDelete.as_view(), name="delete_comment"),
    path('<slug:slug>/<int:pk>/edit_comment/',
         views.CommentEdit.as_view(), name="edit_comment"),

    path('403', views.Page403.as_view(), name='403'),
    path('404', views.Page404.as_view(), name='404'),
    path('500', views.Page500.as_view(), name='500'),
]