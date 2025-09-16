# Project - DNA Sequence Simulation and Mutation 

# In this Project, we'll use NumPy to:
# 1) Generate a random DNA Sequence
# 2) Introduce random mutations
# 3) Count nucleotide frequencies 
# 4) Represent DNA as numbers (for analysis)


import numpy as np

# Possible nucleotides
nucleotides = np.array(['A', 'T', 'G', 'C'])

# Generate random DNA sequence of length 20
sequence = np.random.choice(nucleotides, size=20)
print("Random DNA sequence:", ''.join(sequence))  

# Choose random mutation positions  
mutation_positions = np.random.choice(len(sequence), size=3, replace=False)  

print("Original sequence:", ''.join(sequence))  
print("Mutation positions:", mutation_positions)  

# Apply mutations  
for pos in mutation_positions:  
    # pick a nucleotide different from the original  
    new_nucleotide = np.random.choice(nucleotides[nucleotides != sequence[pos]])  
    sequence[pos] = new_nucleotide  

print("Mutated sequence :", ''.join(sequence))   

# Count nucleotide frequencies 
unique, counts = np.unique(sequence, return_counts=True)

freq_dict = {}  

for k, v in zip(unique, counts):   
    key = str(k)       
    value = int(v)     
    freq_dict[key] = value   

print("DNA sequence:", ''.join(sequence))
print("Frequencies:", freq_dict)  

# Represent DNA as Numbers
mapping = {'A': 0, 'T': 1, 'G': 2, 'C': 3}
numeric_seq = np.array([mapping[nuc] for nuc in sequence])

print("Numeric representation:", numeric_seq) 










 






