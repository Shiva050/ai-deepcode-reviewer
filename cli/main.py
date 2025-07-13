def read_file(path):
    with open(path) as f:
        return f.read()

def main():
    path = input("Enter code file path: ")
    code = read_file(path)
    print("Your code:\n", code)

if __name__ == "__main__":
    main()