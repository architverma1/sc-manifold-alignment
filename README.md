# sc-manifold-alignment
Code for recreating results from "A Bayesian nonparametric semi-supervised model for integration of multiple single-cell experiments." Given multiple single cell RNA seq datasets with some shared genes, sstGPVLM fits a joint latent space that can be used for downstream analysis. 

## Fitting
alignment-scripts contains python scripts for fitting the model to data. 

## Requirements
sstGPLVM is implemented in python 2.7 with:

numpy 1.14.5
pandas 0.23.3
h5py 2.8.0
tensorflow 1.6.0
edwards 1.3.5
sklearn 0.19.2

## Analysis
analysis-nbs contains jupyter notebooks and the required output files for recreating figures from the paper. 

## Data

