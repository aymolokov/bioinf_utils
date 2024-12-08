from scripts.dna_rna_tools import is_dna, is_rna
from scripts.dna_rna_tools import transcribe, complement, reverse
from scripts.dna_rna_tools import reverse_complement, reverse_transcribe
from scripts.filter_fastq import filter_fastq_seq, convert_bounds
from scripts.filter_fastq import read_fastq_seq, write_fastq_seq
from typing import Union


def run_dna_rna_tools(*args: list[str]) -> list[str]:
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


def filter_fastq(input_fastq: str, output_fastq: str,
                 gc_bounds: Union[list[float, float], float] = [0, 100],
                 length_bounds: Union[list[int, int], int] = [0, 2**32],
                 quality_threshold: float = 0) -> None:
    """
    Filters a fastq file based on GC content,
    sequence length, and average quality.

    Parameters:
    input_fastq: The input fastq file.
    output_fastq: The output fastq file.
    gc_bounds: A two-elements list representing the
                inclusive lower and upper bounds for GC content percentage.
                If a single float is provided, it is considered as the upper
                bound with a default lower bound of 0. Default is [0, 100].
    length_bounds: A two-elements list representing
                 the inclusive lower and upper bounds for sequence length.
                 If a single integer is provided, it is considered as the upper
                 bound with a default lower bound of 0. Default is [0, 2**32].
    quality_threshold: The minimum average quality threshold
                 for sequences to be retained. Default is 0 (phred33 scale).
    """
    gc_bounds = convert_bounds(gc_bounds)
    length_bounds = convert_bounds(length_bounds)
    input_fastq_file = open(input_fastq, "r")
    output_fastq_file = open(output_fastq, "w")
    try:
        entry = 1
        seq_data = read_fastq_seq(input_fastq_file)
        while seq_data:
            if filter_fastq_seq(seq_data, gc_bounds, length_bounds,
                                quality_threshold):
                write_fastq_seq(output_fastq_file, seq_data)
            entry += 1
            seq_data = read_fastq_seq(input_fastq_file)
    except (ValueError, SystemError) as e:
        print(f"Error {e} in entry {entry}.")
    input_fastq_file.close()
    output_fastq_file.close()
