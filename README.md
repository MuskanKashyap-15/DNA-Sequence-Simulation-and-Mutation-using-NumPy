# NumPy Mini Projects – DNA & Gene Expression

This repository contains two beginner-friendly projects built using **Python** and **NumPy**. Both projects highlight how NumPy can be applied in the context of **bioinformatics and biological data analysis**.

---

## Project 1: DNA Sequence Simulation and Mutation

### Overview
This project demonstrates how to simulate DNA sequences computationally using NumPy. It includes generating randomized DNA sequences, introducing mutations, analyzing nucleotide frequency, and converting DNA symbols into a numeric representation.

### Workflow
- **Sequence Generation:** Generate a random DNA sequence of a specified length (`A`, `T`, `G`, `C`).
- **Mutation Simulation:** Randomly mutate selected positions in the sequence to mimic biological mutation.
- **Frequency Analysis:** Count how often each nucleotide appears in the sequence.
- **Numeric Encoding:** Convert nucleotides into numeric values (`A=0, T=1, G=2, C=3`) for computational analysis.

### Learning Outcomes
- Representing biological sequences with NumPy arrays.
- Understanding random mutation processes computationally.
- Performing frequency analysis with array operations.
- Preparing biological data for numeric analysis and machine learning.

---

## Project 2: Gene Expression Dataset (Yeast Data)

### Overview
This project analyzes a real biological dataset: the **Yeast Protein Localization dataset** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/yeast). It demonstrates how to handle, preprocess, normalize, and analyze gene expression data.

### Workflow
1. **Data Loading:** Import the yeast dataset into NumPy.
2. **Data Separation:** Split the dataset into protein IDs, numerical features, and localization labels.
3. **Normalization:** Scale all numeric values so they range between 0 and 1.
4. **Statistical Analysis:**  
   - Calculate per-protein mean values.  
   - Calculate feature means across all proteins.  
   - Identify global maximum and minimum values in the dataset.  
5. **Group Analysis:** Compare average feature values for proteins in different localizations (e.g., mitochondria `MIT` vs. nucleus `NUC`).
6. **Result Export:** Save the normalized dataset to CSV for future analysis.

### Learning Outcomes
- Handling real-world biological datasets with NumPy.
- Data cleaning and normalization for analysis.
- Using masks for label-specific filtering in NumPy.
- Exporting processed datasets for downstream tasks.

---

## Concepts and Skills Covered
- DNA sequence representation and mutation simulation.
- Biological sequence numeric encoding.
- Statistical analysis on biological datasets.
- NumPy operations for preprocessing and normalization.
- Practical bioinformatics with Python.

---

## How to Run

1. Clone or download this repository.
2. Place the dataset (`yeast.data`) in the project folder (for Project 2).
3. Run the Python scripts:
   - `dna_sequence_simulation.py` → Project 1  
   - `yeast_dataset_analysis.py` → Project 2  

---

## Requirements

- Python 3.x  
- NumPy  




