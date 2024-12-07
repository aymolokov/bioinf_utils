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
    return seq[::-1]


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
    comp_seq = ""
    a_comp = "T" if is_dna(seq) else "U"
    for base in seq:
        comp_base = base.upper()
        if comp_base == "C":
            comp_base = "G"
        elif comp_base == "G":
            comp_base = "C"
        elif comp_base == "T":
            comp_base = "A"
        elif comp_base == "U":
            comp_base = "A"
        elif comp_base == "A":
            comp_base = a_comp
        if (base.islower()):
            comp_base = comp_base.lower()
        comp_seq += comp_base
    return comp_seq


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
