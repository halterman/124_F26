import string

counts: dict[str, int] = {}

with open('mary.txt', 'r') as f:
    for line in f:
        line = line.strip().upper()
        for ch in line:
            if ch in string.ascii_uppercase:
                if ch in counts:
                    counts[ch] += 1
                else:
                    counts[ch] = 1
    for ch, count in sorted(counts.items()):
        print(f'{ch}: {count}')
