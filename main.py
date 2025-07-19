from app.reviewer import review_code

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    path = input("Enter the path to your Python file: ")
    try:
        code = read_file(path)
        print("\nSending code to AI Reviewer...")
        review = review_code(code)
        print("\n📋 AI Review:\n")
        print(review)
    except FileNotFoundError:
        print("❌ File not found. Please check the path and try again.")

if __name__ == "__main__":
    main()