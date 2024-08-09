import cv2
import numpy as np
from retinaface import RetinaFace

def detect_faces(image, min_confidence=0.9):
    faces = RetinaFace.detect_faces(image)
    return [face['facial_area'] for face in faces.values() if face['score'] >= min_confidence]

def align_face(image, landmarks):
    left_eye = landmarks['left_eye']
    right_eye = landmarks['right_eye']
    
    dY = right_eye[1] - left_eye[1]
    dX = right_eye[0] - left_eye[0]
    angle = np.degrees(np.arctan2(dY, dX)) - 180

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    aligned = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC)

    return aligned