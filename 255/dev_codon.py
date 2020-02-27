import os
from urllib.request import urlretrieve
import re
from collections import Counter

TRANSL_TABLE_11 = """
    AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------**--*----M------------MMMM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
"""
# Converted from http://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Staphylococcus_aureus_Newman_uid58839/NC_009641.ffn  # noqa E501
URL = "https://bites-data.s3.us-east-2.amazonaws.com/NC_009641.txt"

# Order of bases in the table
BASE_ORDER = ["U", "C", "A", "G"]


def _preload_sequences(url=URL):
    """
    Provided helper function
    Returns coding sequences, one sequence each line
    """
    filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
    if not os.path.isfile(filename):
        urlretrieve(url, filename)
    with open(filename, "r") as f:
        return f.readlines()


def return_codon_usage_table(
    sequences=_preload_sequences(), translation_table_str=TRANSL_TABLE_11
):
    """
    Receives a list of gene sequences and a translation table string
    Returns a string with all bases and their frequencies in a table
    with the following fields:
    codon_triplet: amino_acid_letter frequency_per_1000 absolute_occurrences

    Skip invalid coding sequences:
       --> must consist entirely of codons (3-base triplet)
    """
    total_codons = []
    for seq in sequences:
        # skip invalid sequences
        seq = seq.strip().replace('T','U')
        if len(seq) % 3 != 0:
            next
        else:
            stop = len(seq) + 3 
            rng = zip( range(0,stop,3), range(3,stop,3) )
            codons = [ seq[a:e] for a, e in rng ]
            total_codons += codons

    num_of_codons = len(total_codons)
    absolut = Counter(total_codons)
    result_dict = { k: {'abs':v, 'freq': v/num_of_codons} for k, v in absolut.items() }

    table = TRANSL_TABLE_11.replace('T','U').split('\n')[1:6]
    table = [ re.sub('.* = ', '', line ) for line in table]
    for aa, __, first, sec, third in zip(*table):
        codon = first + sec + third
        result_dict[codon].update({'AA':aa})

    header = '|' + ' Codon  AA  Freq  Count   |' * 4
    separator = '-' * len(header)
    vsep = '|'
    string = header + '\n'
    for base_1 in BASE_ORDER:
        string += separator + '\n'
        for base_3 in BASE_ORDER:
            string += '|'
            for num, base_2 in enumerate(BASE_ORDER,1):
                codon = base_1 + base_2 + base_3
                dct = result_dict[codon]
                string += ' {:<5s}  {:>1s}  {:>4.1f}  {:>5d}  {:>3}'.format( 
                                                         codon + ':',
                                                         dct['AA'],
                                                         dct['freq']*1000,
                                                         dct['abs'],
                                                         vsep)  
                if num % 4 == 0:
                    string+='\n'
    string += separator
    return string

print(return_codon_usage_table())
