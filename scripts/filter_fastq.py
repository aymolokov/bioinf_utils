import typing
from typing import Union
from scripts.dna_rna_tools import is_dna, is_rna


def avg_quality(seq_quality: str) -> float:
    """
    Calculate the average quality score of the given sequence quality.
    """
    return sum(ord(base) - 33 for base in seq_quality) / len(seq_quality)


def gc_percent(seq: str) -> float:
    """
    Calculate the GC content of the given sequence.
    """
    return (seq.count("G") + seq.count("C")) / len(seq) * 100


def convert_bounds(bounds: Union[int, float, list]) -> list:
    """
    Convert bounds to a valid range.
    If only one bound is passed, convert it to [0, bounds].
    """
    if isinstance(bounds, int) or isinstance(bounds, float):
        return [0, bounds]
    else:
        return bounds


def filter_fastq_seq(seq_data: str, gc_bounds: Union[int, float, list],
                     length_bounds: Union[list[int, int], int],
                     quality_threshold: float) -> bool:
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


def read_fastq_seq(fastq_file: typing.TextIO,
                   multiline_seq: bool = False) -> typing.List[str]:
    """
    Reads a FASTQ sequence from the given file and returns a list of 4 strings:
    name, description, sequence and quality.
    If the file is closed or empty, returns an empty list.
    If the FASTQ entry is invalid in any way, raises a ValueError with
    a description of the problem.

    If multiline_seq is True, reads the sequence from multiple lines until the
    line starting with "+" is encountered.
    """
    seq_data = []
    if fastq_file.closed:
        raise SystemError("The FASTQ file is not open.")
    title = fastq_file.readline().rstrip('\n')
    if not title:
        return seq_data
    if len(title) < 2 or title[0] != "@":
        raise ValueError("Invalid Field 1 in the FASTQ entry.")
    separator_index = title.find(" ")
    name = title[1:separator_index]
    desc = "" if separator_index == -1 else title[separator_index + 1:]
    seq_data.append(name)
    seq_data.append(desc)

    seq = fastq_file.readline().rstrip('\n')
    seq_len = len(seq)
    if seq_len < 1 or not (is_rna(seq) or is_dna(seq)):
        raise ValueError("Invalid Field 2 in the FASTQ entry.")
    line = fastq_file.readline().rstrip('\n')
    if multiline_seq:
        while line and line[0] != "+":
            seq += line
            seq_len += len(line)
            line = fastq_file.readline().rstrip('\n')
    seq_data.append(seq)
    comp = line
    if not comp or comp[0] != "+":
        raise ValueError("Invalid Field 3 in the FASTQ entry.")
    seq_data.append(comp)
    qual = fastq_file.readline().rstrip('\n')
    if len(qual) != seq_len:
        raise ValueError("Invalid Field 4 length in the FASTQ entry.")
    for base in qual:
        if not (33 <= ord(base) <= 126):
            raise ValueError("Invalid Field 4 in the FASTQ entry.")
    seq_data.append(qual)
    return seq_data


def write_fastq_seq(fastq_file: typing.TextIO, seq_data: typing.List[str]):
    """
    Writes a FASTQ sequence to the given file from the given seq_data.

    The seq_data must be a list of 5 strings: name, description, sequence,
    comment and quality.

    If the file is closed, raises a SystemError with the problem description.
    """
    if fastq_file.closed:
        raise SystemError("The FASTQ file is not open.")
    fastq_file.write(f"@{seq_data[0]}")
    if (seq_data[1] != ""):
        fastq_file.write(f" {seq_data[1]}")
    fastq_file.write(f"\n{seq_data[2]}\n{seq_data[3]}\n{seq_data[4]}\n")
