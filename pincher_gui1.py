import tkinter as tk
from tkinter import messagebox
import rclpy
import threading
from pincher_control.control_servo import PincherController
from tkinter import PhotoImage


# Posiciones predeterminadas
preset_positions = {
    "Posición 1": [512, 512, 512, 512, 512] ,
    "Posición 2": [582, 582, 568, 454, 512],
    "Posición 3": [412, 610, 426, 596, 512],
    "Posición 4": [753, 454, 667, 582, 512],
    "Posición 5": [738, 412, 667, 383, 512]
}

# Iniciar ROS y el controlador
rclpy.init()
pincher = PincherController()

# Crear ventana principal
ventana = tk.Tk()
img = PhotoImage(file="/home/santiago/ros2_ws/phantom_ws/src/pincher_control/pincher_control/unal_logo.png")
logo = tk.Label(ventana, image=img, bg="#f0f0f0")
logo.image = img  # importante para que no se borre
logo.pack(pady=10)
ventana.title("Interfaz Pincher")
ventana.geometry("500x500")
ventana.configure(bg="#f0f0f0")

# Encabezado
titulo = tk.Label(ventana, text="Robótica 2025-1", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
titulo.pack(pady=(10, 0))

subtitulo = tk.Label(ventana, text="UNAL", font=("Helvetica", 14), bg="#f0f0f0")
subtitulo.pack()

autores = tk.Label(ventana, text="Santiago Camilo Fonseca\nJuan David Medina", font=("Helvetica", 10), bg="#f0f0f0")
autores.pack(pady=(0, 20))

# Función para mover el robot
def mover_a(posicion):
    def _thread():
        pincher.cambioPos(posicion)
    threading.Thread(target=_thread).start()

# Botones para posiciones predeterminadas
label_presets = tk.Label(ventana, text="Posiciones predeterminadas:", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
label_presets.pack()

for nombre, posicion in preset_positions.items():
    boton = tk.Button(ventana, text=nombre, width=30, command=lambda p=posicion: mover_a(p))
    boton.pack(pady=3)

# Entrada de posiciones personalizadas
label_custom = tk.Label(ventana, text="Posición personalizada (5 valores):", font=("Helvetica", 12), bg="#f0f0f0")
label_custom.pack(pady=(20, 5))

entrada = tk.Entry(ventana, width=50)
entrada.pack()
entrada.insert(0, "512,512,512,512,512")

def enviar_personalizado():
    texto = entrada.get()
    try:
        valores = [int(x.strip()) for x in texto.split(',')]
        if len(valores) != 5:
            raise ValueError
        mover_a(valores)
    except:
        messagebox.showerror("Error", "Ingresa 5 números separados por comas")

boton_personalizado = tk.Button(ventana, text="Mover a posición personalizada", command=enviar_personalizado)
boton_personalizado.pack(pady=10)

# Cierre seguro
def cerrar():
    pincher.terminar()
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrar)
ventana.mainloop()
