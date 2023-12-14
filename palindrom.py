palindrom = input("Adjon meg egy palindrómot: ")

text1 = palindrom.lower().replace(" ", "").replace("!", "").replace(",", "").replace(".", "").replace(".", "").replace("-", "").replace("?", "").replace("–", "").replace("ö", "o").replace("ó", "o").replace("ő", "o").replace("ü", "u").replace("ű", "u").replace("ú", "u").replace("é", "e").replace("á", "a").replace("í", "i")

text2 = text1[::-1]

print(text2)
if text1 == text2:
    print(f"A(z) \'{palindrom}\' kifejezés palindrom!")
else:
    print(f"A(z) \'{palindrom}\' kifejezés nem palindrom!")