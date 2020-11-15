# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:08:37 2020

@author: Gabriel Muriel
"""
#%gui qt5
from vpython import * # Libreria que permite crear objetos 3D de manera sencilla
import math


#Funcion que muestra un pendulo en movimiento sin fricción
def pendulo_doble(longitud_pendulo1,
            amplitud_inicial1, #Angulo en radianes
            longitud_pendulo2,
            amplitud_inicial2,
            masa1 = 3,
            masa2 = 3,
            gravedad = 9.8,
            velocidad_inicial1 = 0,
            velocidad_inicial2 = 0,
            tiempo_max = 100, # Tiempo en segundos
            mostrar_grafica = True,
            radio_bolita1 = 3,
            radio_bolita2 = 3,
            color_pendulo1 = vector(1,1,1),
            color_pendulo2 = vector(1,0,0),
            ):
    
    
    #Definiendo las variables localmente
    l1 = longitud_pendulo1
    l2 = longitud_pendulo2
    theta1 = amplitud_inicial1 # Angulo interno
    theta2 = amplitud_inicial2
    m1 = masa1
    m2 = masa2
    mt = m1+m2
    punto_apoyo= vector(0,0,-10) # Eje de oscilacion del pendulo
    color_p = color_pendulo1
    color_p2 = color_pendulo2 #Color de la bolita del pendulo
    g = gravedad
    vel1 = velocidad_inicial1
    vel2 = velocidad_inicial2
    tmax = tiempo_max*10
    
    
    # Linea que define el display o canvas
    display(width=600, height=600, background=(0,0,0)) 
    
    # Cubo donde se fija el punto de apoyo o eje del pendulo
    techo = box(pos=punto_apoyo,size=vector(1,1,1))
   
    # Esfera que cuelga del pendulo
    bolita1 = sphere(
        pos=vector(l1*math.sin(theta1),-l1*math.cos(theta1),-10),
        radius = radio_bolita1,
        color = color_p, 
        shininess=0, 
        make_trail = False, 
        trail_type = 'points', 
        trail_color = color.red, 
        interval=25, 
        retain=30   
        )
    
    bolita2 = sphere(
        pos=vector(l1*math.sin(theta1) + l2*math.sin(theta2),
                   -l1*math.cos(theta1)-l2*math.cos(theta2),
                   -10
                   ),
        radius = radio_bolita2,
        color = color_p2, 
        shininess=0, 
        make_trail = False, 
        trail_type = 'curve', 
        trail_color = color.white, 
        )
    
    #Objeto del que tiende la masa del pendulo
    cuerda = cylinder(pos=punto_apoyo,
        axis=(bolita1.pos - punto_apoyo),
        radius=0.1, color=vector(120,100,70)
        )
    
    #Objeto del que tiende la segunda masa
    cuerda2 = cylinder(pos=bolita1.pos,
        axis=(bolita2.pos - bolita1.pos),
        radius=0.1, color=vector(120,100,70)
        )
    
    
    t = 0
    dt = 0.005
    cos21 = math.cos(theta2-theta1)
    sin21 = math.sin(theta2-theta1)
    
    cos12 = math.cos(theta1-theta2)
    sin12 = math.sin(theta1-theta2)


    
    
    #Se crea una grafica de curva de color verde
    grafica = gcurve(color=color.green)
        
    # Loop que hace que el pendulo se mueva reevaluando su posición durante un tiempo
    while t < tmax:
        #Número de calculos por segundo que se hacen. Determina velocidad de animacion
        rate(1000)
        
        # Aceleracion angular
            #Partes de la ecuación
        pa = -m2*l2*vel2**2*sin12-mt*g*math.sin(theta1)
        pb = m2*l2*cos12
        pc = (l1*vel1**2*sin12-g*math.sin(theta2))/l2  
        pd = mt*l1
        pe = l1/l2*cos12
        
        angular1 = (pa-pb*pc)/(pd-pb*pe)
        
        angular2 = pc-pe*angular1
        
        vel1 = vel1 + angular1*dt # Velocidad angular
        
        vel2 = vel2 + angular2*dt
        
        theta1 = theta1 + vel1*dt # Reevaluacion del ángulo interno del pendulo
        theta2 = theta2 + vel2*dt
       
        #Reevaluacion de la posicion de cada bolita
        bolita1.pos = vector(l1*math.sin(theta1),-(l1*math.cos(theta1)),-10) 
        
        bolita2.pos = bolita1.pos +vector(l2*math.sin(theta2),-l2*math.cos(theta2),0)
        
        #Reevaluacion del eje sobre el que se crea el cilindro
        cuerda2.pos = (bolita1.pos)
        cuerda2.axis = (bolita2.pos - bolita1.pos)
        cuerda.axis = (bolita1.pos - punto_apoyo) 
        
        t = t + dt #Avance del tiempo
       
        if mostrar_grafica:
            #Se va plotteando la grafica creada
            grafica.plot((theta2, theta1))

#Ejemplo de un pendulo doble    
pendulo_doble(10, math.pi, 10, 0.01, 5, 5,9.8,0,0,60,True,1,1,color.purple,color.orange)

