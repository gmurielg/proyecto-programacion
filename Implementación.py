# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:11:22 2020

<<<<<<< HEAD
@author: Laura Viviana A. - Julián D. Osorio - Gabriel Muriel
=======
@author: gabit
>>>>>>> 8c304802d62858a865f87de96d071a00724e8679
"""

from vpython import *
import numpy as np
import math

#Condiciones iniciales

theta_zero = float(input('Amplitud angular inicial: '))
omega_zero = float(input('Velocidad angular inicial: '))

dt = float(input('Diferencial temporal: '))
tmax = float(input('Tiempo de Oscilación: '))

#Father class
class Pendulo(object):
    
    def __init__ (self, omega_zero, theta_zero, g = 9.784, l=10., tmax = 12, dt = 0.001):
        '''
        Genera el objeto pendulo bajo las condiciones iniciales de movimiento
        Parameters
        ----------
        omega_zero : float
            Velocidad anfular inicial (Enegia cinetica suministrada)
        theta_zero : float
            Amplitud angular inicial en rad.
        g : float, optional
            Gravedad en Bogotá. The default is 9.784.
        l : float, optional
            Longitud de la cuerda. The default is 10.
        tmax : float, optional
            Tiempo máximo de oscilación en segundos. The default is 104.
        dt : float, optional
            Diferencial de tiempo. The default is 0.001.
        Returns
        -------
        None.
        '''
        self.g = g
        self.l = l
        self.omega = omega_zero
        self.t= tmax*10
        self.dt = dt
        self.theta = theta_zero
        self.natural= -g/l
        self.display = display(width=600, height=300,background=color.black)
        
        grapf = graph(width=645,height=400, xtitle='<i>Tiempo (s)</i>',ytitle='<i>Amplitud (m)</i>',foreground=color.black, background=color.black)
        self.recorrido = gcurve(graph=grapf, color=color.orange)
        
    def osc(self):
        raise NotImplementedError
        
    def __str__(self):
        print('Este es un sistema de pendulos acoplados')
  
        
#Children classes
class PenduloLibre(Pendulo):
    
    def __init__ (self, omega_zero, theta_zero, g = 9.784, l=10, tmax = 104, dt = 0.001):
        Pendulo.__init__(self, omega_zero, theta_zero, g = 9.784, l=10, tmax = 104, dt = 0.001)
        
    def osc(self):
        '''
        Genera la animación correspondiene a un pendulo bajo la ecuación
        diferencial de segundo orden para el oscilador armonico simple.
        Returns
        -------
        None.
        
        '''      
        self.display
        
        pivot=vector(0,0,-10)
        esfera=sphere(pos=vector(self.l*sin(self.theta), pivot.y - self.l*cos(self.theta), -10),radius=0.55,color=color.white,make_trail = True, 
                           trail_type = 'points',trail_color = color.purple, interval=25, retain=50)
        techo=box(pos=pivot, size=vector(0.5,0.5,0.5), color=color.red)
        cuerda=cylinder(pos=pivot, axis=esfera.pos - pivot, radius=0.05, color=color.white)
        
        n=0
        while n < self.t: 
          rate(1500) 
          
          self.theta+=(self.omega*self.dt)
          alpha = self.natural * sin(self.theta)
          self.omega+=(alpha*self.dt)
          
          esfera.pos = vector(self.l*sin(self.theta), pivot.y-self.l*cos(self.theta), -10) 
          cuerda.axis = esfera.pos - cuerda.pos 
          n+=self.dt 
          
          self.recorrido.plot((n, self.theta)) 
          
class PenduloAmortiguado(Pendulo):
    
    def __init__ (self, omega_zero, theta_zero,g = 9.784, l=10, tmax = 104, dt = 0.001):
        Pendulo.__init__(self, omega_zero, theta_zero, g = 9.784, l=10, tmax = 104, dt = 0.001)
    
    def osc(self,gamma):
        '''
        Genera la animación correspondiene a un pendulo bajo un factor de decaimiento
        gamma para el oscilador armonico amortiguado.
    
        Returns
        -------
        None.
        
        '''  
        self.display
        
        pivot=vector(0,0,-10)
        esfera=sphere(pos=vector(self.l*sin(self.theta), pivot.y - self.l*cos(self.theta), -10),radius=0.55,color=color.white,make_trail = True, 
                           trail_type = 'points',trail_color = color.purple, interval=25, retain=50)
        techo=box(pos=pivot, size=vector(0.5,0.5,0.5), color=color.red)
        cuerda=cylinder(pos=pivot, axis=esfera.pos - pivot, radius=0.05, color=color.white)
        
        t=0
        while t < self.t:
            
            if self.omega == 0:
                break
                #exit()
                
            rate(1500)
            
            alpha = ( self.natural * sin(self.theta) ) - (gamma * self.omega)
            self.omega+=(alpha*self.dt)
            self.theta+=(self.omega*self.dt) 
           
            esfera.pos = vector(self.l*sin(self.theta), pivot.y-self.l*cos(self.theta), -10)
            cuerda.axis = esfera.pos - cuerda.pos 
            
            t += self.dt 
            
            self.recorrido.plot((t, self.theta)) 
            
        
class PenduloAcoplado(Pendulo):
    def __init__(self, omega_zero, theta_zero,g = 9.784, l=10, tmax = 50, dt = 0.001):
        Pendulo.__init__(self, omega_zero, theta_zero, g = 9.784, l=10, tmax = 50, dt = 0.001)
    
    def osc(self,constante_k, masa, distancia, angulo2):
        
        #Reasignación de variables###
        
        g = self.g              # Gravedad
        k = constante_k                   # Constante de resorte
        m = masa                # Masa de las bolitas
        
        theta1 = self.theta        # ángulo de la primera masa
        theta2 = angulo2
        l = self.l              # Longitud de los pendulos
        d = distancia           # Distancia entre las dos bolitas
            
        T  = self.t              # Tiempo de simulación
        dt = self.dt             # Delta t
            
            
        x1, y1 =     l* np.sin(theta1), -l* np.cos(theta1) #Coordenadas bolita1
        x2, y2 = d + l* np.sin(theta2), -l* np.cos(theta2) #Coordenadas bolita2
            
        self.display
        
        #Objetos a definir
        techo = box( pos = vector(d/2, 0, 0), size = vector(d + 0.5, 0.5, 0.5),
                    color = color.gray(0.3))
     
        bolita1 = sphere( pos = vector(x1, y1, 0), radius = l*0.035, color = color.white, make_trail = True, trail_type ='points', trail_color = color.orange, retain = 50, interval = 25 )
        bolita2 = sphere( pos = vector(x2, y2, 0), radius = l*0.035, color = color.white, make_trail = True, trail_type ='points', trail_color = color.blue, retain = 50, interval = 25 )
        
        cuerda1 = cylinder(pos = vector(0, 0, 0), axis = vector(l* np.sin(theta1),
                            -l* np.cos(theta1), 0), radius = 0.05, color = color.white)
        cuerda2 = cylinder(pos = vector(d, 0, 0), axis = vector(l* np.sin(theta2),
                            -l* np.cos(theta2), 0), radius = 0.05, color = color.white)
        
        resorte = cylinder(pos  = vector(l* np.sin(theta1)/2,-l* np.cos(theta1)/2, 0),
                          axis = vector(d + l* np.sin(theta2)/2 - l* np.sin(theta1)/2,-l* np.cos(theta2)/2 + l* np.cos(theta1)/2, 0),
                          radius = 0.05,
                          color  = color.gray(0.3))
        
        ## Creacíon de la gráfica y variables adicionales############
        gd = graph( width = 600, height = 300,
                title = '<b></b>',
                xtitle = '<i>Tiempo</i>', ytitle = '<i>Amplitud</i>',
                foreground = color.black, background = color.white)
    
        fase1 = gcurve( color = color.orange,  label = 'bolita1' )
        fase2 = gcurve( color = color.blue, label = 'bolita2' )
        
        #Velocidades angulares iniciales
        angular1 = self.omega
        angular2 = self.omega
        
        t = 0
        
        ##Animación
        while (t < T):
    
            rate(1500)
        
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
            fase1.plot( pos=(t, theta1) )
            fase2.plot( pos=(t, theta2) )
            
class PenduloDoble(Pendulo):
    def __init__(self, omega_zero, theta_zero,g = 9.784, l=10, tmax = 50, dt = 0.001):
        Pendulo.__init__(self, omega_zero, theta_zero, g = 9.784, l=10, tmax = 50, dt = 0.001)
    
    def osc(self, masa1, masa2, angulo2, velocidad2):
        l1 = self.l
        l2 = self.l
        g = self.g
        theta1 = self.theta # Angulo interno
        theta2 = angulo2
        m1 = masa1
        m2 = masa2
        mt = m1+m2
        
        punto_apoyo= vector(0,0,-5) # Eje de oscilacion del pendulo
        vel1 = self.omega
        vel2 = velocidad2
        T = self.t
        
        
        # Linea que define el display o canvas
        self.display        
        # Cubo donde se fija el punto de apoyo o eje del pendulo
        techo = box(pos=punto_apoyo,size=vector(0.5,0.5,0.5), color = color.gray(0.3))
       
        # Esfera que cuelga del pendulo
        bolita1 = sphere(
            pos=vector(l1*math.sin(theta1),-l1*math.cos(theta1),-5),
            radius = l1*0.035,
            color = color.white, 
            make_trail = True, 
            trail_type = 'points', 
            trail_color = color.orange, 
            interval=25, 
            retain=50   
            )
        
        bolita2 = sphere(
            pos=vector(l1*math.sin(theta1) + l2*math.sin(theta2),
                       -l1*math.cos(theta1)-l2*math.cos(theta2),
                       -5
                       ),
            radius = l2*0.035,
            color = color.white, 
            make_trail = True, 
            trail_type = 'points', 
            trail_color = color.blue,
            interval=25,
            retain=50
            )
        
        #Objeto del que tiende la masa del pendulo
        cuerda = cylinder(pos=punto_apoyo,
            axis=(bolita1.pos - punto_apoyo),
            radius=0.05, color=color.white
            )
        
        #Objeto del que tiende la segunda masa
        cuerda2 = cylinder(pos=bolita1.pos,
            axis=(bolita2.pos - bolita1.pos),
            radius=0.05, color=color.white
            )
        
        
        t = 0
        dt = self.dt
        cos21 = math.cos(theta2-theta1)
        sin21 = math.sin(theta2-theta1)
        
        cos12 = math.cos(theta1-theta2)
        sin12 = math.sin(theta1-theta2)
    
    
        
        
        #Se crea una grafica de curva de color verde
        gd = graph( width = 600, height = 300,
        title = '<b></b>',
        xtitle = '<i>Tiempo</i>', ytitle = '<i>Amplitud</i>',
        foreground = color.black, background = color.white)
    
        curva1 = gcurve( color = color.orange,  label = 'bolita1' )
        curva2 = gcurve( color = color.blue, label = 'bolita2' )
            
        # Loop que hace que el pendulo se mueva reevaluando su posición durante un tiempo
        while t < T:
            #Número de calculos por segundo que se hacen. Determina velocidad de animacion
            rate(1500)
            
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
            bolita1.pos = vector(l1*math.sin(theta1),-(l1*math.cos(theta1)),-5) 
            
            bolita2.pos = bolita1.pos +vector(l2*math.sin(theta2),-l2*math.cos(theta2),0)
            
            #Reevaluacion del eje sobre el que se crea el cilindro
            cuerda2.pos = (bolita1.pos)
            cuerda2.axis = (bolita2.pos - bolita1.pos)
            cuerda.axis = (bolita1.pos - punto_apoyo) 
            
            t = t + dt #Avance del tiempo
            
            curva1.plot( pos=(t, theta1) )
            curva2.plot( pos=(t, theta2) )

try:
    while True:

        modo = input('Seleccione el sistema a simular.\nSimple:s\nAmortiguado:a\nForzado:f\nDoble:d\nAcoplado:c\n')
    
        if modo == 'l':
            Simple = PenduloLibre(omega_zero, theta_zero)
            Simple.osc()
            break
        
        if modo == 'a':
            gamma = float(input('Asigne un coeficiente de amortiguamiento: ')) 
            Amortiguado = PenduloAmortiguado(omega_zero, theta_zero)
            Amortiguado.osc(gamma)
            break
        
        if modo == 'f':
            Forzado = PenduloForzado()
            Forzado.osc()
            break
        

        if modo == 'c':
            constante_k = float(input('Asigne una constante de resorte: ')) 
            masa = float(input('Asigne una masa para ambos péndulos: '))
            distancia = float(input('Asigne una distancia d entre ambos péndulos: '))
            angulo2 = float(input('Asigne un ángulo para el segundo péndulo: ')) 
            Acoplado = PenduloAcoplado(omega_zero,theta_zero)
            Acoplado.osc(constante_k, masa, distancia, angulo2)
            
        if modo == 'd':
            masa1 = float(input('Asigne una masa para el primer péndulo: ')) 
            masa2 = float(input('Asigne una masa para el segundo péndulo: ')) 
            angulo2 = float(input('Asigne un ángulo para el segundo péndulo: ')) 
            velocidad2 = float(input('Asigne una velocidad inicial para el segundo péndulo: ')) 
            Doble = PenduloDoble(omega_zero,theta_zero)
            Doble.osc(masa1, masa2, angulo2, velocidad2)
        else:
            print('Modo invalido, intente de nuevo')
 
# Este except sirve para ver cual es la variable que falta o que error hay en el try
#except Exception as e: 
    #print(e)
except:
    print('Por favor, defina las variables primero')
##
