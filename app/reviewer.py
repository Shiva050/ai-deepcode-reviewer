from app.llm import query_llm

def generate_review_prompt(code: str) -> str:
    return f"""You are a senior software engineer. Review the following Python code for:
- Code quality
- Security issues
- Best practices
- Optimization suggestions

Provide actionable feedback with line references if applicable.

Code:
{code}
"""

def review_code(code: str) -> str:
    prompt = generate_review_prompt(code)
    return query_llm(prompt)
