from agent.prompt_builder import build_prompt
from models.gemini_client import call_gemini
from utils.safety import apply_safety_rules
from utils.image_loader import validate_image

def run_agent(user_text, image_path):

    try:
        image_path = validate_image(image_path)

        prompt = build_prompt(user_text)

        raw_response = call_gemini(prompt, image_path)

        final_response = apply_safety_rules(raw_response)

        return final_response

    except Exception as e:
        return f"Erreur agent: {str(e)}"