from os import remove, rename
from scripts.filter_fastq import write_fastq_seq, read_fastq_seq


def convert_multiline_fasta_to_oneline(input_fastq: str,
                                       output_fastq: str = ""):
    """
    Converts a multiline FASTQ file to a single-line FASTQ file.

    If output_fastq is not specified, the file is overwritten.
    """
    no_output_fastq = (output_fastq == "")
    if no_output_fastq:
        output_fastq = input_fastq + ".tmp"
    input_fastq_file = open(input_fastq, "r")
    output_fastq_file = open(output_fastq, "w")
    try:
        entry = 1
        seq_data = read_fastq_seq(input_fastq_file, True)
        while seq_data:
            write_fastq_seq(output_fastq_file, seq_data)
            entry += 1
            seq_data = read_fastq_seq(input_fastq_file, True)
    except (ValueError, SystemError) as e:
        print(f"Error {e} in entry {entry}.")
    input_fastq_file.close()
    output_fastq_file.close()
    if no_output_fastq:
        remove(input_fastq)
        rename(output_fastq, input_fastq)
