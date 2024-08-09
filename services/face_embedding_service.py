import torch
import cv2
from torchvision import transforms
from facenet_pytorch import InceptionResnetV1

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = InceptionResnetV1(pretrained='vggface2').eval().to(device)

def extract_embedding(face_img):
    try:
        # aligned_face = align_face(face_img, landmarks)
        face_img = cv2.resize(face_img, (160, 160))
        face_img = transforms.ToTensor()(face_img).unsqueeze(0).to(device)
        with torch.no_grad():
            embedding = model(face_img).cpu().numpy()
        return embedding.flatten()
    except Exception as e:
        print(f"Error in extract_embedding: {str(e)}")
        return None