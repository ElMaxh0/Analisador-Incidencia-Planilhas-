#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyautogui
import time
import pandas as pd
import easygui
import plotly.express as px

gtable=[]
geraltb=[]
resultg=[]
result=[]
resultg1=[]
sresult=[]
resulta1=[]
arquivo="C://Caminho_DO_ARQUIVO"

dados = pd.read_excel(arquivo)

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    
    return l

elementscontrol=[]
i=0
gkey = remove_repetidos(dados)
print('Colunas Encontradas ')
print(gkey)
print('')
print('Total de vezes / Valor / Coluna')
for ae1 in gkey:
    ng =(remove_repetidos(dados[ae1]))
    ngc= len(ng)
    resulta1.append(ngc)
for g in gkey:
    ng =remove_repetidos(dados[g])
    print('')
    print('Resposta Na Coluna ',g)
    print('')
    for g1 in ng:
        print((dados[dados[g] == g1].count()[2]),'/ ',g1 , '/ ', g)
        resultg1.append(g1)
        result.append((dados[dados[g] == g1].count()[2]))
for aa in resulta1 :
    nhtable=[]
    sresult=[]
    srcount=len(sresult)
    print(sresult)
    while i < 0:
        value=result[i],'/',resultg1[i]
        nhtable.append(value)
        i=i+1
    nhsum=nhtable.sum()
    nhcount=nhtable.count()
    datav=(nhsun/nhcount)
    print (datav)


# In[ ]:

