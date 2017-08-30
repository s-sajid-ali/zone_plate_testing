# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 11:38:01 2017

@author: sajid
"""

import numpy as np
import numpy.fft as fft


def propTF(u1,step,L,wavel,z) :
    M,N = np.shape(u1)
    #k = 2*np.pi/wavel
    fx = fft.fftfreq(M,d=step)
    fy = fft.fftfreq(N,d=step)
    FX,FY = np.meshgrid((fx),(fy))
    H = np.exp(-1j*np.pi*wavel*z*(FX**2+FY**2))
    U1 = fft.fft2(u1)
    U2 = np.multiply(H,(U1))
    u2 = fft.ifft2((U2))
    return u2

def propIR(u1,step,L,wavel,z) :
    M,N = np.shape(u1)
    k = 2*np.pi/wavel
    x = np.linspace(-L/2.0,L/2.0-step,M)
    y = np.linspace(-L/2.0,L/2.0-step,N)
    X,Y = np.meshgrid(x,y)
    h = (1/(1j*wavel*z))*np.exp(1j*k*(1/(2*z))*(X**2+Y**2))
    H = fft.fft2(fft.fftshift(h))*step*step
    U1 = fft.fft2(fft.fftshift(u1))
    U2 = np.multiply((H),(U1))
    u2 = fft.ifftshift(fft.ifft2(U2))
    return u2
    
def propFF(u1,step,L1,wavel,z):
    M,N = np.shape(u1)
    k = 2*np.pi/wavel
    print(wavel,z,step)
    L2 = wavel*z/step
    step2 = wavel*z/L1
    n = L2/step2 #number of samples
    x2 = np.linspace(-L2/2.0,L2/2.0,n)
    X2,Y2 = np.meshgrid(x2,x2)
    c = 1/(1j*wavel*z)*np.exp(((1j*k)/(2*z))*(X2**2+Y2**2))
    u2 = np.multiply(c,fft.ifftshift(fft.fft2(fft.fftshift(u1))))*step*step
    return u2,L2