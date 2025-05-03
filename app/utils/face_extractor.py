from mtcnn.mtcnn import MTCNN
import numpy as np
import cv2

def extract_face(img_array):
    detector = MTCNN()
    faces = detector.detect_faces(img_array)

    if not faces:
        return None

    x, y, width, height = faces[0]['box']
    face = img_array[y:y+height, x:x+width]
    face = cv2.resize(face, (256, 256))
    return face / 255.0
