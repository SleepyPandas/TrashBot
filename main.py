
import os
import google.generativeai as genai

genai.configure(api_key=os.environ['API_KEY'])

# Upload the file and print a confirmation.
sample_file = genai.upload_file(path="jetpack.jpg",
                            display_name="Jetpack drawing")

print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

file = genai.get_file(name=sample_file.name)
print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Prompt the model with text and the previously uploaded image.
response = model.generate_content([sample_file, "If this picture was a real item, would this product belong in the recycle, garbage, or compost."])

print(response.text)
print("wrhfwhifrf")