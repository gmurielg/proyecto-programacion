# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt #Test purpouses
from PIL import ImageDraw,Image #Modificacion y creacion de imagen (respectivamente)

#//////////////////#
#  PENDULO SIMPLE  #
#//////////////////#
"""
Dibujar el pendulo (PIL)
En un tiempo t el pendulo puede ser descrito por un angUlo \theta con la vertical,
la posicion de su pivote (xc,yc) y el largo de su cuerda (L).
Adicionalmente necesitamos el tamaño de la iamgen.
"""
#Dibujo del pendulo en un isntande

def pendulo(Ancho,Alto,L,theta):
    img=Image.new("RGB",(Ancho,Alto))
    Pendulum=ImageDraw.Draw(img)
    xc = Ancho/2
    yc = Alto/2
    x=xc+L*(np.sin(theta))
    y=yc+L*(np.cos(theta))
    Pendulum.line([(xc,yc),(x,y)],(255,2555,255),1)
    Pendulum.ellipse([(x-3,y-3),(x+3,y+3)],(255,0,0))
    return img

#img=pendulo(256,256,70,np.pi/3)
#img.show()

"""
En esta ocasion el problema se abrodara a partir del calculo de la trayectoria del pendulo.
A partir de esta se crearan suficientes imagenes por seguundo para obtener un video de la evolucion del sistema.
Para ello se utilizara un diferencial de tiempo que simulara un tiempo continuo.
-Ecuacion diferencial que modela el sistema: \ddot\theta=-(g/l)sin(\theta) 
-Condiciones inicales \theta_0 y \dot\theta_0
Haciendo uso de la aproximacion: f(x)=f(x+dx)+dx(\dotf(x)):
\theta(t+dt)=\theta(t)+dt(\dot\theta(t))
\dot\theta(t+dt)=dot\theta(t)-(g/l)sin(\theta)
"""
#Calculo del estado del sistema en n(steps) instantes de tiempo

def trayectoria(theta0,dtheta0,steps,dt,L,g=9.8):
    estados=np.zeros((steps,2))
    estados[0,:]=np.array([theta0,dtheta0]) #Estado inicial
    #Ahora el i-esimo elemento de estados correspondera al estado tras el i-esimo step
    for i in range(steps-1):
        estados[i+1,0]=estados[i,0]+dt*estados[i,1] #Nuevo angulo
        estados[i+1,1]=estados[i,1]-g/L*(np.sin(estados[i,0])) #Nueva velocidad
    
    return estados 

#a=trayectoria(np.pi/3,0,1000,0.0001,10)
#plt.plot(a[:,0])
#plt.show()

#usar cv2 y os para generar el video :/
def video(estados,fps,m,l,g=9.8):
    frames=[]
    a=estados.shape[0]
    for i in a:
        theta=estados[i,0]
        dtheta=estados[i,1]
        img=pendulo(256,256,45,theta)
        frames.append(img)
        
#///////////////////////#
#  PENDULO AMORTIGUADO  #
#///////////////////////#
"""
Ecuacion sin aproxiamcion de pequeñas oscilaciones <---Primera opcion
Ecuacion con aproximacion de pequeñas oscialciones (Usar un resorte?)
Mas razonable usar este approach para el pendulo doble y los pendulos acoplados
pues sacamos el potencial de los sitemas de EDO
"""