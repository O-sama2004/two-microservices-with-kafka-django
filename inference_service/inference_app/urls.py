from django.urls import path
from .views import latest_inference_image, webcam_view

urlpatterns = [
    path('inference/latest/', latest_inference_image, name='latest_inference_image'),
    path('webcam/', webcam_view, name='webcam_view'),
]