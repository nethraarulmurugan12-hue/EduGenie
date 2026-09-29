import os
import time
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def answer_question(question: str):

    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=question
            )

            return response.text

        except Exception as e:

            error_message = str(e)

            print("QNA GEMINI ERROR:", error_message)

            if "503" in error_message or "UNAVAILABLE" in error_message:

                if attempt < 2:
                    print("Gemini is busy. Retrying...")
                    time.sleep(3)
                    continue

                return "Gemini is temporarily busy. Please try again after a few moments."

            return "Unable to get an answer from Gemini right now."

    return "Unable to get an answer from Gemini right now."