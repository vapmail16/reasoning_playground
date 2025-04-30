✅ Summary of Errors & Fixes

# | Error Message (Short) | 📍 Source File | 💥 Root Cause | ✅ Resolution
1 | The current project could not be installed | poetry install | Poetry expected a package layout | Added package-mode = false to pyproject.toml
2 | poetry shell not working | CLI / Poetry | Poetry 2.0 removed shell plugin by default | Use poetry run or run poetry self add poetry-plugin-shell
3 | openai.ChatCompletion is no longer supported | gpt_interface.py | You’re using OpenAI SDK ≥ 1.0 with old API syntax | Switched to new OpenAI() client interface (client.chat.completions.create)
4 | Wrong GPT response (e.g., irrelevant “neuroplasticity” answer) | app.py, prompts | Prompt template was likely missing, weak, or not inserted | Fixed prompt loading logic; strengthened template wording
5 | Only 3 reasoning types show in dropdown | app.py | Reasoning list hardcoded instead of reading all prompt files | Replaced static list with dynamic list from prompts/ folder
6 | .env not found or OPENAI_API_KEY not loaded | gpt_interface.py | .env file missing or not loaded | Added load_dotenv() and created .env.example template
7 | Streamlit shows no prompt context before sending to GPT | app.py | Prompt not visible, making debugging difficult | Added st.code(prompt) before calling ask_gpt()