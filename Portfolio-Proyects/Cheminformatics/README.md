# Tyrosinase Inhibitors - Skin Permeability and Activity Prediction

This project is divided into two parts, combining computational analysis and molecule generation to identify tyrosinase inhibitors with potential skin permeability. 

## Bibliography and Data

- Literature review on tyrosinase inhibition and skin permeability properties.
- Datasets used:
  - *ChEMBL*: bioactivity data
  - *HuskinDB*: experimental human skin permeability data

## Project Structure

- `literature_search/`: Contains the initial bibliographic research, including relevant publications on tyrosinase inhibition and skin permeability.
- `Part I Tyrosinase Inhibitors Analysis/`
- `Part II Molecule Generation/`
- `Results/`

## Part I: Tyrosinase Inhibitors Analysis

- Data cleaning and preprocessing.
- Molecular descriptor and fingerprint calculation using *RDKit*.
- Random Forest classification model to predict activity (IC50 < 1000 nM).
- Skin permeability evaluation based on physicochemical property rules.
- Clustering using Tanimoto similarity for structural analysis.
- External validation with independent datasets.

##  Part 2: Molecule Generation with REINVENT

- Used REINVENT 4 to generate ~3000 novel molecules based on 4 known active compounds.
- Configuration parameters set in .toml file (batch size, steps, scoring metrics).
- Included files:  
  - JSON config and output files (gen_mols.json)  
  - Model checkpoint (mol2mol_stage1.chkpt)  
  - SMILES and TOML configuration files  
- Optimization balanced QED, SA score, and Tanimoto similarity to ensure activity, synthetic accessibility, and novelty.

## Results

- General results stored in results/ folder, including:  
  - CSV file with generated molecules and scores  
  - Visualizations and plots  
  - Top 10 promising molecules selection

## Tools and Libraries

- Python 3.x  
- RDKit  
- scikit-learn  
- REINVENT 4 (AstraZeneca)  
- matplotlib / seaborn  

