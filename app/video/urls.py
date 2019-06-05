from django.urls import path

from . import views

urlpatterns = [
    path('', views.VideoListView.as_view(), name="video_index"),
    path('s/<collection>/', views.VideoListView.as_view(), name="video_index"),
    path('process/<int:vid_pk>/', views.process_video, name='process_video'),
    path('get/<slug:slug>/<filetype>', views.get_video, name="getter_file"),
    path('play/<slug:slug>/', views.VideoPlayerView.as_view(), name="video_player"),
    path('form/', views.form_view, name="video_form"),
    path('api/chunked_upload/', views.MyChunkedUploadView.as_view(), name='api_chunked_upload'),
    path('api/chunked_upload_complete/', views.MyChunkedUploadCompleteView.as_view(), name='api_chunked_upload_complete'),
    path('api/colleciton_autocomplete/', views.CollectionAutocomplete.as_view(create_field='title'), name='api_collection_autocomplete'),
]
