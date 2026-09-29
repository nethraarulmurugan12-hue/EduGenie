import os
import time
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_learning_recommendations(topic: str):

    prompt = f"""
Create a simple and useful step-by-step learning path for the topic: {topic}

The learner is a college student and a beginner.

Include:

1. Beginner Concepts
2. Important Topics
3. Practice Activities
4. Mini Project Idea
5. Next-Level Topics

Rules:
- Arrange topics in a logical learning order.
- Use simple and clear language.
- Give practical recommendations.
- Keep the learning path easy to follow.
- Create useful suggestions related to the given topic.
"""

    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            error_message = str(e)

            print("LEARNING PATH GEMINI ERROR:", error_message)

            if "503" in error_message or "UNAVAILABLE" in error_message:

                if attempt < 2:
                    print("Gemini is busy. Retrying...")
                    time.sleep(3)
                    continue

                return "Gemini is temporarily busy. Please try again after a few moments."

            return "Unable to generate learning recommendations right now."

    return "Unable to generate learning recommendations right now."