def to_rna(dna_strand):
    dna_dict = {"G":"C", "C":"G", "T":"A", "A":"U"}

# Compact solution
    return "".join([dna_dict.get(nuc,"") for nuc in dna_strand])

# Step by step solution
#    rna_strand = ""
#    for nuc in dna_strand:
#        rna_strand += dna_dict.get(nuc,"")
#    return rna_strand

# Program tester
#while True:
#    dna_strand = input("DNA strand: ")
#    if dna_strand == "done":
#         break
#    print("RNA transcription: ", to_rna(dna_strand))
#
#print("=> End of program")
