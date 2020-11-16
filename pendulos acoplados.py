# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 18:31:46 2020

@author: gabit
"""

from vpython import *
import numpy as np

def pendulo_acoplado(gravedad = 9.8,
                     constante_resorte = 0.1,
                     masa = 0.1,
                     angulo1 = 0,
                     angulo2 = 0.52,
                     longitud = 10,
                     distancia = 10,
                     tiempo_sim = 30             
                     ):

## Constantes y parametros ############################################################
    g = gravedad            # Gravedad
    k = constante_resorte   # Constante de resorte
    m = masa                # Masa de las bolitas
    
    theta1 = angulo1        # ángulo de la primera masa
    theta2 = angulo2        # ángulo de la segunda masa
    
    l = longitud            # Longitud de los pendulos
    d = distancia           # Distancia entre las dos bolitas
    
    T  = tiempo_sim         # Tiempo de simulación
    dt = 0.001              # Delta t
    
    
    x1, y1 =     l* np.sin(theta1), -l* np.cos(theta1) #Coordenadas bolita1
    x2, y2 = d + l* np.sin(theta2), -l* np.cos(theta2) #Coordenadas bolita2
    
    scene = canvas(title = 'Oscilador acoplado',
                   width = 600, height = 400,
                   background = color.black)

## Objetos ######################################################################################################################## 
    techo = box( pos = vector(d/2, 0, 0), size = vector(d + 0.5, 0.5, 0.5),
                color = color.white)
 
    bolita1 = sphere( pos = vector(x1, y1, 0), radius = l*0.1, color = color.orange)
    bolita2 = sphere( pos = vector(x2, y2, 0), radius = l*0.1, color = color.purple)
    
    cuerda1 = cylinder(pos = vector(0, 0, 0), axis = vector(l* np.sin(theta1),
                        -l* np.cos(theta1), 0), radius = 0.05, color = vector(120,100,70))
    cuerda2 = cylinder(pos = vector(d, 0, 0), axis = vector(l* np.sin(theta2),
                        -l* np.cos(theta2), 0), radius = 0.05, color = vector(120,100,70))
    
    resorte = cylinder(pos  = vector(l* np.sin(theta1)/2,-l* np.cos(theta1)/2, 0),
                      axis = vector(d + l* np.sin(theta2)/2 - l* np.sin(theta1)/2,-l* np.cos(theta2)/2 + l* np.cos(theta1)/2, 0),
                      radius = 0.05,
                      color  = color.yellow)

## Gráfica y variables adicionales ######################################################################################################################

    gd = graph( width = 600, height = 300,
                title = '<b>Oscilaciones</b>',
                xtitle = '<i>Tiempo</i>', ytitle = '<i>Theta</i>',
                foreground = color.black, background = color.white)
    
    phase_1 = gcurve( color = color.orange,  label = 'bolita1' )
    phase_2 = gcurve( color = color.purple, label = 'bolita2' )
    
    #Velocidades angulares iniciales
    angular1 = 0
    angular2 = 0
    
    t = 0
## Loop de animación ######################################################################################################################   
    while (t < T):
    
        rate(500)
    
        # Velocidad angular
        angular1 = angular1 + ( -g* np.sin(theta1)/l + k* np.sin(2*(theta2-theta1))/ (8* m) )* dt
        angular2 = angular2 + ( -g* np.sin(theta2)/l - k* np.sin(2*(theta2-theta1))/ (8* m) )* dt
    
        # Ángulo
        theta1 = theta1 + angular1* dt
        theta2 = theta2 + angular2* dt
    
        # Tiempo
        t = t + dt
    
        # Posición bolita1 (y su cuerda)
        bolita1.pos.x =   l* np.sin(theta1)
        bolita1.pos.y = - l* np.cos(theta1)
    
        cuerda1.axis.x =   l* np.sin(theta1)
        cuerda1.axis.y = - l* np.cos(theta1)
    
        # Posición bolita2 (y su cuerda)
        bolita2.pos.x =  l* np.sin(theta2) + d
        bolita2.pos.y =- l* np.cos(theta2)
    
        cuerda2.axis.x =   l* np.sin(theta2)
        cuerda2.axis.y = - l* np.cos(theta2)
    
        # Resorte
        resorte.pos.x  =   l* np.sin(theta1)/2
        resorte.pos.y  = - l* np.cos(theta1)/2
        resorte.axis.x = d + l* np.sin(theta2)/2 - l* np.sin(theta1)/2
        resorte.axis.y =   - l* np.cos(theta2)/2 + l* np.cos(theta1)/2
    
        # Plot del diagrama de fases
        phase_1.plot( pos=(t, theta1) )
        phase_2.plot( pos=(t, theta2) )
        

## Ejemplo del funcionamiento de la función sin especificar parametros ####################################################

pendulo_acoplado()

########################################################################################################
