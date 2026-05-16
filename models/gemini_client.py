import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE

genai.configure(api_key=GEMINI_API_KEY)

def call_gemini(prompt, image_path=None):
    try:
        model = genai.GenerativeModel(MODEL_NAME)

        if image_path:
            with open(image_path, "rb") as img:
                response = model.generate_content(
                    [
                        prompt,
                        {
                            "mime_type": "image/jpeg",
                            "data": img.read()
                        }
                    ],
                    generation_config={
                        "temperature": TEMPERATURE
                    }
                )
        else:
            response = model.generate_content(
                prompt,
                generation_config={
                    "temperature": TEMPERATURE
                }
            )

        return response.text

    except Exception as e:
        return f"Erreur Gemini: {str(e)}"