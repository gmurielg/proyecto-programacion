# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:23:43 2020

@author: Julián D. Osorio
"""

from vpython import*

'''
Forma 1.
Coordenadas generelazidas: θ_1, θ_2
Modelo basado en la formulación bajo metodos de Mecanica Newtoniana; ecuación de fuerza
de las EDO acopladas en función del angulo que describen el movimiento de los pendulos
'''

# =============================================================================
# Configuración inicial
# =============================================================================
display(title='Pendulos Acoplados libres', width=600, height=400,
        background=color.black)

graf=graph(width=645,height=400,title='<b>Pendulos Acoplados libres</b>',
            xtitle='<i>Tiempo (s)</i>',ytitle='<i>Amplitud (m)</i>',
            foreground=color.black, background=color.white)
recorrido1 = gcurve(graph=graf, color=color.orange) #Traza el recorrido deseado
recorrido2 = gcurve(graph=graf, color=color.blue)

# =============================================================================
# condiciones iniciales
# =============================================================================
lp = 5
lo = 9.3
l = lp+lo

theta1 = pi/3 # Angulo inicial
theta2 = 0

g = 9.784 #gravedad 
t=0 # tiempo inicial
dt = 0.001 #diferencial temporal

pivot1=vector(-1.15*lp,0,-10) #vector eje / z -> acerca la imagen
pivot2=vector(1.15*lp,0,-10)

omega1 = 0. # vel angular inicial
omega2 = 0.
alpha1 = 0.
alpha2 = 0.

w = -1/2*lp + lo 

# =============================================================================
# Sistema referencia cuerda-esfera
# =============================================================================
acople = cylinder(pos=vector(pivot1.x, -lo, -10), axis= vector(pivot2.x, -lo, -10) - vector(pivot1.x, -lo, -10), radius=0.1, color=color.red)

esfera1=sphere(pos=vector(pivot1.x + lp *sin(theta1), -lo - lp*cos(theta1), -10),radius=0.55,
               color=color.white,make_trail = True, 
               trail_type = 'points',trail_color = color.purple, 
               interval=25, retain=50)
esfera2=sphere(pos=vector(pivot2.x + lp*sin(theta2), -lo - lp*cos(theta2), -10),radius=0.55,
               color=color.white,make_trail = True, 
               trail_type = 'points',trail_color = color.green, 
               interval=25, retain=50)

techo1=box(pos=pivot1, size=vector(0.5,0.5,0.5), color=color.red)
techo2=box(pos=pivot2, size=vector(0.5,0.5,0.5), color=color.red)

cuerda_ac1= cylinder(pos=pivot1, axis=vector(pivot1.x, -lo, -10) - pivot1, radius=0.05, color=color.white)
cuerda_ac2= cylinder(pos=pivot2, axis=vector(pivot2.x, -lo, -10) - pivot2, radius=0.05, color=color.white)
cuerda1=cylinder(pos=vector(pivot1.x, -lo, -10), axis=esfera1.pos - vector(pivot1.x, -lo, -10), radius=0.05, color=color.white)
cuerda2=cylinder(pos=vector(pivot2.x, -lo, -10), axis=esfera2.pos - vector(pivot2.x, -lo, -10), radius=0.05, color=color.white)


# =============================================================================
# movimiento
# =============================================================================

while t < 104: 
  rate(1500) # Homogeneidad de computo
  
  theta1+=(omega1*dt)
  theta2+=(omega2*dt)
  
  aplpha2 = w * (lo*alpha1 + 2*g*theta2)
  alpha1 = w * (lo*alpha2 + 2*g*theta1)
  
  omega1+=(alpha1*dt)
  omega2+=(alpha2*dt)
  
  esfera1.pos = vector(pivot1.x + lp *sin(theta1), -lo - lp*cos(theta1), -10) # posicion nueva 
  esfera2.pos = vector(pivot2.x + lp *sin(theta2), -lo - lp*cos(theta2), -10)
  
  cuerda1.axis = esfera1.pos - cuerda1.pos # extremo nuevo
  cuerda2.axis = esfera2.pos - cuerda2.pos
  t+=dt 
  
  recorrido1.plot((t, theta1))
  recorrido2.plot((t, theta2))
