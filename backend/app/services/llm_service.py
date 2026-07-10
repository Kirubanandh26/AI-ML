from google import genai
from app.core.config import settings


class LLMService:

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    @staticmethod
    def generate_response(
        prompt: str) -> str:

        response = LLMService.client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )

        return response.text