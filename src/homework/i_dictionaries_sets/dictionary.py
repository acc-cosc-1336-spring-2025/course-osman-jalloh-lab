def get_p_distance(list1, list2):
    """Calculate p-distance between two lists."""
    mismatches = sum(1 for a, b in zip(list1, list2) if a != b)
    return mismatches / len(list1)

def get_p_distance_matrix(sequences):
    """Create a p-distance matrix for a collection of sequences."""
    n = len(sequences)
    p_distance_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            p_distance_matrix[i][j] = get_p_distance(sequences[i], sequences[j])
    return p_distance_matrix