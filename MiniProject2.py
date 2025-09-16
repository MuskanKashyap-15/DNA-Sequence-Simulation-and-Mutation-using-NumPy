# Project - Working with a gene expression dataset 

# Step 1:
# 1) Open web browser and in the search bar, type "UCI Machine Learning Repository Yeast dataset"
# 2) Click on first link and open the Yeast – UCI Machine Learning Repository page.
# 3) On the right side of the page, click on DOWNLOAD (18.5 KB) button.
# 4) Go to Downloads folder, find the file yeast.zip, right-click → Extract All
# 5) Inside, there's a file called yeast.data, move the file into project folder (where Python scripts are)


# Step 2: Load the data in Python using NumPy 

import numpy as np

data = np.genfromtxt("yeast.data", delimiter=None, dtype=str)

print("Shape of dataset:", data.shape)
print("First 5 rows:\n", data[:5]) 

# Step 3: Separate text (IDs + labels) from numbers

ids = data[:, 0]               # protein IDs
X = data[:, 1:9].astype(float) # convert numbers to float
labels = data[:, 9]            # localization labels

print("IDs:", ids[:5])
print("Numeric values:\n", X[:5])
print("Labels:", labels[:5])
print("Shape of numeric data:", X.shape)   

# Step 4: Normalize the numeric values 

X_normalized = X / np.max(X) 

print("First 5 rows (normalized):\n", X_normalized[:5]) 

# Step 5: Compute statistics

protein_means = np.mean(X, axis=1)      
print("Protein means (first 5):", protein_means[:5])

feature_means = np.mean(X, axis=0)
print("Feature means:", feature_means)


print("Max value in dataset:", np.max(X))
print("Min value in dataset:", np.min(X)) 

# Step 6: Group analysis by label  

mit_mask = labels == "MIT"
nuc_mask = labels == "NUC"

mit_mean = np.mean(X[mit_mask], axis=0)
nuc_mean = np.mean(X[nuc_mask], axis=0)

print("Average features (MIT):", mit_mean)
print("Average features (NUC):", nuc_mean)

# Step 7: Save results

np.savetxt("yeast_normalized.csv", X_normalized, delimiter=",") 
print("Normalized dataset saved!")




