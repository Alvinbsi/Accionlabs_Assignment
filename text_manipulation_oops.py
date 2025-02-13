import re
def text_manipulation(text):
    pattern = r'\b [A-Za-z0-9.%+-] + @[A-Za-z0-9.-] +/.[A-Z|a-z]{2,} \b'
    return sorted(set(re.findall(pattern, text)))

text = "Contact us alvin@example.com and user@alvin.com"
print(text_manipulation(text))
