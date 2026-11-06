
from langchain_core.prompts import ChatPromptTemplate


INTERVIEW_PROMPT = ChatPromptTemplate.from_template("""
You are an expert technical interviewer and placement trainer.

Generate exactly {number} interview questions.

Candidate Details:

Job Role: {role}
Experience: {experience}
Domain: {domain}
Difficulty Level: {difficulty}

Instructions:

1. Generate exactly the requested number of questions.
2. Focus on the selected technical domain.
3. Match questions to the candidate's experience.
4. Use simple and clear English.
5. Avoid duplicate questions.
6. Include practical and conceptual questions.
7. Number questions from 1 to {number}.
8. Do not generate answers.

Return only the interview questions.
""")
