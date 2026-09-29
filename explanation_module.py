import os
import time
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def explain_topic(topic: str):

    prompt = f"""
Explain the topic "{topic}" in very simple language for a college student.

Include:

1. Definition
2. Main points
3. How it works
4. Simple example
5. Short summary

Rules:
- Use simple English.
- Keep the explanation clear.
- Avoid unnecessary complicated terms.
"""

    for attempt in range(5):

        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            error_message = str(e)

            print(
                f"EXPLAIN GEMINI ERROR - Attempt {attempt + 1}:",
                error_message
            )

            if "503" in error_message or "UNAVAILABLE" in error_message:

                if attempt < 4:
                    wait_time = (attempt + 1) * 5

                    print(
                        f"Gemini is busy. Retrying after {wait_time} seconds..."
                    )

                    time.sleep(wait_time)
                    continue

                return "Gemini is temporarily busy. Please try again later."

            return "Unable to explain the topic right now."

    return "Unable to explain the topic right now."