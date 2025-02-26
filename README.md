# HelpmateProject

## Overview
HelpmateProject is a Python-based project in the insurance domain, designed to build a robust generative search system capable of effectively and accurately answering questions from a policy document. Leveraging advanced libraries such as LangChain, OpenAI, and ChromaDB, this project aims to provide a sophisticated retrieval augmented generation system. The system is structured to retrieve the top 3 relevant chunks from the search layer and generate precise answers using a language model in the generation layer. The project setup includes a virtual environment to manage dependencies efficiently.

## Project Structure

## Requirements
The project dependencies are listed in the `requirements.txt` file:

## Setup
1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd HelpmateProject
    ```

2. **Create and activate the virtual environment:**
    ```sh
    python -m venv langchain_env
    source langchain_env/Scripts/activate  # On Windows
    # source langchain_env/bin/activate    # On Unix or MacOS
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the root directory and add your environment variables.

## Usage
Run the main script:
```sh
python Helpmate.py
```
