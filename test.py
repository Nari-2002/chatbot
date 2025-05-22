from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

print("Available Gemini Models and their supported methods:")
for m in genai.list_models():
    # Only list models that support generating content (i.e., chat or text generation)
    if "generateContent" in m.supported_generation_methods:
        print(f"Model Name: {m.name}")
        print(f"  Description: {m.description}")
        print(f"  Input Token Limit: {m.input_token_limit}")
        print(f"  Output Token Limit: {m.output_token_limit}")
        print(f"  Supported Methods: {m.supported_generation_methods}\n")