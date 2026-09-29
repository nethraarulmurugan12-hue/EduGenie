import os
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_quiz(topic: str):

    prompt = f"""
Create a 5-question multiple-choice quiz about {topic}
for college students.

Each question must have:
A) Option
B) Option
C) Option
D) Option

Only one answer should be correct.

At the end give:

Answer Key:
1. A
2. B
3. C
4. D
5. A
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print("QUIZ GEMINI ERROR:", e)

        # Local backup quiz if Gemini quota is unavailable
        return f"""
Quiz: {topic}

Question 1:
What is the main purpose of studying {topic}?

A) To understand its concepts
B) To avoid learning
C) To delete information
D) None of these

Question 2:
Which activity helps in learning {topic}?

A) Practice
B) Ignoring the topic
C) Avoiding examples
D) None of these

Question 3:
What is important when learning a new topic?

A) Understanding the basics
B) Skipping everything
C) Memorizing without understanding
D) Avoiding practice

Question 4:
Which method improves knowledge of {topic}?

A) Practice and revision
B) Never practicing
C) Ignoring mistakes
D) Avoiding questions

Question 5:
What is a useful way to improve in {topic}?

A) Practice with examples
B) Stop studying
C) Avoid the topic
D) Do nothing

Answer Key:
1. A
2. A
3. A
4. A
5. A
"""