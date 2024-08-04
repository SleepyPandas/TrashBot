import os
import google.generativeai as genai

#TODO: Ensure the API key is set in the environment variables
class GeminiAPI:
    def __init__(self):
        genai.configure(api_key=os.environ['API_KEY'])

    def classify_image(self):
        # Upload the file and print a confirmation.
        sample_file = genai.upload_file(path="/Users/Matt/Documents/GitHub/TerraHacks/throw_away_item.png",
                                        display_name="Test")

        print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

        file = genai.get_file(name=sample_file.name)
        print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")

        # Choose a Gemini model.
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")

        # Prompt the model with text and the previously uploaded image.
        response = model.generate_content([sample_file, "Would this item belong in the recycle, garbage, or compost."])

        print(response.text)


pass
