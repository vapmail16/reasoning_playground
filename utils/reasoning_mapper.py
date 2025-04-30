
# utils/reasoning_mapper.py

from pathlib import Path

def get_prompt(reasoning_type: str, question: str) -> str:
    path = Path("prompts") / f"{reasoning_type.capitalize()}.txt"
    if not path.exists():
        return f"You are a reasoning assistant.\n\nQuestion: {question}\nAnswer:"
    template = path.read_text()
    return template.replace("{{question}}", question)

