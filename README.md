# Proyecto programación
Este es un repositorio en el cual se desarrollaran uno o varios proyectos simples de programación en Python.

# Primer proyecto - Exploración de la simulación de péndulos en vpython

En este primer proyecto de la clase de "Programación e introducción a los métodos numéricos", se pretende ahondar en el estudio del movimiento oscilatorio del péndulo generando un camino constructivo desde el movimiento fundamental del oscilador armónico por medio de simulaciones, utilizando el lenguaje de Python. Se han empleado diversas herramientas, tanto de librerías ya desarrolladas de este mismo lenguaje como diferentes modelos matemáticos y gráficas, para así tener la capacidad de comprobar la dificultad que puede llegar a tener el movimiento de los péndulos.

## Pre-requisitos 📋
Todas las simulaciones se han llevado a cabo con el uso de la libreria _vpython_, y algunas de las mismas requieren de _math_ y _matplotlib_, así que se recomienda el descargar estas librerias en _cmd_.

### Instalación 🔧
Se recomienda utilizar Spyder (donde no es necesario descargar math) y fácilmente se pueden descargar las librerías requeridas por Anaconda Prompt  con los siguientes códigos:

```
conda install -c vpython vpython
conda install -c conda-forge matplotlib
```

## Ejecutando las pruebas ⚙️
En _Implementación.py_ se encontrarán todas las simulaciones creadas, en donde el usuario tendrá la opción de escoger el tipo de péndulo que desea simular y así mismo, la libertad de ingresar las condiciones iniciales que desee (sin embargo, los parámetros son opcionales, cada variable ya posee valores por defecto).

### Paso a paso 🚀

I.	Si se desea simular un _péndulo simple_ el usuario tendrá que: 
    1.	Ingresar el comando “s”
    2.	Seleccionar si quiere que este sea péndulo simple libre (con el comando       “Libre”), péndulo simple amortiguado (con el comando “Amortiguado”) o péndulo simple forzado (con el comando “Forzado”).
    3.	Determinar los parámetros del sistema según la elección previa.
II.	Si se desea simular péndulos acoplados el usuario tendrá que:
    1.	Ingresar el comando “a”
    2.	Responder a la pregunta con “Libre” si se desea simular un sistema de péndulos acoplados simple.
        - Posterior a esto tendrá que elegir si desea que su acople sea por medio de una  “Vara rígida” o un “Resorte” (así como se encuentra dentro de las comillas)
        - Asignar los parámetros correspondientes
    3.	Si se desea simular un péndulo acoplado amortiguado, tendrá que elegir “Amortiguado” y si este quiere que sea péndulo acoplado forzado, se tendrá que elegir “Forzado” y asignar los parámetros correspondientes.

### Analice las pruebas 🔩
El usuario puede probar que si ingresa algún comando que no se encuentra definido en cualquiera de las opciones o los parámetros ingresados no corresponden con el tipo de variable, se encontrará con un error y así como el programa lo sugiere, tendrá que volver a intentarlo.

# Autores ✒️
  Laura Viviana Alfonso Diaz  
  Gabriel Muriel    
  Julián D. Osorio    
  Felipe Ospina Suarez   
  Carolina Valenzuela  


