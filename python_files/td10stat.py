import scipy as sp
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import sys

np.set_printoptions(precision=2,suppress=True)
def Q1a():
    nbappel = np.arange(11)
    nbocc = np.array([2,14,23,24,18,9,6,2,1,0,1])
    plt.hist(x = nbappel, bins = np.arange(-0.5,11,1),weight=nbocc)
    plt.show()

def Q1b():
    nbappel = np.arange(11)
    nbocc = np.array([2, 14, 23, 24, 18, 9, 6, 2, 1, 0, 1])
    n = np.sum(nbocc)
    esp = np.sum(nbappel*nbocc)/n
    varnat = np.sum((nbappel-esp)**2*nbocc)/(n)
    varsb = np.sum((-esp)**2*nbocc)/(n-1)
    print("Esperance : 4%\t Variance naturelle : %.4f\t Variance sans biais : %.4f"%(esp,varnat,varsb))


def Q1d():
    l = 3.15
    for i in range(16):
        print("%i: %.3f"%(i, 100*st.poisson(l).pmf(i)))
    efftho = 100*st.poisson(l).pmf(np.arange(16))
    print(efftho)

def Q1f():
    nbappel = np.arange(11)
    nbocc = np.array([2, 14, 23, 24, 18, 9, 6, 2, 1, 0, 1])
    l = 3.15
    n = np.sum(nbocc)
    efftho = n*st.poisson(l).pmf(np.arange(16))
    #Classe 0 et classe k pour k>=7 trop petites
    #Creation d'une classe 0-1 et d'une classe 6+
    efftho2 = np.array([efftho[0]+efftho[1]]+list(efftho[2:6])+[n-np.sum(efftho[:6])])
    effobs2 = np.array([nbocc[0]+nbocc[1]]+list(nbocc[2:6])+[n-np.sum(nbocc[:6])])
    print("Theorique :", efftho2)
    print("Observé : ",effobs2)
    chi2 = (efftho2-effobs2)**2/efftho2
    print("chi2 :",chi2)
    chi2tot=np.sum(chi2)
    print("chi2tot :", chi2tot)
    ddl = len(efftho2)-1-1
    print("Chi2 max avec %i degrés de liberté : %.3f"%(ddl,st.chi2(ddl).ppf(0.1)))




if __name__ == '__main__':
    print(Q1a)
    print(Q1b)
    print(Q1d)
