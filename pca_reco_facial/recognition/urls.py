from django.urls import path
from .views import recognize_view, upload_face, face_list

urlpatterns = [
    path('upload/', upload_face, name='upload_face'),
    path('faces/', face_list, name='face_list'),
    path('recognize/', recognize_view, name='recognize'),

]
