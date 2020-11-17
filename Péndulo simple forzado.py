# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 21:04:06 2020

@author: carov
"""

from vpython import *
display(title="Pendulo forzado", width=600, height=600, background=color.black)

graph=graph(width=600,height=400,title='<b>Pendulo forzado</b>',
            xtitle='<i>Tiempo (s)</i>',ytitle='<i>Amplitud (m)</i>',
            foreground=color.black, background=color.black)
recorrido = gcurve(graph=graph, color=color.orange)

#Condiciones iniciales
omega_zero=0
theta_zero=pi/4
dt=0.001
tmax=104
g=9.784
l=10
natural=-g/l


pivot=vector(0,0,-10)
esfera=sphere(pos=vector(l*sin(theta_zero),pivot.y-l*cos(theta_zero),-10), radius=0.55, color=color.white)
techo=box(pos=pivot, size=vector(0.5,0.5,0.5), color=color.red)
cuerda=cylinder(pos=pivot, axis=esfera.pos-pivot, radius=0.05, color=color.white)

t=0
Omega=0.02
f=1
F=f*cos(Omega*t) #Forzamiento
gamma=0.5
k=2*gamma #Amortiguamiento
while t < tmax and omega_zero!=Omega: 
  rate(1500) # Homogeneidad de computo
      
  theta_zero+=(omega_zero*dt)
  alpha=(natural*sin(theta_zero))-(k*omega_zero)+F # θ'' + kθ' + g/l sen(θ) = F
  omega_zero+=(alpha*dt)
  
  esfera.pos = vector(l*sin(theta_zero),pivot.y-l*cos(theta_zero),-10) #Posicion nueva
  cuerda.axis = esfera.pos - cuerda.pos # Extremo nuevo
  t+=dt 
  
  recorrido.plot((t, theta_zero))