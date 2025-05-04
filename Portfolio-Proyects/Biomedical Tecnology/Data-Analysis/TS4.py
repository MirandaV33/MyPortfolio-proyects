# %%
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 17:28:09 2025

@author: l
"""


import numpy as np
from scipy import signal
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt


## What do I want to do with this task? 
#-----> Estimate the spectrum when we have "unknown" samples 
# For this, we mainly want to find three estimators: estimated amplitude, spectral power, and frequency estimation

#%% Function definitions

def estimador_omega(f_t, N, df):
    FT_abs = np.abs(f_t[:N//2, :])
    omega_est = np.argmax(FT_abs, axis=0) * df
    return omega_est

#%% Simulation data, constant definition

Np=1000 
SNRs = [3, 10]
R=200 #number of samples
a1= np.sqrt(2) #Signal amplitude, choosing this normalizes the signal. No need to divide by the standard deviation anymore
fs = 1000 #sampling frequency (Hz) convenient integer known number 
N = 1000 #number of samples
N2= 10*N
ts = 1/fs  #sampling time
df= fs/N #spectral resolution 
df_pp=fs/N2
omega0= fs/4

#%% Signal X generation

# Define S

# Temporal sampling grid ---> TIME DISCRETIZATION (sampling)
tt = np.linspace(0, (N-1)*ts, N).reshape((1000, 1))  #[1000x1]
tt= np.tile(tt, (1, R)) #Repetition [100x200]

# Frequency sampling grid
ff= np.linspace(0, (N-1)*df, N) #.reshape(1, 1000) # [1,1000]
fr = np.random.uniform(-1/2, 1/2, size=(1,R)) # [1, 200]

omega1= omega0 + fr* (df)

S= a1*np.sin(2*np.pi*omega1*tt)

# Define the Barthann window
M=N
w= signal.windows.barthann(M).reshape((Np, 1)) #[1000, 1]

# Define the Blackman-Harris window
w2= signal.windows.blackmanharris(M).reshape((Np, 1)) #[1000, 1]

# Define the Flattop window
w3= signal.windows.flattop(M).reshape((Np, 1)) #[1000, 1]

# Frequency grid  
freqs = np.fft.fftfreq(N, d=ts)

# %% Loop for each SNR value
for snr_db in SNRs:
    # #%% Noise data
    
    # # Analog signal --> Obtained from SNR
    pot_ruido_analog = 10**(- snr_db / 10)
    sigma= np.sqrt(pot_ruido_analog)
    # #Generation of analog noise 
    nn = np.random.normal(0, sigma, (Np, R)) 
     
    # Final signal 
    xx = S + nn  # [1000x200]
    
    # Multiplication 
    xw= xx * w  # [1000, 200] * [1000, 1] → [1000, 200]
    xw2= xx * w2 
    xw3= xx * w3
    
    # Transform and estimators 

    # Compute the transform without zero padding 
    ft_xx = 1/N * np.fft.fft(xx,  axis=0) 
    ft_xw = 1/N * np.fft.fft(xw, axis=0) 
    ft_xw2 = 1/N * np.fft.fft(xw2, axis=0)
    ft_xw3 = 1/N * np.fft.fft(xw3, axis=0) 
    
    
    # Compute the transform with zero padding 
    ft_xx_pp = 1/N * np.fft.fft(xx,n=N2, axis=0) 
    ft_xw_pp = 1/N * np.fft.fft(xw, n=N2, axis=0) 
    ft_xw2_pp = 1/N * np.fft.fft(xw2, n=N2, axis=0)
    ft_xw3_pp = 1/N * np.fft.fft(xw3, n=N2, axis=0)
    
    # Compute the amplitude estimator (a1=mod(ft_xw))
    
    #Estimator---> in N/4 of the xx matrix is 
    # # Estimator without windowing
    a1_est= np.abs(ft_xx[N//4, :])  # [1000, 200] // Integer division   
    
    # # Estimator with Barthann window
    a1_est2= np.abs(ft_xw[N//4, : ])  # [1000, 200]
    
    # # Estimator with Blackman-Harris window
    a1_est3= np.abs(ft_xw2[N//4, :])  # [1000, 200]
    
    # # Estimator with Flattop window
    a1_est4= np.abs(ft_xw3[N//4, :])  # [1000, 200]
    
    #Compute frequency estimator (without zero padding)
    #WITH ZERO PADDING
    omega1_est_pp = estimador_omega(ft_xx_pp, N2, df_pp)
    omega2_est_pp = estimador_omega(ft_xw_pp, N2, df_pp)
    omega3_est_pp = estimador_omega(ft_xw2_pp, N2, df_pp)
    omega4_est_pp = estimador_omega(ft_xw3_pp, N2, df_pp)
    
    # BONUS – WITHOUT ZERO PADDING
    omega1_est = estimador_omega(ft_xx, N, df)
    omega2_est = estimador_omega(ft_xw, N, df)
    omega3_est = estimador_omega(ft_xw2, N, df)
    omega4_est = estimador_omega(ft_xw3, N, df)
    
    #Compute the bias and variance of the amplitude estimator
    valor_real=a1
    esperanza_a1_xx= np.mean(a1_est)
    esperanza_a1_xw= np.mean(a1_est2)
    esperanza_a1_xw2=np.mean(a1_est3)
    esperanza_a1_xw3= np.mean(a1_est4)
    
    sesgo_a1_xx= esperanza_a1_xx-valor_real
    sesgo_a1_xw= esperanza_a1_xw-valor_real
    sesgo_a1_xw2=esperanza_a1_xw2-valor_real
    sesgo_a1_xw3= esperanza_a1_xw3-valor_real
    
    varianza_a1_xx= np.var(a1_est)
    varianza_a1_xw=np.var(a1_est2)
    varianza_a1_xw2=np.var(a1_est3)
    varianza_a1_xw3=np.var(a1_est4)
    
    #Compute the bias and variance of the spectral frequency estimator
    
    valor_real2= omega0

    esperanza_o_xx= np.mean(omega1_est)
    esperanza_o_xw= np.mean(omega2_est)
    esperanza_o_xw2=np.mean(omega3_est)
    esperanza_o_xw3= np.mean(omega4_est)
    
    sesgo_xx_o= esperanza_o_xx-valor_real2
    sesgo_xw_o= esperanza_o_xw-valor_real2
    sesgo_xw2_o=esperanza_o_xw2-valor_real2
    sesgo_xw3_o= esperanza_o_xw3-valor_real2
    
    varianza_xx_o= np.var(omega1_est)
    varianza_xw_o=np.var(omega2_est)
    varianza_xw2_o=np.var(omega3_est)
    varianza_xw3_o=np.var(omega4_est)
    

    nombres_ventanas = ['Rectangular', 'BartHann', 'Blackman-Harris', 'Flattop']
    sesgos_amplitud = [sesgo_a1_xx, sesgo_a1_xw, sesgo_a1_xw2, sesgo_a1_xw3]
    varianzas_amplitud = [varianza_a1_xx, varianza_a1_xw, varianza_a1_xw2, varianza_a1_xw3]
    sesgos_frecuencia = [sesgo_xx_o, sesgo_xw_o, sesgo_xw2_o, sesgo_xw3_o]
    varianzas_frecuencia = [varianza_xx_o, varianza_xw_o, varianza_xw2_o, varianza_xw3_o]
    
    # Create data as a list of rows
    tabla_datos = []
    for i in range(len(nombres_ventanas)):
        fila = [
            nombres_ventanas[i],
            round(sesgos_amplitud[i], 6),
            round(varianzas_amplitud[i], 6),
            round(sesgos_frecuencia[i], 6),
            round(varianzas_frecuencia[i], 6)
        ]
        tabla_datos.append(fila)
    
    # Show the table as an image
    fig, ax = plt.subplots(figsize=(10, 2 + len(tabla_datos)*0.5))
    ax.axis('off')
    tabla = ax.table(
        cellText=tabla_datos,
        colLabels=['Window', 'Bias A1', 'Variance A1', 'Bias Ω1', 'Variance Ω1'],
        loc='center',
        cellLoc='center',
        colLoc='center'
    )
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(10)
    tabla.scale(1.2, 1.2)
    
    plt.show()
    
    # Set the title of the plot
    plt.title('Bias and Variance of SNR Estimators {} dB'.format(snr_db), fontsize=14)
    plt.tight_layout()
    plt.show()

    ###HISTOGRAM###
    # First histogram: Estimated frequencies without windowing
    plt.figure()
    plt.hist(omega1_est, bins=10, color='red', alpha=0.5, label="Unwindowed estimator")
    plt.hist(omega2_est, bins=10, color='green', alpha=0.5, label="Barthann window estimator")
    plt.hist(omega3_est, bins=10, color='blue', alpha=0.5, label="Blackman-Harris window estimator")
    plt.hist(omega4_est, bins=10, color='pink', alpha=0.5, label="Flattop window estimator")
    plt.title("Histogram of estimated frequencies (200 realizations)- SNR {} dB".format(snr_db))
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Number of occurrences")
    plt.grid(True)
    plt.legend()

    # Second histogram: Estimated frequencies with zero padding
    plt.figure()
    plt.hist(omega1_est_pp, bins=30, color='red', alpha=0.5, label="Unwindowed estimator")
    plt.hist(omega2_est_pp, bins=30, color='green', alpha=0.5, label="Barthann window estimator")
    plt.hist(omega3_est_pp, bins=30, color='blue', alpha=0.5, label="Blackman-Harris window estimator")
    plt.hist(omega4_est_pp, bins=30, color='pink', alpha=0.5, label="Flattop window estimator")
    plt.title("Histogram of estimated frequencies (200 realizations)- SNR {} dB (zero padding)".format(snr_db))
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Number of occurrences")
    plt.grid(True)
    plt.legend()

    # Third histogram: Estimated amplitudes
    plt.figure()
    plt.hist(a1_est, bins=10, color='red', alpha=0.5, label="Unwindowed estimator") # Bins: spectral resolution of the histogram; relative count. WIDTH of the values.
    plt.hist(a1_est2, bins=10, color='green', alpha=0.5, label="Barthann window estimator")
    plt.hist(a1_est3, bins=10, color='blue', alpha=0.5, label="Blackman-Harris window estimator")
    plt.hist(a1_est4, bins=10, color='pink', alpha=0.5, label="Flattop window estimator")
    plt.legend()

    plt.title("Histogram of estimated amplitudes - SNR {} dB".format(snr_db))
    plt.xlabel("Estimated amplitude")
    plt.ylabel("Number of occurrences")
    plt.grid(True)

    # Spectral representation plot
    plt.figure()
    bfrec = ff <= fs / 2  # Filter for positive frequencies
    plt.plot(ff[bfrec], 10 * np.log10(2 * np.abs(ft_xx[bfrec])**2))
    plt.title('Spectral Representation')
    plt.ylabel('Power Spectral Density [dB]')
    plt.xlabel('Frequency [Hz]')
    axes_hdl = plt.gca()
    axes_hdl.legend()

    plt.show()

#%% BONUS

def estimador_omega2(f_t, N, df):
    FT_abs = np.abs(f_t[:N//2, :])
    P_est = (1/N) * (FT_abs ** 2)
    omega_est = np.argmax(P_est, axis=0) * df
    return omega_est

# ## --> Amplitude estimator 
a1_est= np.abs(ft_xx)  # [1000, 200]
a1_est_max = np.max(a1_est, axis=0) 



