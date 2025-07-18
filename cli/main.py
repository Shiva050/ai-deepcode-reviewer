from llm import query_llm

def read_file(path):
    with open(path) as f:
        return f.read()

def main():
    path = input("Enter code file path: ")
    code = read_file(path)

    print("Sending code to AI Reviewer...")
    promt = f"Please review the following Python code and suggest improvements:\n\n{code}"
    review = query_llm(promt)

    print("AI review: \n", review)

if __name__ == "__main__":
    main()