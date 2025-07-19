def read_code_file(uploaded_file) -> str:
    return uploaded_file.read().decode("utf-8")
