# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 23:24:21 2020

@author: Laura Viviana A. - Julián D. Osorio
"""
#%gui qt5
from vpython import*

# =============================================================================
# Configuración inicial
# =============================================================================
display(title='Pendulo simple', width=600, height=400,
        background=color.black)

graph=graph(width=645,height=400,title='<b>Pendulo simple</b>',
            xtitle='<i>Tiempo (s)</i>',ytitle='<i>Amplitud (m)</i>',
            foreground=color.black, background=color.black)
recorrido = gcurve(graph=graph, color=color.orange) #Traza el recorrido deseado

# =============================================================================
# condiciones iniciales
# =============================================================================
theta = pi/4 # Angulo inicial
g = 9.784 #gravedad 
t=0 # tiempo inicial
dt = 0.001 #diferencial temporal
pivot=vector(0,0,-10) #vector eje / z -> acerca la imagen
omega = 0.25 # vel angular inicial
l = 15 # longitud como parametro
w = -g/l # frecuencia natural

# =============================================================================
# Sistema referencia cuerda-esfera
# =============================================================================
esfera=sphere(pos=vector(l*sin(theta), pivot.y - l*cos(theta), -10),radius=0.55,color=color.white,make_trail = True, 
              trail_type = 'points',trail_color = color.purple, interval=25, retain=50)

techo=box(pos=pivot, size=vector(0.5,0.5,0.5), color=color.red)
cuerda=cylinder(pos=pivot, axis=esfera.pos - pivot, radius=0.05, color=color.white)


# =============================================================================
# movimiento
# =============================================================================

while t < 104: 
  rate(1500) # Homogeneidad de computo
  
  theta+=(omega*dt)
  alpha = w * sin(theta) # θ'' + g/l sen(θ) = 0
  omega+=(alpha*dt)
  
  esfera.pos = vector(l*sin(theta), -l*cos(theta), -10) # posicion nueva
  cuerda.axis = esfera.pos - cuerda.pos # extremo nuevo
  t+=dt 
  
  recorrido.plot((t, theta)) ###
