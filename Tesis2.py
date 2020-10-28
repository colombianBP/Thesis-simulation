#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import random as rn
import pandas as pd
import math as mt


# In[ ]:


#Entradas

#Poblacion total de bacterias
n=100

#Taza de mutacion por plasmido
u=0.1

#Constant hill coeficient
h=5

#Repression coheficient distribution
#Improve
start=10
end=108
kdist=[]
count=1
mean=67
down=False
for i in range(end-start):
    k=i+10
    for j in range(count):
        kdist.append(k)
    if(count<mean and down==False):
        count=count+1
    else:
        count=count-2
        down=True
        


# In[ ]:


def mutantesPorPob(n,k):
    global u
    mutantes=[]
    nexp=(27.93*mt.exp(-h)+1.652)*k
    nplas=np.random.binomial(nexp,u,n)
    if sum(nplas==0):
        return(mutantes)
    for i in nplas:
        if(i!=0):
#             ka=rn.choice(kdist)
#             ca=((0.029*h)-0.036)*mt.log(k/ka)
#             r=1-ca
#             if(r**nexp<=0 or r**nexp==1):
#                 continue
#             pfix=(1-(1/r))/(1-(1/(r**nexp)))
#             if(rn.random()<=pfix):
#                 mutantes.append(ka)
            
            generado=False
            for j in range(i):
                ka=rn.choice(kdist)
                ca=((0.029*h)-0.036)*mt.log(k/ka)
                r=1-ca
                if(r**nexp<=0 or r**nexp==1):
                    continue
                pfix=(1-(1/r))/(1-(1/(r**nexp)))
                if(rn.random()<=pfix):
                    #print('mutante no confirmado')
                    generado=True
                    mutante=ka
                    break
        if(generado==True):
            #print(mutante)
            mutantes.append(mutante)
    return(mutantes)


# In[ ]:


#Condiciones iniciales
poblacion=[5,n-5]
ks=[rn.choice(kdist),rn.choice(kdist)]
print(poblacion)
print(ks)
Spoblacion=[]
Sks=[]


# In[ ]:


#Ciclo
for w in range(200000):
    #Reproduccion
    part=[]
    cas=[]
    for i in range(len(poblacion)):
        nmean=poblacion[i]*27.93*mt.exp(-h)*ks[i]
        #Improve
        ca=nmean*748000/4600000
        cas.append(ca)
    ptotal=sum(np.multiply(cas,poblacion))
    #ponderada= [i/ptotal for i in poblacion]
    ponderada=[]
    for i in range(len(poblacion)):
        ponderada.append(poblacion[i]*cas[i]/ptotal)
        
        
    part=[]
    for i in range(len(poblacion)):
        if(i>=1):
            part.append(part[i-1]+ponderada[i])
        else:
            part.append(ponderada[i])
            
    part[-1]=1 
    prob=rn.random()
    cont=0
    for i in part:
        if (prob<=i):
            poblacion[cont]=poblacion[cont]+1
            break
        cont+=1

    #Muerte
    part=[]
    total=sum(poblacion)
    for i in range(len(poblacion)):
        if(i>=1):
            part.append(part[i-1]+(poblacion[i]/total))
        else:
            part.append(poblacion[i]/total)
    
    part[-1]=1
    prob=rn.random()
    cont=0
    for i in part:
        if (prob<=i):
            poblacion[cont]=poblacion[cont]-1
            break
        cont+=1
    #Mutacion
    for i in range(len(poblacion)):
        mutantes=mutantesPorPob(poblacion[i],ks[i])
        if(mutantes!=[]):
            for j in mutantes:
                #print(j)
                poblacion[i]=poblacion[i]-1
                poblacion.append(1)
                ks.append(j)
    #Save
    Spoblacion.append(poblacion)
    Sks.append(ks)
#     #Delete
#     while(0 in poblacion):
#         ks.pop(poblacion.index(0))
#         poblacion.pop(poblacion.index(0))


# In[ ]:


for i in range(1):
    print(i)


# In[ ]:


poblacion


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




