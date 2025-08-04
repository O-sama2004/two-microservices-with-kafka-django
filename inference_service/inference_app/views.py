from django.shortcuts import render

from django.http import FileResponse, Http404
import os

def latest_inference_image(request):
    file_path = '/output/inferenced_frame.jpg'  # this is where your consumer saves
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='image/jpeg')
    else:
        raise Http404("Inference output not found")

# Optional: live-refresh HTML page
from django.shortcuts import render

def webcam_view(request):
    return render(request, 'webcam.html')