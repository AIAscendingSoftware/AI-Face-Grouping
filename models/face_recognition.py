from services.face_detection_service import detect_faces, align_face
from services.face_embedding_service import extract_embedding
from services.image_processing_service import compare_faces, separate_unique_data
from utils.helpers import convert_binary_to_image

def process_event_data(data):
    event_faces = process_event_images(data['EventImages'])
    user_faces = process_user_images(data['UserImages'])
    similar_faces = compare_faces(user_faces, event_faces)
    return separate_unique_data(similar_faces)

def process_event_images(event_images):
    processed_faces = []
    for image_data in event_images:
        image = convert_binary_to_image(image_data['image'])
        if image is not None:
            faces = detect_faces(image)
            for face in faces:
                x1, y1, x2, y2 = face
                face_img = image[y1:y2, x1:x2]
                embedding = extract_embedding(face_img)
                if embedding is not None:
                    processed_faces.append({
                        "eventFolderPath": image_data['eventFolderPath'],
                        'ImageName': image_data['ImageName'],
                        "encoding": embedding,
                        'OrgId': image_data['OrgId'],
                        'EventId': image_data['EventId']
                    })
    return processed_faces

def process_user_images(user_images):
    processed_faces = []
    for user_data in user_images:
        for image in user_data.get('image', []):
            image_data = convert_binary_to_image(image)
            if image_data is not None:
                faces = detect_faces(image_data)
                for face in faces:
                    x1, y1, x2, y2 = face
                    face_img = image_data[y1:y2, x1:x2]
                    embedding = extract_embedding(face_img)
                    if embedding is not None:
                        processed_faces.append({
                            'UserId': user_data["UserId"],
                            "encoding": embedding
                        })
    return processed_faces