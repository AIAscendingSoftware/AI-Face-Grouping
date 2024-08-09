import cv2
import numpy as np
import pickle
import io

def convert_binary_to_image(binary_string):
    try:
        nparr = np.frombuffer(binary_string, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return image
    except Exception as e:
        print(f"Error converting binary to image: {str(e)}")
        return None

def deserialize_binary_response(binary_response):
    byte_stream = io.BytesIO(binary_response)
    response = pickle.load(byte_stream)
    return response

# Usage:
# Assuming 'binary_response' is your serialized data
# response = deserialize_binary_response(binary_response)