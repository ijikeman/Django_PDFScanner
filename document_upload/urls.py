from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_document, name='upload_document'), # /upload/にアクセスするとviews.pyのupload_document関数が呼び出される
]
