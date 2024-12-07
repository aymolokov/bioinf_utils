def avg_quality(seq_quality):
    """
    Calculate the average quality score of the given sequence quality.

    Parameters
    ----------
    seq_quality : str
        The sequence quality to calculate the average score for.

    Returns
    -------
    float
        The average quality score of the sequence quality.
    """
    return sum(ord(base) - 33 for base in seq_quality) / len(seq_quality)


def gc_percent(seq):
    """
    Calculate the GC content of the given sequence.

    Parameters
    ----------
    seq : str
        The sequence to calculate the GC content for.

    Returns
    -------
    float
        The GC content of the sequence as a percentage.
    """
    return (seq.count("G") + seq.count("C")) / len(seq) * 100


def convert_bounds(bounds):
    """
    Convert bounds to a valid range.
    If only one bound is passed, convert it to [0, bounds].

    Parameters
    ----------
    bounds : int, float, list
        The bounds to convert.

    Returns
    -------
    list
        The converted bounds.
    """
    if isinstance(bounds, int) or isinstance(bounds, float):
        return [0, bounds]
    else:
        return bounds


def filter_fastq_seq(seq_data, gc_bounds, length_bounds, quality_threshold):
    """
    Returns True if the given seq_data satisfies the following conditions:

    1. The length of the sequence is within the given bounds.
    2. The GC content of the sequence is within the given bounds.
    3. The average quality score of the sequence is above the given threshold.

    Otherwise returns False.
    """
    if not (length_bounds[0] <= len(seq_data[0]) <= length_bounds[1]):
        return False
    if not (gc_bounds[0] <= gc_percent(seq_data[0]) <= gc_bounds[1]):
        return False
    if avg_quality(seq_data[1]) < quality_threshold:
        return False
    return True
