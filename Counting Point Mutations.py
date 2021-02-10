# Counting Point Mutations

dna1 = 'ACTG'
dna2 = 'ACTG'

hamming_distance = 0

if len(dna1) == len(dna2):
    j = int(len(dna1))
    i = 0
    while True:
        if dna1[i] != dna2[i]:
            hamming_distance += 1

        i += 1

        if i == j:
            break

    print('\nHamming distance: ', hamming_distance)

else:
    print('\nThese strings need to be equal size!')