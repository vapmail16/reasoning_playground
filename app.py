from pathlib import Path
import streamlit as st
from utils.gpt_interface import ask_gpt
from utils.reasoning_mapper import get_prompt
from utils.reasoning_classifier import classify_reasoning_type

# Dynamically load available reasoning types from /prompts
prompt_files = sorted(Path("prompts").glob("*.txt"))
available_types = [f.stem for f in prompt_files]

# App UI
st.set_page_config(page_title="Reasoning Playground", layout="centered")
st.title("🧠 Reasoning Playground")

st.markdown("Explore how GPT answers a question based on different reasoning types.")

# Input Section
question = st.text_area("Enter your question")

# Auto-detect checkbox
auto_detect = st.checkbox("Auto-detect reasoning type")

# Optional: classify reasoning type using GPT
if auto_detect and question.strip():
    with st.spinner("Detecting reasoning type..."):
        detected_type = classify_reasoning_type(question)
        st.success(f"Auto-detected: {detected_type}")
else:
    detected_type = None

# Compare mode toggle
compare_mode = st.checkbox("Compare across multiple reasoning types")

# Show diagram toggle
show_diagram = st.checkbox("Show explanation as diagram")

# Choose reasoning type(s)
if compare_mode:
    selected_types = st.multiselect(
        "Select reasoning types to compare",
        available_types,
        default=["Deductive", "Inductive"]
    )
else:
    reasoning_type = st.selectbox(
        "Choose Reasoning Type",
        available_types,
        index=available_types.index(detected_type) if detected_type in available_types else 0
    )
    selected_types = [reasoning_type]

# Submit and get responses
if st.button("Submit") and question.strip():
    for rtype in selected_types:
        st.markdown(f"### 🧠 Reasoning Type: **{rtype}**")
        prompt = get_prompt(rtype, question)
        
        # Enhance prompt if diagram is requested
        if show_diagram:
            prompt += "\n\nPlease explain your reasoning in 3-5 clear steps."
        
        st.code(prompt, language="markdown")
        
        with st.spinner(f"Thinking using {rtype} reasoning..."):
            response = ask_gpt(prompt)
        
        st.subheader("Response:")
        st.write(response)
        
        if show_diagram:
            st.markdown("**🧩 Reasoning Steps:**")
            steps = [line for line in response.split("\n") if line.strip().startswith(("-", "1.", "•"))]
            if not steps:
                st.info("No structured steps found.")
            else:
                for step in steps:
                    st.markdown(f"- {step.strip('-• ').strip()}")
        
        st.markdown("---")
