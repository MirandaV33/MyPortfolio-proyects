# Tyrosinase Inhibitors - Skin Permeability and Activity Prediction

This project focuses on the computational analysis and machine learning-based prediction of **tyrosinase inhibitors** intended for **topical use**. The aim was to identify structurally active compounds with potential **skin permeability** using cheminformatics tools.

## Project Structure

- `literature_search/`: Contains the initial bibliographic research, including relevant publications on tyrosinase inhibition and skin permeability.
- ` databases/`: Includes datasets from **ChEMBL** (bioactivity data for tyrosinase) and **HuskinDB** (experimental data on human skin permeation).
- ` notebook/`: Jupyter notebooks with all the **data cleaning**, **feature engineering**, **descriptor calculation**, **clustering**, and **model training**.

## Tools and Libraries

- **RDKit** for molecular fingerprints and chemical descriptors
- **scikit-learn** for model training (Random Forest classifier)
- **matplotlib** and **seaborn** for visualization
- **pandas/numpy** for data handling
- **SciPy** for clustering and dendrograms

## Key Methodologies

- Creation of binary activity labels (active/inactive) based on IC50 < 1000 nM
- Addition of custom fingerprint for phenolic substructures (common in tyrosinase inhibitors)
- Construction of a boolean function for skin permeability rule based on physicochemical thresholds (MW, LogP, PSA, HBA/HBD)
- Clustering based on molecular similarity using Tanimoto similarity and dendrogram analysis
- Supervised learning model (Random Forest) trained and validated on a balanced split
- External test using compounds from HuskinDB


