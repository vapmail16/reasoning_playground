# Run the Streamlit app
run:
	poetry run streamlit run app.py

# Format code using black
format:
	poetry run black .

# Run basic diagnostics
diagnose:
	poetry run python diagnostics/diagnostic.py

# Export requirements.txt (for Streamlit Cloud)
export-reqs:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

# Install dependencies from pyproject.toml
install:
	poetry install
