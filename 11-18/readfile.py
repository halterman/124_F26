import string

with open('mary.txt', 'r') as f:
    content = f.read()
print(f'[{content}]')

print('----------------')

punct = string.punctuation.replace('\'', '').replace('-', '')
with open('mary.txt', 'r') as f:
    for line in f:
        line = line.strip()
        line = ''.join(ch for ch in line if ch not in punct)
        line = line.upper()
        print(f'[{line}]')

