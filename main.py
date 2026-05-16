from agent.controller import run_agent

def main():

    print("=== AGENT IA MULTIMODAL SANTÉ (Gemini) ===\n")

    image_path = "examples/sample.jpg"

    user_text = input("Décris tes symptômes :\n> ")

    result = run_agent(user_text, image_path)

    print("\n===== RESULTAT =====\n")
    print(result)


if __name__ == "__main__":
    main()