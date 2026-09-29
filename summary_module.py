import os
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def summarize_text(text: str):

    prompt = f"""
Summarize the following text in simple and clear language
for a college student.

Rules:
1. Include the main ideas.
2. Remove unnecessary details.
3. Keep important facts.
4. Use simple sentences.
5. Give the summary in short paragraphs or bullet points.

Text to summarize:

{text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("SUMMARY GEMINI ERROR:", e)
        return "Unable to summarize the text right now."