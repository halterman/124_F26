import string

counts = [0] * 26

with open('mary.txt', 'r') as f:
    for line in f:
        line = line.strip().upper()
        for ch in line:
            if ch in string.ascii_uppercase:
                counts[ord(ch) - 65] += 1
    for i in range(len(counts)):
        print(f'{chr(i + 65)}: {counts[i]}')

