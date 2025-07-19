import subprocess

def query_llm(prompt: str, model="codellama") -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"[LLM Error]: {e}"
