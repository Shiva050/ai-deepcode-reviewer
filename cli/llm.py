import subprocess

def query_llm(promt: str) -> str:
    try:
        result = subprocess.run(
            ["ollama","run","codellama"],
            input =  promt,
            text = True,
            capture_output = True
        )

        return result.stdout.strip()
    
    except Exception as e:
        return f"Error calling Ollama: {e}"