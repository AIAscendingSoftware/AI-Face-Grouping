import os

class Config:
    API_URL = 'http://192.168.29.64:8083/api/facedetection/' #saran id
    # API_URL = 'http://192.168.29.96:5000/api/facedetection' #my id
    SIMILARITY_THRESHOLD = 0.6
    MAX_WORKERS = 4  # Number of worker threads for processing tasks