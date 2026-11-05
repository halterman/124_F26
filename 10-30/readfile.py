f = open("mary.txt", "r")
content = f.read()
content = content.upper()
print(content)
words = content.split()
print(words)
# for line in f:
#     print('>' + line.strip() + '<')
f.close()