from collections import Counter

def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    bases = Counter([b for b in sequence])
    gc_content = ( bases["G"] + bases["C"] ) / len(sequence) * 100
    return round(gc_content, 2)