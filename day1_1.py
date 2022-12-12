"""
# QUESTION

# The information in DNA is stored as a sequence of four chemical bases (adenine, guanine, cytosine, and thymine).
# These four bases are often represented by the letters A, G, C and T. Sequences of DNA, then, can be represented
# by strings of these characters.

# Imagine the task of checking whether a given genome (long string of "ACGT" bases) contains a specified gene
# (shorter sequence of bases) as a substring. One way to do this is to loop over every index in the genome, and
# try to match the gene sequence from each location. This will take (in the worst case) a number of steps
# proportional to the length of the genome multiplied by the length of the gene sequence. 
"""

# def gene_search(s, t):
#     if t in s:
#         return True
#     else:
#         return False                

def gene_search(s, t):
    initial_point = 0
    end_point = len(t) 

    while end_point <= len(s):
        if s[initial_point:end_point] == t:
            return True
        initial_point+=1
        end_point+=1
    return False

print(gene_search("ACCATGCA", "GCA"))
print(gene_search("CATTGA", "CAT"))
print(gene_search("GGCACACATG", "CACAT"))
print(gene_search("CAAAT", "CAT"))
print(gene_search("ATTTGAGAGAAGAGACCATGCACATTGAGGCACACATGCAAAT", "TTGAGGCACACATGCA"))