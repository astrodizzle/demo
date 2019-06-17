import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

m50 = 'z6_4350gals_abun_abun'
xx = pd.read_pickle(m50)

L_CII = []
for i in range(len(xx.galnames)):
   L_CII.append(xx.L_CII[i])
   
L_CII_ionized = []
for i in range(len(xx.galnames)):
   L_CII_ionized.append(xx.L_CII_DIG[i])

L_CII_neutral = []
for i in range(len(xx.galnames)):
   L_CII_neutral.append(xx.L_CII_DNG[i])
   
L_CII_GMC = []
for i in range(len(xx.galnames)):
    L_CII_GMC.append(xx.L_CII_GMC[i])   
   
M_gas = []
for i in range(len(xx.galnames)):
    M_gas.append(xx.M_gas[i])
    
M_star = []
for i in range(len(xx.galnames)):
    M_star.append(xx.M_star[i])
 
M_DNG = []
for i in range(len(xx.galnames)):
    M_DNG.append(xx.M_DNG[i])
    
M_DIG = []
for i in range(len(xx.galnames)):
    M_DIG.append(xx.M_DIG[i])
    
M_GMC = []
for i in range(len(xx.galnames)):
    M_GMC.append(xx.M_GMC[i])

SFR = []
for i in range(len(xx.galnames)):
    SFR.append(xx.SFR[i]) 

Z_SFR = []
for i in range(len(xx.galnames)):
    Z_SFR.append(xx.Zsfr[i])    

LCII_over_Mgas = np.array(L_CII)/np.array(M_gas)

SSFR_over_ASFR = (np.array(SFR) / np.array(M_star)) / np.mean(SFR)
    
def best_fit(xd, yd, order=1, c='r', alpha=1, Rval=False):
    """Make a line of best fit"""

    coeffs = np.polyfit(xd, yd, order)

    intercept = coeffs[-1]
    slope = coeffs[-2]
    power = coeffs[0] if order == 2 else 0
    
    print("Slope is " + str(slope))
    print("Power is " + str(power))
    print ("Intercept is " + str(intercept))

    minxd = np.min(xd)
    maxxd = np.max(xd)

    xl = np.array([minxd, maxxd])
    yl = power * xl ** 2 + slope * xl + intercept

    plt.plot(xl, yl, alpha=alpha,c='magenta')
    plt.scatter(xd,yd,s=5,c='r')

#    a = str(input("X value? "))
#    b = str(input("Y value? "))
#    
#    plt.title(b + " as a function of " + a)
    
    #Calculate R Squared
    p = np.poly1d(coeffs)

    ybar = np.sum(yd) / len(yd)
    ssreg = np.sum((p(xd) - ybar) ** 2)
    sstot = np.sum((yd - ybar) ** 2)
    Rsqr = ssreg / sstot

    if not Rval:
        #Plot R^2 value
        plt.text(0.8 * maxxd + 0.2 * minxd, 0.8 * np.max(yd) + 0.2 * np.min(yd),
                 '$R^2 = %0.2f$' % Rsqr)
    else:
        #Return the R^2 value:
        return Rsqr  
