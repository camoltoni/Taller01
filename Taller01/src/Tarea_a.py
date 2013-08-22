#coding=utf-8
'''
Created on 22/08/2013

@author: admin2
'''
# Primero debemos importar la "biblioteca" cocos
# que nos provee de funcionalidades gráficas
# y prestaciones específicas de videojuegos
import cocos.layer
# A continuación creamos una "clase"
# que hereda de la clase Layer (capa)
# de cocos, es un contenedor al que le
# agregamos los elementos visuales
# que vamos a representar
class HelloWorld(cocos.layer.Layer):
    # La función init se ejecuta para inicializar
    # la clase recibe el parámetro self que es una
    # instancia de si misma
    def __init__(self):
        # Siempre al iniciar una layer debo invocar
        # el constructor de la clase padre
        super(HelloWorld, self).__init__()

# Indica cual es el punto de entrada para la
# función "main"    
if __name__ == '__main__':
    # Clase principal de cocos
    # manejará la ventana del juego y las escenas
    cocos.director.director.init()
    # Creo una "instancia" de mi clase HelloWorld
    # que será la capa principal de dibujo
    hello_layer = HelloWorld()
    # Creo la escena a representar asignándole
    # la capa previamente creada
    main_scene = cocos.scene.Scene(hello_layer)
    # Le ordeno al director que "corra"
    # con la escena principal
    cocos.director.director.run(main_scene)
    
'''
NOTA FINAL
El impresionante resultado de nuestro programa es...
una ventana negra en pantalla, no parece muy emocionante
agreguemosle un poco de emoción a la siguiente tarea
con algo de texto.
'''