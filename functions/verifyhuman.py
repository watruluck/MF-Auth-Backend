from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import io
import os

model_path = os.path.join(os.path.dirname(__file__), '../models/150_epoch_facial_model.keras')
model = load_model(model_path)

async def verify_human(file_contents: bytes) -> dict:
    photo = image.load_img(io.BytesIO(file_contents), target_size=(200, 200))
    photo = image.img_to_array(photo)

    photo = np.expand_dims(photo, axis=0)
    photo = photo/255

    prediction = model.predict(photo)


    # return value of model is number from 0-1, 0 being human and 1 nonhuman.
    predicted_class = int(prediction[0][0] > 0.5)

    return {
        "prediction": predicted_class,
        "result": "nonhuman" if predicted_class == 1 else "human"
    }