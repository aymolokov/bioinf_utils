def is_dna(seq: str) -> bool:
    """
    Checks if a sequence is DNA.
    """
    for base in seq:
        if base.upper() == "U":
            return False
    return True


def is_rna(seq: str) -> bool:
    """
    Checks if a sequence is RNA.
    """

    for base in seq:
        if base.upper() == "T":
            return False
    return True


def transcribe(seq: str) -> str:
    """
    Converts a DNA sequence to an RNA sequence by replacing
    thymine (T) with uracil (U).
    """
    if not is_dna(seq):
        raise ValueError("Attempt to transcribe RNA!")
    return seq.replace("t", "u").replace("T", "U")


def reverse_transcribe(seq: str) -> str:
    """
    Converts an RNA sequence to a DNA sequence by replacing
    uracil (U) with thymine (T).
    """
    if not is_rna(seq):
        raise ValueError("Attempt to transcribe DNA!")
    return seq.replace("u", "t").replace("U", "T")


def reverse(seq: str) -> str:
    """
    Reverses a DNA or RNA sequence.
    """
    if is_dna(seq) or is_rna(seq):
        result = seq[::-1]
    return result


def complement(seq: str) -> str:
    """
    Computes the complement of a DNA or RNA sequence.
    """
    if is_dna(seq) or is_rna(seq):
        complement_str = str.maketrans('AUGCaugc', 'UACGuacg')
    return seq.translate(complement_str)


def reverse_complement(seq: str) -> str:
    """
    Computes the reverse complement of a DNA or RNA sequence.
    """
    return reverse(complement(seq))
