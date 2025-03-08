def get_hamming_distance(dna1, dna2):
    distance = 0
    for i in range(len(dna1)):  # Loop through each position in the strings
        if dna1[i] != dna2[i]:  # Compare the corresponding symbols
            distance += 1       # Increment the distance for mismatches
    return distance
def get_dna_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_complement = ''  # Initialize an empty string
    for symbol in dna[::-1]:  # Manually reverse the string
        reverse_complement += complement[symbol]  # Find the complement
    return reverse_complement
