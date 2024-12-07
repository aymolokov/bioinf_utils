from scripts.dna_rna_tools import is_dna, is_rna
from scripts.dna_rna_tools import transcribe, complement, reverse
from scripts.dna_rna_tools import reverse_complement, reverse_transcribe
from scripts.filter_fastq import filter_fastq_seq, convert_bounds


def run_dna_rna_tools(*args):
    """
    Processes a list of DNA/RNA sequences based on the specified procedure.

    Parameters:
    *args: A variable length argument list where all arguments except
           the last one are DNA/RNA sequences to be processed, and
           the last argument is a string representing the procedure
           to be applied. Valid procedures are:
           - "transcribe": Transcribes DNA to RNA.
           - "reverse": Reverses the sequence.
           - "complement": Computes the complement of the sequence.
           - "reverse_complement": Computes the reverse complement
             of the sequence.
           - "reverse_transcribe": Converts RNA to DNA.
           - "type": Determines if the sequence is DNA or RNA.
           - "to_upper": Converts the sequence to uppercase.

    Returns:
    list or str: A list of processed sequences or a single processed sequence
                 if only one sequence is provided. Returns error messages if
                 invalid sequences or procedures are specified.
    """
    *seqs, proc = args
    res = []
    for seq in seqs:
        if not (is_dna(seq) or is_rna(seq)):
            res.append("Is not valid sequence")
        elif proc == "transcribe":
            res.append(transcribe(seq))
        elif proc == "reverse":
            res.append(reverse(seq))
        elif proc == "complement":
            res.append(complement(seq))
        elif proc == "reverse_complement":
            res.append(reverse_complement(seq))
        elif proc == "reverse_transcribe":
            res.append(reverse_transcribe(seq))
        elif proc == "type":
            res.append("DNA" if is_dna(seq) else "RNA")
        elif proc == "to_upper":
            res.append(seq.upper())
        else:
            res.append("Is not valid procedure")
    if len(res) == 1:
        return res[0]
    else:
        return res


def filter_fastq(seqs, gc_bounds=[0, 100],
                 length_bounds=[0, 2**32], quality_threshold=0):
    """
    Filters a dictionary of FASTQ sequences based on GC content,
    sequence length, and average quality.

    Parameters:
    seqs (dict): A dictionary where keys are sequence identifiers and values
                 are tuples containing the sequence and its quality string.
    gc_bounds (list or float, optional): A two-elements list representing the
                 inclusive lower and upper bounds for GC content percentage.
                 If a single float is provided, it is considered as the upper
                 bound with a default lower bound of 0. Default is [0, 100].
    length_bounds (list or int, optional): A two-elements list representing
                 the inclusive lower and upper bounds for sequence length.
                 If a single integer is provided, it is considered as the upper
                 bound with a default lower bound of 0. Default is [0, 2**32].
    quality_threshold (int, optional): The minimum average quality threshold
                 for sequences to be retained. Default is 0 (phred33 scale).

    Returns:
    dict: A dictionary containing only the sequences that meet all filtering
          criteria, with the same structure as the input dictionary.
    """
    gc_bounds = convert_bounds(gc_bounds)
    length_bounds = convert_bounds(length_bounds)
    filtered = {}
    for name, seq in seqs.items():
        if filter_fastq_seq(seq, gc_bounds, length_bounds, quality_threshold):
            filtered[name] = seq
    return filtered
