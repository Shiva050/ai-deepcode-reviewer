from app.reviewer import review_code

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
            if not content.strip():
                raise ValueError("The file is empty.")
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ File not found: {path}")
    except UnicodeDecodeError:
        raise UnicodeDecodeError("❌ Could not decode the file. Please ensure it's UTF-8 or plain text.")
    except Exception as e:
        raise RuntimeError(f"❌ Error reading file: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_python_file>")
        sys.exit(1)

    path = sys.argv[1]

    try:
        code = read_file(path)
        print("\nSending code to AI Reviewer...")
        review = review_code(code)
        print("\n📋 AI Review:\n")
        print(review)
        sys.exit(0)

    except Exception e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()