# Computing GC Content


def read_lines(file):
    with open(file, 'r') as f:
        return [lines.strip() for lines in f.readlines()]


def gc(seq):
    return round(((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)


file_lines = read_lines('rosalind_gc.txt')

sequence = {}
location = ''

for line in file_lines:
    if line[0] == '>':
        location = line.strip('>')
        sequence[location] = ''

    else:
        sequence[location] += line

for item in sequence:
    sequence[item] = gc(sequence[item])

result = max(sequence, key=sequence.get)

print(
    f'{result}\n{sequence[result]}'
)








