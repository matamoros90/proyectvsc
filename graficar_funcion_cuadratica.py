import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.animation as animation

# se importa como plt para crear gráficas
# se importa como np para trabajar con arrays y funciones matemáticas.
# se importa para crear animaciones.

def obtener_valores(): # Esta funcion pide al usuario que introduzca los valores a,b -x, x
    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: "))
    x_min = float(input("Introduce el valor de -X: "))
    x_max = float(input("Introduce el valor de X: "))
    return a, b, x_min, x_max

# Definir la funcion 
def graficar_funcion_cuadratica(a, b, x_min, x_max):
    x = np.linspace(x_min, x_max, 400) # crea un array de 400 puntos entre -x y x
    y = a * x**2 + b

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"y = {a}x^2 + {b}") # calcula los valores de y para la función cuadrática
    bola, = ax.plot([], [], 'o', color='green', markersize=10) #'o' representa que sera una esfera markersize es el tamaño de la esfera y color por logica se sabe que es

# Añadir puntos de referencia
    puntos_x = np.linspace(x_min, x_max, 10) #divide el rango en 10 puntos
    puntos_y = a * puntos_x**2 + b # calcula los valores y correspondientes
    ax.scatter(puntos_x, puntos_y, color='red') # muestra los puntos en la grafica
    for i in range(len(puntos_x)): #añade etiquetas a cada punto
        ax.text(puntos_x[i], puntos_y[i], f"({puntos_x[i]:.2f}, {puntos_y[i]:.2f})", fontsize=9, ha='right')

# Añadir lineas y etiquetas adicionales
    altura_al_suelo = b
    ax.axhline(y=altura_al_suelo, color='blue', linestyle='--', linewidth=0.5) # dibuja una linea horizontal en b para mostrar la altura al suelo
    ax.text(0, altura_al_suelo, f"Altura al suelo: {altura_al_suelo:.2f}", fontsize=12, ha='left', color='blue') # etiqueta esta linea en el eje y

# Configurar la grafica
    # Todas estas lineas configuran el titulo, las etiquetas de los ejes y la cuadrícula de la grafica
    ax.set_title("Gráfica de la Función Cuadrática")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.legend()

# Crear la función de Animación
    def actualizar(frame): #Calcula las posiciones x e y de la bola para cada frame.
        x_pos = [x_min + frame * (x_max - x_min) / 200]  # Convertimos a lista
        y_pos = [a * x_pos[0]**2 + b]  # Convertimos a lista
        bola.set_data(x_pos, y_pos) # actualiza la posición de la bola
        return bola,

# Configurar la animación
    ani = animation.FuncAnimation(fig, actualizar, frames=200, interval=50, blit=True) # Crea la animación con 200 frames y un intervalo de 50 milisegundos entre enllos

    plt.show() # muestra la gráfica animada.

# Función principal
def main(): # obtiene los valores del usuario y llama a la función para graficar la función cuadratica.
    a, b, x_min, x_max = obtener_valores()
    graficar_funcion_cuadratica(a, b, x_min, x_max)

# ejecutar el programa habrir un terminal escribir python graficar_funcion_cuadratica.py enter y listo
if __name__ == "__main__":
    main()
