def distance(strand_a, strand_b):

    if len (strand_a) != len (strand_b):
        raise ValueError("Error 1: strands are of different lengths")

    return len ([(a, b) for (a, b) in zip(strand_a, strand_b) if a != b])

# Original solution
#    hamdist = 0
#    pos = 0
#    while pos < len (strand_a):
#        if strand_a[pos] != strand_b[pos]:
#            hamdist += 1
#        pos +=1

#    return (hamdist)

# Program tester
#while True:
#    strandA = input ("Enter Strand A: ")
#    if strandA == "done":
#         break

#    strandB = input ("Enter Strand B: ")
#    if strandB == "done":
#         break

#    hammingDist = distance(strandA,strandB)
#    print ("Hamming Distance: ", hammingDist)

#print("=> End of program")
