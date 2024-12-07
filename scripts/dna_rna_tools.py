def is_dna(seq):
    """
    Checks if a sequence is DNA.

    Parameters
    ----------
    seq : str
        The sequence to check.

    Returns
    -------
    bool
        True if the sequence is DNA, False otherwise.
    """
    for base in seq:
        if base.upper() == "U":
            return False
    return True


def is_rna(seq):
    """
    Checks if a sequence is RNA.

    Parameters
    ----------
    seq : str
        The sequence to check.

    Returns
    -------
    bool
        True if the sequence is RNA, False if it is not.
    """

    for base in seq:
        if base.upper() == "T":
            return False
    return True


def transcribe(seq):
    """
    Converts a DNA sequence to an RNA sequence by replacing
    thymine (T) with uracil (U).

    Parameters
    ----------
    seq : str
        The DNA sequence to transcribe.

    Returns
    -------
    str
        The RNA sequence corresponding to the given DNA sequence.
    """
    if not is_dna(seq):
        raise ValueError("Attempt to transcribe RNA!")
    return seq.replace("t", "u").replace("T", "U")


def reverse_transcribe(seq):
    """
    Converts an RNA sequence to a DNA sequence by replacing
    uracil (U) with thymine (T).

    Parameters
    ----------
    seq : str
        The RNA sequence to be converted to DNA.

    Returns
    -------
    str
        The DNA sequence resulting from the conversion of uracil to thymine,
        preserving the case.
    """
    if not is_rna(seq):
        raise ValueError("Attempt to transcribe DNA!")
    return seq.replace("u", "t").replace("U", "T")


def reverse(seq):
    """
    Reverses a DNA or RNA sequence.

    Parameters
    ----------
    seq : str
        The sequence to reverse.

    Returns
    -------
    str
        The reversed sequence.
    """
    if is_dna(seq) or is_rna(seq):
        result = seq[::-1]
    return result


def complement(seq):
    """
    Computes the complement of a DNA or RNA sequence.

    Parameters
    ----------
    seq : str
        The DNA or RNA sequence to compute the complement for.

    Returns
    -------
    str
        The complement of the given sequence.
    """
    if is_dna(seq) or is_rna(seq):
            complement_str = str.maketrans('AUGCaugc', 'UACGuacg')
    return seq.translate(complement_str)


def reverse_complement(seq):
    """
    Computes the reverse complement of a DNA or RNA sequence.

    Parameters
    ----------
    seq : str
        The DNA or RNA sequence to compute the reverse complement for.

    Returns
    -------
    str
        The reverse complement of the input sequence, preserving the case.
    """
    return reverse(complement(seq))
