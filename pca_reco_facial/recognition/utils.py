import cv2
import numpy as np
import os
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from django.conf import settings
from .models import Face

def load_images():
    images = []
    labels = []
    label_map = {}

    faces = Face.objects.all()
    for i, face in enumerate(faces):
        img_path = os.path.join(settings.MEDIA_ROOT, str(face.image))
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (100, 100))
        images.append(img.flatten())
        labels.append(i)
        label_map[i] = face.name

    return np.array(images), np.array(labels), label_map

def train_model():
    X, y, label_map = load_images()
    
    if len(X) < 2:
        return None, None, None  # Pas assez d'images pour entraîner

    pca = PCA(n_components=min(50, len(X)))
    X_pca = pca.fit_transform(X)

    clf = SVC(kernel='rbf', probability=True)
    clf.fit(X_pca, y)

    return pca, clf, label_map

def recognize_face(image_path):
    pca, clf, label_map = train_model()
    if pca is None:
        return "Pas assez de données"

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (100, 100))
    img = img.flatten().reshape(1, -1)

    img_pca = pca.transform(img)
    prediction = clf.predict(img_pca)[0]

    return label_map.get(prediction, "Inconnu")
