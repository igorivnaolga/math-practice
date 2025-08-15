# Перетворення символів в ASCII-коди
text = "Hello"
ascii_codes = [ord(char) for char in text]
print("ASCII Codes:", ascii_codes)


# Перетворення ASCII-кодів в символи
decoded_text = "".join([chr(code) for code in ascii_codes])
print("Decoded Text:", decoded_text)
