import google.generativeai as genai
from app.core.config import settings

class OpenAIService:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_quotes(self, category, mood, count):
        prompt = f"Generate {count} {mood} quotes about {category}"

        response = self.model.generate_content(prompt)

        return [response.text]