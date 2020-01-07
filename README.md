# sc-manifold-alignment
Code for recreating results from "A Bayesian nonparametric semi-supervised model for integration of multiple single-cell experiments." Given multiple single cell RNA seq datasets with some shared genes, sstGPVLM fits a joint latent space that can be used for downstream analysis. 

## Fitting
alignment-scripts contains python scripts for fitting the model to data. It also contains a python script for calculating the average $W_2$-based distance of a fit from the true latent space.

### Requirements
sstGPLVM is implemented in python 2.7 with:

1. numpy 1.14.5
2. pandas 0.23.3
3. h5py 2.8.0
4. tensorflow 1.6.0
5. edwards 1.3.5
6. sklearn 0.19.2

### Running
**Input**: 
1. A numpy array or sparse csr/csc matrix of scRNA counts (or other types data) with format *N* cells (samples) as rows by *p* genes (features) as columns (loaded to ```y_train```). Input this directly into the code as y_train.
2. A numpy array of relevant metadata with format *N* cells as rows by *m* metadata fatures (loaded to ```z_init```).

**Options**:
The following parameters can be adjusted in the script to adjust inference:

1. Degrees of freedom (```--df```) - default: 4
2. Use t-Distribution error model (otherwise normal error) (```--T```) - default: True
3. Initial Number of Dimensions (```--Q```) - default: 3
4. Kernel Function
    + Matern 1/2, 3/2, 5/2 (```--m12, --m32, --m52```) - default: False
    + Periodic (```--per_bool```) - default: False
5. Number of Inducing Points (```--m```) - default: 30
6. Batch size (```--M```) - default: 250
7. Max iterations (```--iterations```) - default: 5000
8. Save frequency (```--save_freq```): - default: 250
9. Sparse data type (is CSC or CSR) (```--sparse```): - default: False
10. PCA Initialization (otherwise random initialization) (```--pca_init```): - default: True
11. Output directory (```--out```): - default: ./test

**Output**: hdf5 file with
1. Latent mapping posterior (mean and variance)
2. Gene-specific noise
3. Kernel hyperparameters (variance, lengthscale)
4. Inducing points in latent and high-dimensional space

## Analysis
analysis-nbs contains jupyter notebooks and the required output files for recreating figures from the paper. 

## Data

