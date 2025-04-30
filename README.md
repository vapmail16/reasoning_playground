# 🧠 Reasoning Playground

An interactive Streamlit app that helps users explore how GPT-based AI handles different types of reasoning — from deduction and probability to planning and ethics.

## 🚀 Features

- ✅ 17 Reasoning Types (Deductive, Inductive, Abductive, etc.)
- ✅ Auto-detect reasoning type from question
- ✅ Compare responses across multiple reasoning styles
- ✅ Step-by-step reasoning breakdowns and diagrams
- ✅ Easy-to-use Streamlit UI
- ✅ JSON/CSV export-ready structure

---

## 📚 Supported Reasoning Categories

1. Deductive  
2. Inductive  
3. Abductive  
4. Causal  
5. Counterfactual  
6. Temporal  
7. Multi-Hop  
8. Analogical  
9. Probabilistic  
10. Commonsense  
11. Scientific/Mathematical  
12. Spatial  
13. Planning & Decision-Making  
14. Ethical & Moral  
15. Legal & Policy  
16. Multi-Agent  
17. Metacognitive

---

## 🖥️ Getting Started

### 🔧 Requirements

- Python 3.10+
- Poetry (dependency management)
- OpenAI API Key

### 📦 Setup

```bash
# Clone the repo
git clone https://github.com/vapmail16/reasoning_playground.git
cd reasoning_playground

# Install dependencies
poetry install

# Create a .env file
cp .env.example .env
# Then add your OpenAI key inside it:
# OPENAI_API_KEY=your-key-here

# Run the app
poetry run streamlit run app.py
🧪 Sample Test Case
Question: "All cats are mammals. Felix is a cat. Is Felix a mammal?"
Reasoning Type: Deductive
GPT Output: "Yes, because if all cats are mammals and Felix is a cat, then Felix must be a mammal."
✅ Correct logic chain.

📂 Project Structure
bash
Copy
Edit
.
├── app.py                     # Streamlit interface
├── prompts/                  # One prompt template per reasoning type
├── utils/
│   ├── gpt_interface.py      # OpenAI API logic
│   ├── reasoning_mapper.py   # Prompt loading
│   └── reasoning_classifier.py # Auto-detect logic
├── diagnostics/
│   └── diagnostic.py         # Setup checks
├── tests/
│   └── Reasoning_Test_Cases.csv # Evaluation data
├── .env.example
├── Makefile
├── .gitignore
└── README.md
🤖 Powered By
OpenAI GPT-4

Streamlit

Poetry

📜 License
MIT License.
© 2024 Vikkas Arun Pareek

✨ Future Plans
Visual diagrams (Graphviz or Mermaid.js)

Feedback loop to improve prompts

Scoring engine for reasoning quality

Export sessions as JSON/CSV

