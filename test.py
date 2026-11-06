from generator import generate_questions


def test_question_generation():

    result = generate_questions(
        role="Software Developer",
        experience="Fresher",
        domain="Python",
        difficulty="Medium",
        number=10
    )

    print("\nAI GENERATED INTERVIEW QUESTIONS")
    print("--------------------------------")
    print(result)

    assert result.strip(), "AI response is empty"

    print("\nTest passed successfully!")


if __name__ == "__main__":
    test_question_generation()