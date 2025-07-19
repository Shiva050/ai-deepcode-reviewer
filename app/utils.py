def read_code_file(uploaded_file) -> str:
    raw_bytes = uploaded_file.read()
    for encoding in ("utf-8", "latin-1", "windows-1252"):
        try:
            decoded = raw_bytes.decode(encoding)
            if "\x00" in decoded:
                return "[Error] File appears to be binary, not text."
            return decoded
        except UnicodeDecodeError:
            continue
    return "[Error] Unable to decode file with common encodings."
