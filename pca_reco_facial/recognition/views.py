import os
from django.conf import settings
from django.shortcuts import render, redirect

from recognition.utils import recognize_face
from .forms import FaceUploadForm
from .models import Face

# Create your views here.

def upload_face(request):
    if request.method == "POST":
        form = FaceUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('face_list')
    else:
        form = FaceUploadForm()
    return render(request, 'recognition/upload.html', {'form': form})

def face_list(request):
    faces = Face.objects.all()
    return render(request, 'recognition/face_list.html', {'faces': faces})

def recognize_view(request):
    result = None

    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]
        img_path = os.path.join(settings.MEDIA_ROOT, "test.jpg")

        with open(img_path, "wb") as f:
            for chunk in image.chunks():
                f.write(chunk)

        result = recognize_face(img_path)

    return render(request, "recognition/recognize.html", {"result": result})
