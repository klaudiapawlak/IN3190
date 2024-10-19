import numpy as np
import matplotlib.pyplot as plt

#Oppgave 1A
def konvin3190(h,x,ylen):

    """
    konvin3190 konvolverer to signaler
    konvin3190(h,x,ylen) konvolverer de to vektor-signalene h og x.
    Dersom ylen = 0 er utgangssignalet lengde "len(x)", mens hvis ylen
    er 1 har utgangssignalet lengde "len(h)+len(x)-1"
    """

    x_len = len(x)
    h_len = len(h)

    if ylen == 1:
        y = np.zeros(x_len+y_len-1)
        for i in range(h_len):
            for j in range(x_len):
                k = j+i-1
                y[k] = y[k]+h[i]*x[j] #Konvolusjon

    if ylen == 0:
        y = np.zeros(x_len)
        for i in range(h_len):
            for j in range(x_len-h_len+1):
                k=i+j-1
                y[k] = y[k]+h[i]*x[j] #Konvolusjon

    return y

#Oppgave 1B
def frekspekin3190(x,N,fs):

    """
    frekspekin3190 regner ut frekvensresponsen til et signal
    x,g = frekspekin3190(x,N,fs) regner ut frekvensresponsen til
    signalet x med samplingfrekvens fs for N punkter på enhetssirkelen
    I tillegg til frekvensspekteret X returnerer funksjonen også tilhørende
    frekvens f
    """

    x_len = len(x)
    X = np.zeros((N),dtype = "complex_")
    fp = np.linspace(0,1,N)
    f = fp*fs

    for i in range(N):
        for j in range(x_len):
            X[i] = X[i]+x[j]*np.exp(2*np.pi*-1j*fp[i]*j)

    return X,f

#Oppgave 1C
f1 = 10
f2 = 20
fs = 100
t_len = 5

t = np.linspace(0,t_len,t_len*fs+1)
h = [0.2,0.2,0.2,0.2,0.2] #FIR filter
N = 1000
x = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)

Xh,fh = frekspekin3190(h,N,fs)
Xx,fx = frekspekin3190(x,N,fs)
Xy,fy = frekspekin3190(konvin3190(h,x,0),N,fs)

plt.plot(fh,abs(Xh))
plt.title('Frekvensspekter av h')
plt.xlabel('Frekvens')
plt.ylabel('Amplitude')
plt.show()

plt.subplot(211);
plt.plot(fy,abs(Xy))
plt.title('Frekvensspekter av y')
plt.xlabel('Frekvens')
plt.ylabel('Amplitude')

plt.subplot(212);
plt.plot(fx,abs(Xx))
plt.title('Frekvensspekter av x')
plt.xlabel('Frekvens')
plt.ylabel('Amplitude')
plt.show()
