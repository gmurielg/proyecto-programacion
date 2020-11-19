# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:23:43 2020

@author: Laura Viviana A. - Julián D. Osorio
"""

from vpython import*


def angular(theta1 = pi/3, theta2 = 0, lp = 9.3, lo = 5, omega1 = 0.,
            omega2 = 0., g = 9.784, tmax= 104, dt = 0.001):
    '''
    Forma libre
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
    scene = canvas(title='<b>Pendulos Acoplados amortiguados<b>', width=600, height=400,
            background=color.black)
    
    graf=graph(width=645,height=400,title='<b></b>',
                xtitle='<i>Tiempo (s)</i>',ytitle='<i>Amplitud (m)</i>',
                foreground=color.black, background=color.white)
    recorrido1 = gcurve(graph=graf, label = 'Pendulo 1', color=color.orange) #Traza el recorrido deseado
    recorrido2 = gcurve(graph=graf, label = 'Pendulo 2', color=color.blue)
    
    t_i = 0
    
    l = lp+lo
     
    pivot1=vector(-1.05*lp,0,-10) 
    pivot2=vector(1.05*lp,0,-10)
    
    w = -1/(2*lp + lo )

    # =============================================================================
    # Sistema referencia acople-cuerda-esfera
    # =============================================================================
    acople = cylinder(pos=vector(pivot1.x, -lo, -10), axis= vector(pivot2.x, -lo, -10) - vector(pivot1.x, -lo, -10), radius=0.1, color=color.red)
    
    esfera1=sphere(pos=vector(pivot1.x + lp *sin(theta1), -lo - lp*cos(theta1), -10),radius=0.55,
                   color=color.white,make_trail = True, 
                   trail_type = 'points',trail_color = color.orange, 
                   interval=25, retain=50)
    esfera2=sphere(pos=vector(pivot2.x + lp*sin(theta2), -lo - lp*cos(theta2), -10),radius=0.55,
                   color=color.white,make_trail = True, 
                   trail_type = 'points',trail_color = color.blue, 
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
    
    alpha1 = 0
    while t_i < tmax: 
      rate(1500) # Homogeneidad de computo
      
      alpha2 = w * (lo*alpha1 + 2*g*theta2)
      alpha1 = w * (lo*alpha2 + 2*g*theta1)
      
      theta1+=(omega1*dt)
      theta2+=(omega2*dt)
      
      omega1+=(alpha1*dt)
      omega2+=(alpha2*dt)
      
      esfera1.pos = vector(pivot1.x + lp *sin(theta1), -lo - lp*cos(theta1), -10) # posicion nueva 
      esfera2.pos = vector(pivot2.x + lp *sin(theta2), -lo - lp*cos(theta2), -10)
      
      cuerda1.axis = esfera1.pos - cuerda1.pos # extremo nuevo
      cuerda2.axis = esfera2.pos - cuerda2.pos
      t_i+=dt 
      
      recorrido1.plot((t_i, theta1))
      recorrido2.plot((t_i, theta2))


def amort(gamma = 0.05, theta1 = pi/2, theta2 = 0, lp = 9.3, lo = 5, omega1 = 0.,
          omega2 = 0., g = 9.784, tmax= 104, dt = 0.001):
    '''
    Forma amortiguada
    Coordenadas generelazidas: θ_1, θ_2
    Modelo basado en la formulación bajo metodos de Mecanica Newtoniana; ecuación de fuerza
    de las EDO acopladas en función del angulo que describen el movimiento de los pendulos,
    considerando una accíon de amortiguamiento proporcional a la velocidad.

    Parameters
    ----------
    gamma : float, optional
        Coeficiente decaimiento. The default is 0.05.
    
    theta1 : float, optional
        Angulo inicial p_1 . The default is pi/3.
    theta2 : float, optional
        Angulo inicial p_2. The default is 0.
    lp : float, optional
        Longitud pendulo - acople. The default is 5.
    lo : float, optional
        Longitud acople - pivote. The default is 9.3.
    omega1 : float, optional
        Velocidad angular inicial p_1. The default is 0
    omega2 : float, optional
        Velocidad angular inicial p_2. The default is 0
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
    scene = canvas(title='<b>Pendulos Acoplados amortiguados<b>', width=600, height=400,
            background=color.black)
    
    graf=graph(width=645,height=400,title='<b></b>',
                xtitle='<i>Tiempo (s)</i>',ytitle='<i>Amplitud (m)</i>',
                foreground=color.black, background=color.white)
    recorrido1 = gcurve(graph=graf, label = 'Pendulo 1', color=color.orange) #Traza el recorrido deseado
    recorrido2 = gcurve(graph=graf, label = 'Pendulo 2', color=color.blue)
    
    t_i = 0
    
    l = lp+lo
     
    pivot1=vector(-1.05*lp,0,-10) 
    pivot2=vector(1.05*lp,0,-10)
        
    k = (2*lp + lo)

    # =============================================================================
    # Sistema referencia acople-cuerda-esfera
    # =============================================================================
    acople = cylinder(pos=vector(pivot1.x, -lo, -10), axis= vector(pivot2.x, -lo, -10) - vector(pivot1.x, -lo, -10), radius=0.1, color=color.red)
    
    esfera1=sphere(pos=vector(pivot1.x + lp *sin(theta1), -lo - lp*cos(theta1), -10),radius=0.55,
                   color=color.white,make_trail = True, 
                   trail_type = 'points',trail_color = color.orange, 
                   interval=25, retain=50)
    esfera2=sphere(pos=vector(pivot2.x + lp*sin(theta2), -lo - lp*cos(theta2), -10),radius=0.55,
                   color=color.white,make_trail = True, 
                   trail_type = 'points',trail_color = color.blue, 
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
    
    alpha1 = 0
    omega1 = 0
    omega2 = 0
    while t_i < tmax: 
      rate(1500) # Homogeneidad de computo
      
      alpha2 = -1/k * (lo*alpha1 + gamma*(k*omega2 + lo*omega1) + 2*g*theta2)
      alpha1 = -1/k * (lo*alpha2 + gamma*(k*omega1 + lo*omega2) + 2*g*theta1)
      
      theta1+=(omega1*dt)
      theta2+=(omega2*dt)
      
      omega1+=(alpha1*dt)
      omega2+=(alpha2*dt)
      
      esfera1.pos = vector(pivot1.x + lp *sin(theta1), -lo - lp*cos(theta1), -10) # posicion nueva 
      esfera2.pos = vector(pivot2.x + lp *sin(theta2), -lo - lp*cos(theta2), -10)
      
      cuerda1.axis = esfera1.pos - cuerda1.pos # extremo nuevo
      cuerda2.axis = esfera2.pos - cuerda2.pos
      t_i+=dt 
      
      recorrido1.plot((t_i, theta1))
      recorrido2.plot((t_i, theta2))
      
def forz(gamma = 0.05, forzada1 = 2.55,  forzada2 = 1.25, theta1 = pi/2, theta2 = 0, A = 1.5, lp = 9.3, 
         lo = 5, omega1 = 0.,omega2 = 0., g = 9.784, tmax= 104, dt = 0.001):
    '''
    Forma forzada
    Coordenadas generelazidas: θ_1, θ_2
    Modelo basado en la formulación bajo metodos de Mecanica Newtoniana; ecuación de fuerza
    de las EDO acopladas no homogeneas, en función del angulo que describen el movimiento de los pendulos,
    considerando una accíon de amortiguamiento proporcional a la velocidad, en donde el primer pendulo
    es sometido a la acción de una fuerza sinusoidal.

    Parameters
    ----------
    gamma : float, optional
        Coeficiente decaimiento. The default is 0.05.
    
    theta1 : float, optional
        Angulo inicial p_1 . The default is pi/3.
    theta2 : float, optional
        Angulo inicial p_2. The default is 0.
    lp : float, optional
        Longitud pendulo - acople. The default is 5.
    lo : float, optional
        Longitud acople - pivote. The default is 9.3.
    omega1 : float, optional
        Velocidad angular inicial p_1. The default is 0
    omega2 : float, optional
        Velocidad angular inicial p_2. The default is 0
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
    scene = canvas(title='<b>Pendulos Acoplados Forzados<b>', width=600, height=400,
            background=color.black)
    
    graf=graph(width=645,height=400,title='<b></b>',
                xtitle='<i>Tiempo (s)</i>',ytitle='<i>Amplitud (m)</i>',
                foreground=color.black, background=color.white)
    recorrido1 = gcurve(graph=graf, label = 'Pendulo 1', color=color.orange) #Traza el recorrido deseado
    recorrido2 = gcurve(graph=graf, label = 'Pendulo 2', color=color.blue)
    
    t_i = 0
    
    l = lp+lo
     
    pivot1=vector(-1.05*lp,0,-10) 
    pivot2=vector(1.05*lp,0,-10)
        
    k = (2*lp + lo)
    
    F1 = A*sin(forzada1*dt)
    F2 = A*sin(forzada2*dt)
    
    # =============================================================================
    # Sistema referencia acople-cuerda-esfera
    # =============================================================================
    acople = cylinder(pos=vector(pivot1.x, -lo, -10), axis= vector(pivot2.x, -lo, -10) - vector(pivot1.x, -lo, -10), radius=0.1, color=color.red)
    
    esfera1=sphere(pos=vector(pivot1.x + lp *sin(theta1), -lo - lp*cos(theta1), -10),radius=0.55,
                   color=color.white,make_trail = True, 
                   trail_type = 'points',trail_color = color.orange, 
                   interval=25, retain=50)
    esfera2=sphere(pos=vector(pivot2.x + lp*sin(theta2), -lo - lp*cos(theta2), -10),radius=0.55,
                   color=color.white,make_trail = True, 
                   trail_type = 'points',trail_color = color.blue, 
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
    
    alpha1 = 0
    omega1 = 0
    omega2 = 0
    while t_i < tmax: 
      rate(1500) # Homogeneidad de computo
      
      alpha2 = (-1/k * (lo*alpha1 + gamma*(k*omega2 + lo*omega1) + 2*g*theta2)) + F2
      alpha1 = (-1/k * (lo*alpha2 + gamma*(k*omega1 + lo*omega2) + 2*g*theta1)) + F1
      
      theta1+=(omega1*dt)
      theta2+=(omega2*dt)
      
      omega1+=(alpha1*dt)
      omega2+=(alpha2*dt)
      
      pivot1 = vector(-1.05*lp + F1, 0, -10)
      techo1.pos = pivot1
      acople.pos = vector(pivot1.x, -lo, -10)
      cuerda_ac1.pos =  pivot1
      cuerda_ac1.axis = vector(pivot1.x, -lo, -10) - pivot1
      
      pivot2 = vector(1.05*lp + F2, 0, -10)
      techo2.pos = pivot2
      cuerda_ac2.pos =  pivot2
      cuerda_ac2.axis = vector(pivot2.x, -lo, -10) - pivot2

      
      acople.axis = vector(pivot2.x, -lo, -10) - vector(pivot1.x, -lo, -10)
      
      esfera1.pos = vector(pivot1.x + lp *sin(theta1), -lo - lp*cos(theta1), -10) # posicion nueva 
      esfera2.pos = vector(pivot2.x + lp *sin(theta2), -lo - lp*cos(theta2), -10)
      
      cuerda1.pos = vector(pivot1.x, -lo, -10)
      cuerda1.axis = esfera1.pos - cuerda1.pos
      cuerda2.pos = vector(pivot2.x, -lo, -10)
      cuerda2.axis = esfera2.pos - cuerda2.pos
      
      t_i+=dt 
      
      recorrido1.plot((t_i, theta1))
      recorrido2.plot((t_i, theta2))

      
angular()
amort() 
#forz()
