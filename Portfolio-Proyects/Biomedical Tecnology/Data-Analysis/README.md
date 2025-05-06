# Frequency and Amplitude Estimation with Spectral Windows

This project explores the performance of different spectral estimators for frequency and amplitude detection in noisy signals. We simulate sinusoidal signals with additive Gaussian noise, and analyze how different window functions affect bias and variance in the estimators.

## Project Objectives

- Implement custom estimators based on known signal parameters.
- Compare the effect of different window functions (Rectangular, Barthann, Blackman-Harris, Flattop).
- Evaluate bias and variance under different SNR conditions.
- Analyze spectral resolution and estimation accuracy with and without zero-padding.
- Visualize results using histograms and power spectral density plots.

## Tools & Techniques

- Python (NumPy, Matplotlib)
- Jupyter Notebook
- Fourier Transform-based estimators
- Custom amplitude estimation
- Window functions and spectral analysis
- Welch and Blackman-Tukey methods (to be explored in future extensions)

## Results

Included figures:
- Spectral representations for each window
- Histograms of estimated frequencies and amplitudes
- Bias and variance comparison table

These results show how some windows increase bias but reduce variance — a trade-off we discuss in the analysis. In real applications, we prioritize low variance estimators, since bias can often be corrected using gain compensators.

## Files

- `main_code.py`: core estimation functions and simulations
- `notebook.ipynb`: full analysis with visualizations
- `/figures`: plots used in the analysis
- `bias_variance_table.png`: summary table of estimator performance

## Final Report

You can find a full summary of the results, analysis, and conclusions in the TS4. Viceconte.ipynb
##  This repository is part of my portfolio. Feel free to explore all my work and experience!

