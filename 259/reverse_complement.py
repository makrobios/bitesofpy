# See tests for a more comprehensive complementary table
SIMPLE_COMPLEMENTS_STR = """#Reduced table with bases A, G, C, T
 Base	Complementary Base
 A	T
 T	A
 G	C
 C	G
"""

# Recommended helper function
def _clean_sequence(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns all sequences converted to upper case and remove invalid
    characters
    t!t%ttttAACCG --> TTTTTTAACCG
    """
    clean_seq = ''
    compl_dict = {}
    for line in str_table.splitlines()[2:]:
        base = line.split()[0]
        comp = line.split()[-1]
        compl_dict[base] = comp
    for base in sequence:
        base = base.upper()
        if base in compl_dict.keys():
            clean_seq += base
    return clean_seq, compl_dict    

def reverse(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a reversed string of sequence while removing all characters
    not found in str_table characters
    e.g. t!t%ttttAACCG --> GCCAATTTTTT
    """
    clean_seq, compl_dict = _clean_sequence(sequence, str_table)
    return clean_seq[::-1]



def complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in
    str_table while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> AAAAAATTGGC
    """
    clean_seq, compl_dict = _clean_sequence(sequence, str_table)
    complement = ''
    for base in clean_seq:
        complement += compl_dict[base]
    return complement


def reverse_complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in str_table
    while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> CGGTTAAAAAA
    """
    clean_seq, compl_dict = _clean_sequence(sequence, str_table)
    return complement(reverse(clean_seq, str_table), str_table)

COMPLEMENTS_STR = """# Full table with ambigous bases
 Base	Name	Bases Represented	Complementary Base
 A	Adenine	A	T
 T	Thymidine	T 	A
 U	Uridine(RNA only)	U	A
 G	Guanidine	G	C
 C	Cytidine	C	G
 Y	pYrimidine	C T	R
 R	puRine	A G	Y
 S	Strong(3Hbonds)	G C	S
 W	Weak(2Hbonds)	A T	W
 K	Keto	T/U G	M
 M	aMino	A C	K
 B	not A	C G T	V
 D	not C	A G T	H
 H	not G	A C T	D
 V	not T/U	A C G	B
 N	Unknown	A C G T	N
"""


AMBIGOUS_DIRTY = "AGB Vnc gRy Tvv V"
#         # ("TAC WSA YBG KGK DVN YRS TGG TAC TAA TGC CTA AGT GAC CGG CAG CAA AAT GTT"
#        # " GCA GCA CTG ACC CTT TTG GGA CCG CAA TGG GTT GAA TTA GCG GAA CGT CGT GT"
#        # "A GGG GGA AAG CGG TCG ACC GCA TTA TCG CTT CTC CGG GCG TGG CTA GCG GGA A"
#        # "GG GTT GTC AAC GCG TCG GAC TTA CCG CTT ACC GCG AAA CGG ACC AAA GGC CGT "
#        # "GGT CTT CGC CAC GGC CTT TCG ACC GAC CTC ACG CTA GAA GGA")

# print('rev_comp: ', reverse_complement(AMBIGOUS_DIRTY, COMPLEMENTS_STR))
print('comp: ',complement(AMBIGOUS_DIRTY, COMPLEMENTS_STR))
#print('reverse: ',reverse(AMBIGOUS_DIRTY, COMPLEMENTS_STR))