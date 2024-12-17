import pyperclip

filename = "result.txt"

with open(filename, 'r', encoding='utf-8') as file:
    file_contents = file.read()

pyperclip.copy(file_contents)