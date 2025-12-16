from fastapi import FastAPI, File, UploadFile
from tensorflow import keras
import numpy as np
from PIL import Image
import io

model = keras.models.load_model('../150_epoch_facial_model.keras')

async def verify_human(file_contents: bytes) -> dict:
    image = Image.open(io.BytesIO(file_contents))
    
    image = image.convert('RGB')
    image = image.resize((200,200))
    img_array = np.array(image)
    img_array = img_array / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Make prediction
    prediction = model.predict(img_array)
    predicted_class = int(prediction[0][0] > 0.5)  # 0 = human, 1 = nonhuman
    confidence = float(prediction[0][0])

    return {
        "prediction": predicted_class,
        "label": "nonhuman" if predicted_class == 1 else "human",
        "confidence": confidence,
        "is_human": predicted_class == 0
    }