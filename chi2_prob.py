# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 01:04:37 2022

@author: srpdo
"""
import  numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

def chi2_prob(chi2,dof):
    
    #Chi Square Distribution
    
    cons = 1/((2**(dof/2))*gamma((dof/2)))
    mult = chi2**((dof/2)-1)*np.exp(-chi2/2)
    return cons*mult

chi2 = np.linspace(0.3, 25.0, 100)      #100 eqaully spaced chi^2 values from 0.3 to 25
dof_max = 20                            #max degrees of freedom to display on graph


#ploting for all dof and chi^2 values
for dof in range(dof_max):
    plt.plot(chi2,chi2_prob(chi2, dof))

plt.xlabel("Chi Square")
plt.ylabel("Probability")    
plt.title("Chi Square Probability Distribution for varying DOF")
plt.show()
