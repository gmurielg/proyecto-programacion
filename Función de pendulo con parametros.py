# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 07:45:36 2020

@author: gabit
"""

from vpython import * # Libreria que permite crear objetos 3D de manera sencilla
import math


#Funcion que muestra un pendulo en movimiento sin fricción
def pendulo(longitud_pendulo,
            amplitud_inicial, #Angulo en radianes
            gravedad = 9.8,
            velocidad_inicial = 0,
            resistencia = 0.01,
            tiempo_max = 100, # Tiempo en segundos
            mostrar_grafica = True,
            radio_bolita = 3,
            color_pendulo = vector(1,1,1),
            ):
    
    
    
    l = longitud_pendulo
    theta = amplitud_inicial # Angulo interno desde la linea vertical hasta la posicion actual
    punto_apoyo= vector(0,0,-10) # Eje de oscilacion del pendulo
    color_p = color_pendulo #Color de la bolita del pendul
    g = gravedad
    vel = velocidad_inicial
    tmax = tiempo_max*10
    
    # Linea que define el display o canvas
    display(width=600, height=600, background=(0,0,0)) 
    
    # Cubo donde se fija el punto de apoyo o eje del pendulo
    techo = box(pos=punto_apoyo,size=vector(1,1,1))
   
    # Esfera que cuelga del pendulo
    bolita = sphere(
        pos=vector(l*math.sin(theta),punto_apoyo.y-l*math.cos(theta),-10),
        radius = radio_bolita,
        color = color_p, 
        shininess=0, 
        make_trail = True, 
        trail_type = 'points', 
        trail_color = color.red, 
        interval=25, 
        retain=30   
        )
    
    #Objeto del que tiende la masa del pendulo
    cuerda = cylinder(pos=punto_apoyo,
        axis=(bolita.pos - punto_apoyo),
        radius=0.1, color=vector(120,100,70)
        ) 
    t = 0
    dt = 0.01
    
    #Se crea una grafica de curva de color verde
    grafica = gcurve(color=color.green)
        
    # Loop que hace que el pendulo se mueva reevaluando su posición durante un tiempo
    while t < tmax:
        #Número de calculos por segundo que se hacen. Determina velocidad de animacion
        rate(1000)
        
        # Aceleracion angular
        accl_angular = -g/l*math.sin(theta) - resistencia*vel
        
        vel = vel+accl_angular*dt # Velocidad angular
        
        theta = theta + vel*dt # Reevaluacion del ángulo interno del pendulo
       
        #Reevaluacion de la posicion bolita 
        bolita.pos = vector(l*math.sin(theta),punto_apoyo.y-(l*math.cos(theta)),-10) 
        
        #Reevaluacion del eje sobre el que se crea el cilindro
        cuerda.axis = (bolita.pos - punto_apoyo) 
        
        t = t + dt #Avance del tiempo
       
        if mostrar_grafica:
            #Se va plotteando la grafica creada con puntos en los ejes de tiempo y angulo
            grafica.plot((t, theta))

# Ejemplo de un pendulo con parametros especificos
pendulo(100,0.8,)


