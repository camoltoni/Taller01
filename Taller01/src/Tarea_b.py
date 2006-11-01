#coding=utf-8
'''
Created on 22/08/2013

@author: admin2
'''
import cocos.layer
class HelloWorld(cocos.layer.Layer):
    def __init__(self, width, height):
        super(HelloWorld, self).__init__()
        label = cocos.text.Label("Hola a todos!",x=width/2, y=height/2,width=800)
        self.add(label)

if __name__ == '__main__':
    WIDTH = 800
    HEIGHT = 600
    cocos.director.director.init(width = WIDTH, height = HEIGHT)
    hello_layer = HelloWorld(WIDTH, HEIGHT)
    main_scene = cocos.scene.Scene(hello_layer)
    cocos.director.director.run(main_scene)
    
'''
NOTA FINAL
'''