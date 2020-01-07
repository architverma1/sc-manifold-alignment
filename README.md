# sc-manifold-alignment
Code for recreating results from "A Bayesian nonparametric semi-supervised model for integration of multiple single-cell experiments." Given multiple single cell RNA seq datasets with some shared genes, sstGPVLM fits a joint latent space that can be used for downstream analysis. 

## Fitting
analysis-scripts contains python scripts for fitting the model to data. Requirements are the same as for tGPVLM (https://github.com/architverma1/tGPLVM).

## Analysis
analysis-nbs contains jupyter notebooks and the required output files for recreating figures from the paper. 
