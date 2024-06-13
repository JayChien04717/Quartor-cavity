import numpy as np
import scipy.constants as sc

mu = sc.mu_0
sig = 5.8e7
a = 5e-3
b = 25e-3
l = 19e-3
f = sc.c/(4*l) #ideal frequency

Q = (np.sqrt(sig*mu*np.pi*f)*a*l*np.log(b/a)/
     ((l/2)*(1+a/b)+a*np.log(b/a)))


print("ideal frequency: ", f/1e9)
print("ideal quality factor", Q)
