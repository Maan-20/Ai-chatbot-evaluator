import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="AI Evaluation Playground", layout="wide")

st.title("🤖 AI Chatbot Evaluation Playground")

def get_responses(prompt):
    return {
        "ChatGPT": f"Answer to '{prompt}' with structured reasoning.",
        "Gemini": f"A concise explanation about '{prompt}'.",
        "Claude": f"A detailed and safe response regarding '{prompt}'."
    }

def evaluate(response):
    return {
        "accuracy": random.randint(3, 5),
        "tone": random.randint(2, 5),
        "bias": random.randint(3, 5),
        "reasoning": random.randint(2, 5),
    }

prompt = st.text_input("💬 Enter your prompt")

if prompt:
    responses = get_responses(prompt)
    results = []

    st.subheader("📊 Model Responses & Evaluation")

    cols = st.columns(len(responses))

    for i, (model, response) in enumerate(responses.items()):
        scores = evaluate(response)
        total = sum(scores.values()) / 4
        results.append((model, total))

        with cols[i]:
            st.markdown(f"### {model}")
            st.write(response)
            st.write("**Scores:**")
            st.write(scores)
            st.metric("Overall Score", round(total, 2))

    best_model = max(results, key=lambda x: x[1])
    st.success(f"🏆 Best Performing Model: {best_model[0]}")

    df = pd.DataFrame(results, columns=["Model", "Score"])
    st.subheader("📈 Performance Comparison")
    st.bar_chart(df.set_index("Model"))
