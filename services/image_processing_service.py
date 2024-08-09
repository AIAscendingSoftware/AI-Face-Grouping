import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def compare_faces(user_faces, event_faces, threshold=0.6):
    similar_faces = []
    for user_face in user_faces:
        user_encoding = user_face["encoding"]
        for event_face in event_faces:
            event_encoding = event_face["encoding"]
            similarity = cosine_similarity([user_encoding], [event_encoding])[0][0]
            if similarity > threshold:
                similar_faces.append({
                    "imagePath": event_face['eventFolderPath'],
                    'imageName': event_face['ImageName'],
                    'orgId': event_face['OrgId'],
                    'userId': user_face['UserId'],
                    'eventId': event_face['EventId'],
                    'imageId': 1,
                    'similarityScore': similarity,
                    "Angry": 1, "Disgust": 2, "Fear": 3, "Happy": 4,
                    "Sad": 5, "Surprise": 6, "Neutral": 7
                })
    return similar_faces

def separate_unique_data(similar_faces):
    unique_data = {}
    for item in similar_faces:
        key = (item['imagePath'], item['imageName'], item['orgId'], item['userId'], item['eventId'])
        if key not in unique_data:
            unique_data[key] = item
    return list(unique_data.values())