# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:18:29 2019

@author: DRIRA Hassen
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import null_space


def stationnaire(P):
    # a implementer
    pass
    return None


def stochastique(P):
    # a implementer
    pass


def puits(P, i):
    # a implemter
    pass


def simulation(P, pi0, t0, tf):
    # Simulation numerique d'une chaine de Markov en temps discret
    # P	    : matrice de transition
    # pi0	: vecteur stochastique initial (a l'instant t0)
    # t0	: instant initial (debut de la simulation)
    # tf	: instant final
    # pi	: matrice des valeurs successives du vecteur stochastique
    # t     : liste des instants (t0 <= t <= tf)

    t = np.arange(t0, tf + 1)
    # controles
    if P.shape[0] != P.shape[1] | P.shape[0] != pi0.len:
        print("dimensions incorrectes")
    elif not stochastique(P):
        print("la matrice n est pas stochastique")

    # evolution du vecteur stochastique
    pi = np.array(np.zeros((len(t), P.shape[1])))
    pi[0] = pi0
    for i in range(1, len(t)):
        pi[i] = pi[i - 1].dot(P)
    plt.plot(t, pi)
    return t, pi


def Diagonalisation(P):
    # a implementer
    # liste d'exemples de chaines de Markov
    pass


def Exemple(n):
    if n == 1:
        print("shadock")
        P = np.array(
            [[5 / 6, 1 / 12, 1 / 12], [1 / 4, 1 / 2, 1 / 4], [1 / 4, 0, 3 / 4]]
        )
        pi0 = [1, 0, 0]
    elif n == 2:
        print("imprimante")
        P = np.array([[0.2, 0.8, 0], [0.04, 0.95, 0.01], [0.3, 0, 0.7]])
        pi0 = [1, 0, 0]

        #  ajouter d'autres exemples

    return P, pi0
