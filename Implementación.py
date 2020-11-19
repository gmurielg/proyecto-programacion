# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:11:22 2020

<<<<<<< HEAD
@author: Laura Viviana A. - Julián D. Osorio - Gabriel Muriel - Carolina Valenzuela
=======
@author: gabit
>>>>>>> 8c304802d62858a865f87de96d071a00724e8679
"""

from vpython import *
import numpy as np
import math

# =============================================================================
# Pendulos Simples
# =============================================================================

class Simple(object):
    
    def __init__ (self, theta_zero, omega_zero = 0, g = 9.784, l=10., tmax = 10.4, dt = 0.001):
        '''
        Genera el objeto pendulo bajo las condiciones iniciales de movimiento
        Parameters
        ----------
        omega_zero : float, optional
            Velocidad anfular inicial (Enegia cinetica suministrada). The default is 0
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
       
    def osc(self):
        raise NotImplementedError
        
    def __str__(self):
        print('Este es un sistema de pendulo simple')
  
        
#Children classes
class SLibre(Simple):
    
    def __init__ (self, theta_zero, omega_zero = 0, g = 9.784, l=10, tmax = 10.4, dt = 0.001):
        Simple.__init__(self, omega_zero, theta_zero, g = 9.784, l=10, tmax = 104, dt = 0.001)
        
    def osc(self):
        '''
        Genera la animación correspondiene a un pendulo bajo la ecuación
        diferencial de segundo orden para el oscilador armonico simple.
        Returns
        -------
        None.
        
        '''      
        scene = canvas(title = '<b>Pendulo Libre</b>',width = 645, height = 400,
                       background = color.black)
        
        graf=graph(width=645,height=400,title='',
                    xtitle='<i>Tiempo (s)</i>',ytitle='<i>Amplitud (m)</i>',
                    foreground=color.black, background=color.white)
        recorrido = gcurve(graph=graf, label = 'Pendulo', color=color.orange) 
        
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
          
          recorrido.plot((n, self.theta)) 
          
class SAmortiguado(Simple):
    
    def __init__ (self, theta_zero, omega_zero = 0, g = 9.784, l=10, tmax = 10.4, dt = 0.001):
        Simple.__init__(self, omega_zero, theta_zero, g = 9.784, l=10, tmax = 104, dt = 0.001)
    
    def osc(self,gamma):
        '''
        Genera la animación correspondiene a un pendulo bajo un factor de decaimiento
        gamma para el oscilador armonico amortiguado.
    
        Returns
        -------
        None.
        
        '''  
        scene = canvas(title = '<b>Pendulo Amortiguado</b>',width = 645, height = 400,
                       background = color.black)
        
        graf=graph(width=645,height=400,title='',
                    xtitle='<i>Tiempo (s)</i>',ytitle='<i>Amplitud (m)</i>',
                    foreground=color.black, background=color.white)
        recorrido = gcurve(graph=graf, label = 'Pendulo', color=color.orange) 
        
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
            
            recorrido.plot((t, self.theta)) 
            
class SForzado(Simple):
    
    def __init__ (self, theta_zero, omega_zero = 0, g = 9.784, l=10, tmax = 10.4, dt = 0.001):
        Simple.__init__(self, omega_zero, theta_zero, g = 9.784, l=10, tmax = 104, dt = 0.001)
        
    def osc(self,A,Omega,gamma):
        '''
        
        Genera la animación correspondiente a un péndulo sobre el que actúa una fuerza externa sinusoidal 
        cuya amplitud es A y cuya frecuencia es Omega, sometido a un factor de decaimiento gamma.
        
        Returns
        -------
        None.
        
        '''
        scene = canvas(title = '<b>Pendulo Forzado</b>',width = 645, height = 400,
                       background = color.black)
        
        graf=graph(width=645,height=400,title='',
                    xtitle='<i>Tiempo (s)</i>',ytitle='<i>Amplitud (m)</i>',
                    foreground=color.black, background=color.white)
        recorrido = gcurve(graph=graf, label = 'Pendulo', color=color.orange) 
        
        F=A*sin(Omega*self.dt) 
    
        pivot=vector(0,0,-10)
        esfera=sphere(pos=vector(pivot.x + self.l*sin(self.theta), pivot.y - self.l*cos(self.theta),-10), radius=0.55, color=color.white, make_trail = True, trail_type = 'points',trail_color = color.orange, interval=25, retain=50)
        techo=box(pos=pivot, size=vector(0.5,0.5,0.5), color=color.red)
        cuerda=cylinder(pos=pivot, axis=esfera.pos - pivot, radius=0.05, color=color.white)
        
        t=0
        while t < self.t : 
            
            if self.omega!=Omega :
                
                rate(1500) 
                
                self.theta+=(self.omega*self.dt)
                alpha=(self.natural*sin(self.theta)) - (gamma*self.omega) + F
                self.omega+=(alpha*self.dt)
                
                pivot = vector(A*cos(Omega*t), 0, -10)
                techo.pos = pivot
                esfera.pos = vector(pivot.x + self.l*sin(self.theta), pivot.y - self.l*cos(self.theta),-10) 
                cuerda.pos = pivot
                cuerda.axis = esfera.pos - cuerda.pos
                t+=self.dt 
                
                recorrido.plot((t, self.theta))
              
            else:
                continue  
            
            
# =============================================================================
# Doble
# =============================================================================

class PenduloDoble(object):
    
    def __init__(self, omega1 = 0, omega2 = 0, masa1 = 1.25, masa2= 1.25, theta1=pi/3, 
                 theta2=pi/3,g = 9.784, l=10, tmax = 10.4, dt = 0.001):
        
        self.g = g
        self.l = l
        self.omega1 = omega1
        self.omega2 = omega2
        self.t= tmax*10
        self.dt = dt
        self.theta1 = theta1
        self.theta2 = theta2
        self.masa1 = masa1
        self.masa2 = masa2
    
    def osc(self):
        
        l1 = self.l
        l2 = self.l
        g = self.g
        theta1 = self.theta1 # Angulo interno
        theta2 = self.theta2
        m1 = self.masa1
        m2 = self.masa2
        mt = m1+m2
        
        punto_apoyo= vector(0,0,-5) # Eje de oscilacion del pendulo
        vel1 = self.omega1
        vel2 = self.omega2
        T = self.t
        
        
        # Linea que define el display o canvas
        scene = canvas(title = '<b>Pendulo Doble</b>',width = 645, height = 400,
                       background = color.black)     
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
            trail_color = color.blue,
            interval=25,
            retain=500
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
    
        curva1 = gcurve( color = color.orange,  label = 'Pendulo 1' )
        curva2 = gcurve( color = color.blue, label = 'Pendulo 2' )
            
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
            
    def __str__(self):
        print('Este es un sistema de pendulo doble')
            


# =============================================================================
# Acoplados
# =============================================================================

class Acoplados(object):
    
    def __init__(self, theta1, theta2, lo = 9.3, lp = 5, omega1 = 0.,
            omega2 = 0., g = 9.784, tmax= 10.4, dt = 0.001):
        
        self.g = g
        self.omega1 = omega1
        self.omega2 = omega2
        self.t = tmax*10
        self.dt = dt
        self.theta1 = theta1
        self.theta2 = theta2
        self.lo = lo
        self.lp = lp
        self.l = lo + lp
       
    def osc(self):
        raise NotImplementedError
        
    def __str__(self):
        print('Este es un sistema de pendulos acoplados')
 
#Children classes
class AcopleRigido(Acoplados):
    
    def __init__(self, theta1 = pi/3, theta2 = 0, lo = 9.3, lp = 5, omega1 = 0.,
            omega2 = 0., g = 9.784, tmax= 10.4, dt = 0.001):
        
        Acoplados.__init__(self, theta1, theta2, lo, lp, omega1 = 0.,
                           omega2 = 0., g = 9.784, tmax= 10.4, dt = 0.001)
        
    def osc(self):

        scene = canvas(title = '<b>Pendulos por Acople Rigido Libres</b>',width = 645, height = 400,
                       background = color.black)
        
        graf=graph(width=645,height=400,title='<b></b>',
                    xtitle='<i>Tiempo (s)</i>',ytitle='<i>Amplitud (m)</i>',
                    foreground=color.black, background=color.white)
        recorrido1 = gcurve(graph=graf, label = 'Pendulo 1', color=color.orange) 
        recorrido2 = gcurve(graph=graf, label = 'Pendulo 2', color=color.blue)
        
        t_i = 0
                 
        pivot1=vector(-1.15*self.lp,0,-10) 
        pivot2=vector(1.15*self.lp,0,-10)
                
        w = -1/(2*self.lp + self.lo )

        acople = cylinder(pos=vector(pivot1.x, -self.lo, -10), axis= vector(pivot2.x, -self.lo, -10) - vector(pivot1.x, -self.lo, -10), radius=0.1, color=color.gray(0.3))
        
        esfera1=sphere(pos=vector(pivot1.x + self.lp *sin(self.theta1), -self.lo - self.lp*cos(self.theta1), -10),radius=0.55,
                       color=color.white,make_trail = True, 
                       trail_type = 'points',trail_color = color.orange, 
                       interval=25, retain=50)
        esfera2=sphere(pos=vector(pivot2.x + self.lp*sin(self.theta2), -self.lo - self.lp*cos(self.theta2), -10),radius=0.55,
                       color=color.white,make_trail = True, 
                       trail_type = 'points',trail_color = color.blue, 
                       interval=25, retain=50)
        
        techo1=box(pos=pivot1, size=vector(0.5,0.5,0.5), color=color.gray(0.3))
        techo2=box(pos=pivot2, size=vector(0.5,0.5,0.5), color=color.gray(0.3))
        
        cuerda_ac1= cylinder(pos=pivot1, axis=vector(pivot1.x, -self.lo, -10) - pivot1, radius=0.05, color=color.white)
        cuerda_ac2= cylinder(pos=pivot2, axis=vector(pivot2.x, -self.lo, -10) - pivot2, radius=0.05, color=color.white)
        cuerda1=cylinder(pos=vector(pivot1.x, -self.lo, -10), axis=esfera1.pos - vector(pivot1.x, -self.lo, -10), radius=0.05, color=color.white)
        cuerda2=cylinder(pos=vector(pivot2.x, -self.lo, -10), axis=esfera2.pos - vector(pivot2.x, -self.lo, -10), radius=0.05, color=color.white)
    
        alpha1 = 0
        while t_i < self.t: 
          rate(1500) # Homogeneidad de computo
          
          alpha2 = w * (self.lo*alpha1 + 2*self.g*self.theta2)
          alpha1 = w * (self.lo*alpha2 + 2*self.g*self.theta1)
         
          self.theta1+=(self.omega1*self.dt)
          self.theta2+=(self.omega2*self.dt)
          
          self.omega1+=(alpha1*self.dt)
          self.omega2+=(alpha2*self.dt)
          
          esfera1.pos = vector(pivot1.x + self.lp *sin(self.theta1), -self.lo - self.lp*cos(self.theta1), -10) # posicion nueva 
          esfera2.pos = vector(pivot2.x + self.lp *sin(self.theta2), -self.lo - self.lp*cos(self.theta2), -10)
          
          cuerda1.axis = esfera1.pos - cuerda1.pos # extremo nuevo
          cuerda2.axis = esfera2.pos - cuerda2.pos
          t_i+=self.dt 
          
          recorrido1.plot((t_i, self.theta1))
          recorrido2.plot((t_i, self.theta2))
            
        
        
class AcopleResorte(Acoplados):
    
    def __init__(self, theta1 = pi/3, theta2 = 0, lo = 9.3, lp = 5, omega1 = 0.,
            omega2 = 0., g = 9.784, tmax= 10.4, dt = 0.001):
        
        Acoplados.__init__(self, theta1, theta2, lo = 9.3, lp = 5, omega1 = 0.,
                           omega2 = 0., g = 9.784, tmax= 10.4, dt = 0.001)
    
    def osc(self,constante_k, masa, distancia):
        
        #Reasignación de variables###
        
        g = self.g              # Gravedad
        k = constante_k                   # Constante de resorte
        m = masa                # Masa de las bolitas
        
        theta1 = self.theta1        # ángulo de la primera masa
        theta2 = self.theta2
        l = self.l              # Longitud de los pendulos
        d = distancia           # Distancia entre las dos bolitas
            
        T  = self.t              # Tiempo de simulación
        dt = self.dt             # Delta t
            
            
        x1, y1 =     l* np.sin(theta1), -l* np.cos(theta1) #Coordenadas bolita1
        x2, y2 = d + l* np.sin(theta2), -l* np.cos(theta2) #Coordenadas bolita2
            
        scene = canvas(title = '<b>Pendulos por Acople de Resorte Libres</b>',width = 645, height = 400,
                       background = color.black)
        
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
    
        fase1 = gcurve( color = color.orange,  label = 'Pendulo 1' )
        fase2 = gcurve( color = color.blue, label = 'Pendulo 2' )
        
        #Velocidades angulares iniciales
        angular1 = self.omega1
        angular2 = self.omega2
        
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
            

class AcopleAmort(Acoplados):
    
    def __init__(self, theta1 = pi/3, theta2 = 0, lo = 9.3, lp = 5, omega1 = 0.,
            omega2 = 0., g = 9.784, tmax= 10.4, dt = 0.001):
        
        Acoplados.__init__(self, theta1, theta2, lo, lp, omega1 = 0.,
                           omega2 = 0., g = 9.784, tmax= 10.4, dt = 0.001)
        
    def osc(self, gamma):

        scene = canvas(title = '<b>Pendulos Acoplados Amortiguados</b>',width = 645, height = 400,
                       background = color.black)
        
        graf=graph(width=645,height=400,title='<b></b>',
                    xtitle='<i>Tiempo (s)</i>',ytitle='<i>Amplitud (m)</i>',
                    foreground=color.black, background=color.white)
        recorrido1 = gcurve(graph=graf, label = 'Pendulo 1', color=color.orange) 
        recorrido2 = gcurve(graph=graf, label = 'Pendulo 2', color=color.blue)
        
        t_i = 0
                 
        pivot1=vector(-1.15*self.lp,0,-10) 
        pivot2=vector(1.15*self.lp,0,-10)
                
        w = (2*self.lp + self.lo )

        acople = cylinder(pos=vector(pivot1.x, -self.lo, -10), axis= vector(pivot2.x, -self.lo, -10) - vector(pivot1.x, -self.lo, -10), radius=0.1, color=color.gray(0.3))
        
        esfera1=sphere(pos=vector(pivot1.x + self.lp *sin(self.theta1), -self.lo - self.lp*cos(self.theta1), -10),radius=0.55,
                       color=color.white,make_trail = True, 
                       trail_type = 'points',trail_color = color.orange, 
                       interval=25, retain=50)
        esfera2=sphere(pos=vector(pivot2.x + self.lp*sin(self.theta2), -self.lo - self.lp*cos(self.theta2), -10),radius=0.55,
                       color=color.white,make_trail = True, 
                       trail_type = 'points',trail_color = color.blue, 
                       interval=25, retain=50)
        
        techo1=box(pos=pivot1, size=vector(0.5,0.5,0.5), color=color.gray(0.3))
        techo2=box(pos=pivot2, size=vector(0.5,0.5,0.5), color=color.gray(0.3))
        
        cuerda_ac1= cylinder(pos=pivot1, axis=vector(pivot1.x, -self.lo, -10) - pivot1, radius=0.05, color=color.white)
        cuerda_ac2= cylinder(pos=pivot2, axis=vector(pivot2.x, -self.lo, -10) - pivot2, radius=0.05, color=color.white)
        cuerda1=cylinder(pos=vector(pivot1.x, -self.lo, -10), axis=esfera1.pos - vector(pivot1.x, -self.lo, -10), radius=0.05, color=color.white)
        cuerda2=cylinder(pos=vector(pivot2.x, -self.lo, -10), axis=esfera2.pos - vector(pivot2.x, -self.lo, -10), radius=0.05, color=color.white)
    
        alpha1 = 0
        while t_i < self.t: 
          rate(1500) # Homogeneidad de computo
          
          alpha2 = -1/w * (self.lo*alpha1 + gamma*(w*self.omega2 + self.lo*self.omega1) + 2*self.g*self.theta2)
          alpha1 = -1/w * (self.lo*alpha2 + gamma*(w*self.omega1 + self.lo*self.omega2) + 2*self.g*self.theta1)
         
          self.theta1+=(self.omega1*self.dt)
          self.theta2+=(self.omega2*self.dt)
          
          self.omega1+=(alpha1*self.dt)
          self.omega2+=(alpha2*self.dt)
          
          esfera1.pos = vector(pivot1.x + self.lp *sin(self.theta1), -self.lo - self.lp*cos(self.theta1), -10) # posicion nueva 
          esfera2.pos = vector(pivot2.x + self.lp *sin(self.theta2), -self.lo - self.lp*cos(self.theta2), -10)
          
          cuerda1.axis = esfera1.pos - cuerda1.pos # extremo nuevo
          cuerda2.axis = esfera2.pos - cuerda2.pos
          t_i+=self.dt 
          
          recorrido1.plot((t_i, self.theta1))
          recorrido2.plot((t_i, self.theta2))


# =============================================================================
# Implementación
# =============================================================================

try:
    while True:
    
        modo = input('Seleccione el sistema a simular.\nSimple:s\nAcoplado:a\nDoble:d\n')
        
        if modo == 'd':
            print('Determine los parametros de movimento:')
            
            masa1 = float(input('Asigne una masa para el primer péndulo: ')) 
            masa2 = float(input('Asigne una masa para el segundo péndulo: ')) 
            angulo1 = float(input('Asigne un ángulo inicial para el primer péndulo: ')) 
            angulo2 = float(input('Asigne una ángulo inicial para el segundo péndulo: ')) 
            
            Doble = PenduloDoble(0,0, masa1, masa2, angulo1, angulo2)
            Doble.osc()
            break
            
            
        if modo == 's':
            
            tipo = input('Seleccione el tipo de pendulo simple que desee.\nLibre:l\nAmortiguado:a\nForzado:f\n')
            print('Por favor, determine los parametros de sus sistema:')
            
            theta_zero = float(input('Amplitud inicial: '))
            
            if tipo == 'l':
                Libre = SLibre(theta_zero)
                Libre.osc()
                break
            
            elif tipo == 'a':
                gamma = float(input('Asigne un coeficiente de amortiguamiento: ')) 
                Amortiguado = SAmortiguado(theta_zero)
                Amortiguado.osc(gamma)
    
                break
            
            elif tipo == 'f':
                A = float(input('Asignele una amplitud a la Fuerza que incide en el sistema: '))
                Omega = float(input('Determine la frecuenciá de forzamiento: '))
                gamma = float(input('Asigne un coeficiente de amortiguamiento: ')) 
                
                Forzado = SForzado(theta_zero)
                Forzado.osc(A, Omega, gamma)
                break
            
            else:
                print('Tipo invalido, intente de nuevo')
        
        if modo == 'a':
    
            tipo = input('¿Qué tipo de pendulos acoplados desea simular?\nLibre:l\nAmortiguado:a\nForzado:f\n')
            print('Por favor, determine los parametros de sus sistema:')
            
            
            if tipo == 'l':
                acople = input('¿Qué tipo de acople?\nVara Rigida:v\nResorte:r\n')
                print('Por favor, determine los parametros de sus sistema:')
                
                if acople == 'r':
                    constante_k = float(input('Asigne una constante de resorte: ')) 
                    masa = float(input('Asigne una masa para ambos péndulos: '))
                    distancia = float(input('Asigne una distancia d entre ambos péndulos: '))
                    angulo1 = float(input('Asigne un ángulo para el primer péndulo: ')) 
                    angulo2 = float(input('Asigne un ángulo para el segundo péndulo: ')) 
                    
                    Resorte = AcopleResorte(angulo1, angulo2)
                    Resorte.osc(constante_k, masa, distancia)    
                    break
            
                if acople == 'v':
                    theta1 = float(input('Asigne un ángulo para el primer péndulo: ')) 
                    theta2 = float(input('Asigne un ángulo para el segundo péndulo: '))
                    lo = float(input('Asingne la distancia del pivote al acople: '))
                    lp = float(input('Asingne la distancia del acople al los pendulos: '))
                    
                    Rigido = AcopleRigido(theta1, theta2, lo, lp)
                    Rigido.osc()
                    break
                    
            if tipo == 'a':
                theta1 = float(input('Asigne un ángulo para el primer péndulo: ')) 
                theta2 = float(input('Asigne un ángulo para el segundo péndulo: '))
                lo = float(input('Asingne la distancia del pivote al acople: '))
                lp = float(input('Asingne la distancia del acople al los pendulos: '))
                gamma = float(input('Asigne un coeficiente de amortiguamiento: ')) 
                
                Amort = AcopleAmort(theta1, theta2, lo, lp)
                Amort.osc(gamma)
                
                break
              
            
            else:
                print('Tipo invalido, intente de nuevo')
    
        else:
            print('Modo invalido, intente de nuevo')
 
except:
    print('Por favor, defina las variables primero')
    
