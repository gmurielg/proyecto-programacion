# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 21:04:06 2020
@author: Carolina Valenzuela - Julián D. Osorio
"""

from vpython import *

def forzado(theta_zero = pi/2, omega_zero=0, Omega=2.75, A=1.5, gamma = 0.05, 
      l=10, g = 9.784, tmax= 129, dt = 0.001):
    '''
    Desarrollo basado en la formulación de la EDO no homogena de segundo orden
	para pendulos forzados.
    Parameters
    ----------
    theta_zero : float, optional
        Angulo. The default is pi/2.
    omega_zero : float, optional
        Velocidad angular. The default is 0.
    Omega : float, optional
        Frecuencia de oscilación forzada. The default is 2.75.
    A : float, optional
        Amplitud del forzamiento. The default is 1.5.
    gamma : float, optional
        Factor decaimiento. The default is 0.05.
    l : float, optional
        Longitud de la cuerda. The default is 10.
    g : float, optional
        gravedad. The default is 9.784.
    tmax : int, optional
        Tiempo oscilación. The default is 104.
    dt : float, optional
        Diferencial de tiempo. The default is 0.001.

    Returns    None.

    '''
    
    
    scene = canvas(title="<b>Pendulo Simple forzado</b>", width=600, height=400, background=color.black)
    
    graf=graph(width=600,height=400,title='',
                xtitle='<i>Tiempo (s)</i>',ytitle='<i>Amplitud (m)</i>',
                foreground=color.black, background=color.white)
    recorrido = gcurve(graph=graf, color=color.orange)
    
    w=-g/l
    F=A*sin(Omega*dt) #Forzamiento
    
    pivot=vector(0,0,-10)
    esfera=sphere(pos=vector(pivot.x + l*sin(theta_zero), pivot.y - l*cos(theta_zero),-10), radius=0.55, color=color.white, 
                  make_trail = True, trail_type = 'points',trail_color = color.orange, interval=25, retain=50)
    techo=box(pos=pivot, size=vector(0.5,0.5,0.5), color=color.red)
    cuerda=cylinder(pos=pivot, axis=esfera.pos-pivot, radius=0.05, color=color.white)
    
    
    
    t=0
    while t < tmax : 
        
        if omega_zero!=Omega :
            
            rate(1500) # Homogeneidad de computo
                
            theta_zero+=(omega_zero*dt)
            alpha=(w*sin(theta_zero)) - (gamma*omega_zero) + F # θ'' + kθ' + g/l sen(θ) = F
            omega_zero+=(alpha*dt)
            
            pivot = vector(A*cos(Omega*t), 0, -10)
            techo.pos = pivot
            esfera.pos = vector(pivot.x + l*sin(theta_zero),pivot.y-l*cos(theta_zero),-10) #Posicion nueva
            cuerda.pos = pivot
            cuerda.axis = esfera.pos - cuerda.pos # Extremo nuevo
            t+=dt 
            
            recorrido.plot((t, theta_zero))
          
        else:
            continue

forzado()
