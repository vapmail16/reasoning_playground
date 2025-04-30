# diagnostics/diagnostic.py

import importlib
import os
from pathlib import Path

REQUIRED_MODULES = ["openai", "streamlit", "pandas", "dotenv"]

def check_modules():
    print("📦 Checking installed modules...")
    for mod in REQUIRED_MODULES:
        try:
            importlib.import_module(mod)
            print(f"✅ {mod} is installed.")
        except ImportError:
            print(f"❌ {mod} is missing!")

def check_prompt_files():
    print("\n📁 Checking prompt templates...")
    prompts = Path("prompts")
    if not prompts.exists():
        print("❌ 'prompts/' folder not found.")
        return
    expected = ["deductive.txt", "inductive.txt", "abductive.txt"]
    for file in expected:
        f = prompts / file
        if f.exists():
            print(f"✅ {file} exists.")
        else:
            print(f"❌ {file} missing.")

def check_env():
    print("\n🔐 Checking .env file...")
    if Path(".env").exists():
        print("✅ .env file exists.")
    else:
        print("⚠️  .env file missing (needed for API keys).")

if __name__ == "__main__":
    check_modules()
    check_prompt_files()
    check_env()
