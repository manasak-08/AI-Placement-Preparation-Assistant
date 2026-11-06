
import streamlit as st
from generator import generate_questions

st.set_page_config(
    page_title="AI Placement Preparation Assistant",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Placement Preparation Assistant")

st.write(
    "Prepare for your dream job with personalized "
    "AI-generated interview questions."
)

st.divider()

st.subheader("Interview Configuration")

role = st.text_input(
    "Role",
    value="Software Developer"
)

experience = st.selectbox(
    "Experience",
    ["Fresher", "0-2 Years", "2-5 Years", "5+ Years"]
)

domain = st.text_input(
    "Domain",
    value="Python"
)

difficulty = st.selectbox(
    "Level of Questions",
    ["Easy", "Medium", "Hard"],
    index=1
)

number = st.selectbox(
    "Number of Questions",
    [5, 10, 15, 20],
    index=1
)

if st.button("Generate Interview Questions"):

    if not role.strip() or not domain.strip():
        st.warning("Please enter Role and Domain.")

    else:
        try:
            with st.spinner("AI is generating questions..."):

                questions = generate_questions(
                    role,
                    experience,
                    domain,
                    difficulty,
                    number
                )

            st.success("Questions generated successfully!")

            st.subheader("Your Interview Questions")

            st.markdown(questions)

        except Exception as e:
            st.error(f"Error: {e}")
