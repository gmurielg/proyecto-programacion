# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:46:26 2020

@author: Laura Viviana A. - Julián D. Osorio - Gabriel Muriel
"""
from vpython import *

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
    def __init__(self, omega_zero, theta_zero,g = 9.784, l=10, tmax = 104, dt = 0.001):
        Pendulo.__init__(self, omega_zero, theta_zero, g = 9.784, l=10, tmax = 104, dt = 0.001)
    def osc(self):
        
        #Objetos a definir
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
        
        ## Creacíon de la gráfica y variables adicionales############
        gd = graph( width = 600, height = 300,
                title = '<b>Diagrama de fases</b>',
                xtitle = '<i>Theta</i>', ytitle = '<i>Velocidad angular</i>',
                foreground = color.black, background = color.white)
    
        phase_1 = gcurve( color = color.orange,  label = 'bolita1' )
        phase_2 = gcurve( color = color.purple, label = 'bolita2' )
        
        #Velocidades angulares iniciales
        angular1 = 0
        angular2 = 0
        
        t = 0
        
        ##Animación
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
            phase_1.plot( pos=(theta1, angular1) )
            phase_2.plot( pos=(theta2, angular2) )


try:
    while True:
        modo = input('Seleccione el sistema a simular.\nLibre:l\nAmortiguado:a\nForzado:f\n')
    
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
        
        else:
            print('Modo invalido, intente de nuevo')
        
except:
    print('Por favor, defina las variables primero')
            