# Cinemtica-Directa-Phantom-X


Se desarrollo un codigo que permite a traves de una interfaz grafica, elegir 5 posiciones predeterminadas para el manipulador Phantom X Pincher, ademas tambien permite ingresar los valores de posicion de las articulaciones para llegar a una Pose personalizada.

Para el desarrollo de dicho codigo se hace uso de dos modulos, el primero es "pincher_gui1.py", el cual  permite controlar el brazo robótico desde una interfaz gráfica creada con tkinter y a traves de esta elegir usar posiciones predeterminadas o personalizadas.

El segundo modulo es "control_servo.py", el cual es la clase usada dentro de "pincher_gui1.py" para conectar y controlar el manipulador, este codigo permite inicializar y configurar los servomotores, mover el manipulador a posiciones específicas a traves de los valores de las articulaciones deseados, ademas de poder leer la posición actual de los servos y realizar un apagado seguro del sistema.

Las principales funciones usadas son:
  1. __init__(self)
  Propósito:
  Constructor de la clase PincherController. Inicializa el nodo de ROS 2, establece parámetros, configura la comunicación con los servos, Configura torque, velocidad y posición objetivo para cada servo. y los mueve a una posición inicial.

  2. terminar(self)
  Propósito:
  Apaga los servos, cierra la comunicacion y cierra el sistema de forma segura.

  3. cambioPos(self, newPos)
  Propósito:
  Cambia la posición del brazo robótico a una nueva configuración de posiciones (lista de 5 valores), a traves de actualizar self.goal_positions, este cambio se realiza un servo a la vez hasta finalizar la configuracion y muestra en la consola los valores de cada servo.

Diagrama de flujo del funcionamiento del programa:
<img width="3840" height="2829" alt="Diagrama de flujo-Lab4" src="https://github.com/user-attachments/assets/8ad69666-2e1c-4486-8269-7ed241091839" />






[![Watch the video](https://img.youtube.com/vi/Ux1G4xT9eyA/maxresdefault.jpg)](https://youtube.com/shorts/Ux1G4xT9eyA?si=BwozMbiXwo5YeY_l)

### [Ver funcionamiento del pincher](https://youtu.be/Ux1G4xT9eyA)
