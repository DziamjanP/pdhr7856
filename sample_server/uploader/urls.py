from django.contrib import admin
from django.urls import path

from .views import UploadJSONView

urlpatterns = [
    path('upload/', UploadJSONView.as_view(), name='upload_json'),
]
