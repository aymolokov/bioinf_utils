from os import remove, rename
from scripts.filter_fastq import write_fastq_seq, read_fastq_seq


def convert_multiline_fasta_to_oneline(input_fastq: str,
                                       output_fastq: str = "") -> None:
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


def parse_blast_output(input_txt_file: str, output_txt_file: str) -> None:
    """
    Reads a BLAST output file and writes a new file with the sorted list of
    found genes.

    Parameters:
    input_txt_file: The input BLAST output file.
    output_txt_file: The output file to write the sorted list of genes to.
    """
    genes = []
    with open(input_txt_file, "r") as input_file:
        for line in input_file:
            if line.startswith("Description"):
                input_file.readline()
                description_line = input_file.readline()
                if description_line:
                    description_parts = description_line.split("  ")
                    if description_parts:
                        description_gene = description_parts[0].split("[")
                        protein_name = description_gene[0]
                        genes.append(protein_name)
    genes.sort(key=str.lower)
    with open(output_txt_file, "w") as output_file:
        for line in genes:
            output_file.write(line + "\n")
