# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 01:31:11 2020

@author: Carolina Valenzuela
"""

from vpython import *
display(title="Pendulo simple", width=600, height=600, background=color.black)

#Condiciones iniciales
t=0
dt=0.001
g=9.784
pivot=vector(0,15,0)
omega=0

Omega=0.02
A=1
F=A*cos(Omega*t) #Forzamiento
k=1 #Amortiguamiento

#Elementos
esfera=sphere(pos=vector(5,0,0), radius=0.5, color=color.blue)
techo=box(pos=pivot, size=vector(0.5,0.5,0.5), color=color.green)
cuerda=cylinder(pos=pivot, axis=esfera.pos-pivot, radius=0.05, color=color.white)

l=mag(esfera.pos-pivot) #Longitud de la cuerda

w = -g/l #Frecuencia natural
theta = acos((pivot.y - esfera.pos.y)/l) #Angulo mov.

while t < 104 and omega!=Omega: 
  rate(1500) # Homogeneidad de computo
      
  theta+=(omega*dt)
  alpha =(w*sin(theta))-(k*omega)+F # θ'' + kθ' + g/l sen(θ) = F
  omega+=(alpha*dt)
  
  esfera.pos = vector(l*sin(theta), pivot.y-l*cos(theta), 0) #Posicion nueva
  cuerda.axis = esfera.pos - pivot # Extremo nuevo
  t+=dt 
