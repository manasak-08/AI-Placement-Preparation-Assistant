import os
from dotenv import load_dotenv

from langchain_openrouter import ChatOpenRouter
from langchain_core.output_parsers import StrOutputParser

from prompts import INTERVIEW_PROMPT
from schemas import InterviewConfig

load_dotenv(override=True)


def get_llm():

    api_key = os.getenv("OPENROUTER_API_KEY")
    model_name = os.getenv("MODEL_NAME", "openai/gpt-4o-mini")

    if not api_key:
        raise ValueError("OpenRouter API key is missing in .env")

    return ChatOpenRouter(
        model=model_name,
        api_key=api_key,
        temperature=0.3
    )


def generate_questions(role, experience, domain, difficulty, number):

    config = InterviewConfig(
        role=role,
        experience=experience,
        domain=domain,
        difficulty=difficulty,
        number=number
    )

    llm = get_llm()

    chain = INTERVIEW_PROMPT | llm | StrOutputParser()

    result = chain.invoke({
        "role": config.role,
        "experience": config.experience,
        "domain": config.domain,
        "difficulty": config.difficulty,
        "number": config.number
    })

    return result