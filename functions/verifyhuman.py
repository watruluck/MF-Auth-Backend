from keras.preprocessing import image
import numpy as np
import io

async def verify_human(file_contents: bytes, model) -> dict:
    """Verify if uploaded image contains a human face using CNN model"""
    # Load and preprocess image to 200x200
    photo = image.load_img(io.BytesIO(file_contents), target_size=(200, 200))
    photo = image.img_to_array(photo)

    # Reshape for model input and normalize pixel values to 0-1
    photo = np.expand_dims(photo, axis=0)
    photo = photo/255

    # Run prediction through trained CNN model
    prediction = model.predict(photo)

    # Model outputs 0-1: 0=human, 1=nonhuman. Threshold at 0.5
    predicted_class = int(prediction[0][0] > 0.5)

    return {
        "prediction": predicted_class,
        "result": "nonhuman" if predicted_class == 1 else "human"
    }