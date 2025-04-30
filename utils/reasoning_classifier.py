from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

REASONING_TYPES = [
    "Deductive", "Inductive", "Abductive", "Causal", "Counterfactual", "Temporal",
    "Multi-Hop", "Analogical", "Probabilistic", "Commonsense", "Scientific",
    "Spatial", "Planning", "Ethical", "Legal", "Multi-Agent", "Metacognitive"
]

def classify_reasoning_type(question: str) -> str:
    prompt = f"""
You are a reasoning type classifier.

Given the question below, respond with ONLY the most appropriate reasoning type from this list:

{", ".join(REASONING_TYPES)}

Question: "{question}"

Reasoning Type:
"""
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4"),
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        reasoning = response.choices[0].message.content.strip()
        if reasoning in REASONING_TYPES:
            return reasoning
        return "Unknown"
    except Exception as e:
        return f"Error: {e}"
