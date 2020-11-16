# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:23:43 2020

@author: Julián D. Osorio
"""

from vpython import*


def angular(theta1 = pi/3, theta2 = 0, lp = 5, lo = 9.3, omega1 = 0.,
            omega2 = 0., g = 9.784, tmax= 104, dt = 0.001):
    '''
    Forma 1.
    Coordenadas generelazidas: θ_1, θ_2
    Modelo basado en la formulación bajo metodos de Mecanica Newtoniana; ecuación de fuerza
    de las EDO acopladas en función del angulo que describen el movimiento de los pendulos

    Parameters
    ----------
    theta1 : float, optional
        Angulo inicial p_1 . The default is pi/3.
    theta2 : float, optional
        Angulo inicial p_2. The default is 0.
    lp : float, optional
        Longitud pendulo - acople. The default is 5.
    lo : float, optional
        Longitud acople - pivote. The default is 9.3.
    omega1 : float, optional
        Velocidad angular inicial p_1. The default is 0..
    omega2 : float, optional
        Velocidad angular inicial p_2. The default is 0..
    g : float, optional
        gravedad. The default is 9.784.
    tmax : int, optional
        Tiempo oscilación. The default is 104.
    dt : float, optional
        Diferencial de tiempo. The default is 0.001.

    Returns    None.
    
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
    
    t_i = 0
    
    l = lp+lo
     
    pivot1=vector(-1.15*lp,0,-10) 
    pivot2=vector(1.15*lp,0,-10)
    
    alpha1 = 0.
    alpha2 = 0.
    
    w = -1/2*lp + lo 

    # =============================================================================
    # Sistema referencia acople-cuerda-esfera
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
    
    while t_i < tmax: 
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
      t_i+=dt 
      
      recorrido1.plot((t_i, theta1))
      recorrido2.plot((t_i, theta2))


def amplitud(x1 = 4., x2 = 0.1, lp = 5, lo = 9.3, A = 1.5, B = 1.5,
            phi2 = 0, phi1 = 0, g = 9.784, tmax= 104, dt = 0.001):
    '''
    Forma 2.
    Coordenadas generelazidas: x_1, x_2
    Modelo basado en la solución de las EDO acopladas en función de la amplitud
    bajo el uso del metodo de diagonalización matricial, para obtener los 2 modos
    normales de oscilación con sus frecuencias normales respectivas, cuya superposición
    describe el movimiento de ambas particulas acopladas.

    Parameters
    ----------
    x1 : float, optional
        Amplitud inicial p_1. The default is 4..
    x2 : float, optional
        Amplitud inicial p_2. The default is 0.1.
    lp : float, optional
        Longitud pendulo - acople. The default is 5.
    lo : float, optional
        Longitud acople - pivote. The default is 9.3.
    A : TYPE, optional
        Amplitud modo 1. The default is 1.5.
    B : TYPE, optional
        Amplitud modo 2. The default is 1.5.
    phi1 : TYPE, optional
        Desface modo 1. The default is 0.
    phi2 : TYPE, optional
         Desface modo 2. The default is 0.
    g : float, optional
        gravedad. The default is 9.784.
    tmax : int, optional
        Tiempo oscilación. The default is 104.
    dt : float, optional
        Diferencial de tiempo. The default is 0.001.

    Returns  None.
    
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
    
    t_i = 0
    
    l = lp+lo
    
    theta1 = acos(x1/lp)
    theta2 = acos(x2/lp)
       
    y1 = tan(theta1)*x1
    y2 = tan(theta2)*x2
    
    pivot1=vector(-1.15*lp,0,-10) 
    pivot2=vector(1.15*lp,0,-10)
    
    wn1 = sqrt(g/l)
    wn2 = sqrt(g/lp)
    
    # =============================================================================
    # Sistema referencia acople-cuerda-esfera
    # =============================================================================
    acople = cylinder(pos=vector(pivot1.x, -lo, -10), axis= vector(pivot2.x, -lo, -10) - vector(pivot1.x, -lo, -10), radius=0.1, color=color.red)
    
    esfera1=sphere(pos=vector(pivot1.x + x1, -lo - y1, -10),radius=0.55,
                   color=color.white,make_trail = True, 
                   trail_type = 'points',trail_color = color.purple, 
                   interval=25, retain=50)
    esfera2=sphere(pos=vector(pivot2.x + x2, -lo - y2, -10),radius=0.55,
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
    
    while t_i < tmax: 
      rate(1500) # Homogeneidad de computo
      
      x2 = A*cos(wn1*dt + phi1) - B*cos(wn2*dt + phi2)
      x1 = A*cos(wn1*dt + phi1) + B*cos(wn2*dt + phi2)
      
      theta1 = acos(x1/lp)
      theta2 = acos(x2/lp)
      
      y1 = tan(theta1)*x1
      y2 = tan(theta2)*x2
      
      esfera1.pos = vector(pivot1.x + x1, -lo - y1, -10) # posicion nueva
      esfera2.pos = vector(pivot2.x + x2, -lo - y2, -10)
      
      cuerda1.axis = esfera1.pos - cuerda1.pos # extremo nuevo
      cuerda2.axis = esfera2.pos - cuerda2.pos
      t_i+=dt 
      
      recorrido1.plot((t_i, x1))
      recorrido2.plot((t_i, x2))
      
angular()
#amplitud()
