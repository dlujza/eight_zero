# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 17:24:10 2017

@author: Lujza Daoud 
"""
import sys
import math
import networkx
import numpy as np
import skimage.color as color 
import skimage.io as io 
np.set_printoptions(threshold=np.inf)

kepek_test1 = color.rgb2gray(io.imread('eight3.png'))
kepek_test2 = color.rgb2gray(io.imread('zero2.png'))
kepek_expanded1 = np.expand_dims(kepek_test1,axis=0)
kepek_expanded2 = np.expand_dims(kepek_test2,axis=0)    #now shape (1,28,28)
print (kepek_expanded.shape)
x1 = np.reshape(kepek_expanded1,(1,784))
x1=np.array(np.concatenate(x1))

x2 = np.reshape(kepek_expanded2,(1,784)) 
x2=np.array(np.concatenate(x2))


def kepek_mashogy(kep):
    index=0
    lista=[]
    for i in kep:
        if (i==1):
            print("o")
            lista.append(index)
        index+=1
    print(lista)
    index=0
    for i in kep:
        if index in lista:
            kep[index]+=10
        index+=1
    return kep
    
def vane_X(): #korbejar egy X-et (eloszor \ majd a / szarat)
    X=[]
    oszlop=1
    sor=28
    i=(28*9)+10
    X.append(i)
    #while (i==((28*15)+(3*28/4+1))):
    for a in range(0,10):
        i+=oszlop+sor
        X.append(i)
        #print ("h")
    oszlop=-oszlop
    j=(28*9)+18
    X.append(j)
    #while (j==(28*15)+(28/4+1)):
    for b in range(0,10):
        #print ("f")
        j+=oszlop+sor
        X.append(j)
    X=[int(x) for x in X]
    return X

def ertekadas_X(X_vektor):
    filter=np.zeros(784)
    #print (filter)
    index=0
    for i in filter:
        if index in X_vektor:
            #print("s")
            i=i+5
            #print (i)
            filter[index]+=5
            #print (filter)
        index+=1
    return filter
    
x1=kepek_mashogy(x1)
x2=kepek_mashogy(x2)
print (x1)
X_vektor=vane_X()
print (X_vektor)
filter_vektor=ertekadas_X(X_vektor)
#print (valami)
filter_vektor = np.array(filter_vektor)

kep_01=np.dot(x1,filter_vektor)
kep_02=np.dot(x2, filter_vektor)
print(kep_01)
print(kep_02)

#print(valami.shape)
    



       
                