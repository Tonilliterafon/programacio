"""
Starting Template
Once you have learned how to use classes, you can begin your program with this
template.
If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"


class Personatge(arcade.Sprite):
    def __init__(self,x,y,m):
        self.x = x
        self.y = y
        self.m = m
        self.i = 0
        self.j = 0
        self.colorCos = arcade.color.RED

    def moure(self):
        self.x = self.x + self.i 
        self.y = self.y + self.j

    def pintar(self):
        arcade.draw_circle_filled(self.x,self.y,self.m,self.colorCos)


class Arbre(arcade.Sprite):
    def __init__(self,x,y,m):
        self.x = x
        self.y = y
        self.m = random.randint(10,50)
        self.colorTronc= arcade.color.BROWN
        self.colorCopa= arcade.color.GREEN
        self.estat=0
   
    def pinta(self):
        #arcade.draw_point(x, y, arcade.color.RED, m)
        #arcade.draw_circle_filled(x,y,m/2,arcade.color.GRANNY_SMITH_APPLE)
        self.canviColor()
        arcade.draw_rectangle_filled(self.x,self.y+self.m,self.m/2,self.m*2,self.colorTronc)
        arcade.draw_circle_filled(self.x, self.y+2*self.m, self.m, self.colorCopa)
   
    def canviColor(self):
        #la copa de l'arbre ha de canviar de color
        #de manera aleatòria
        # el green ha d'estar de 200 a 255
        #https://api.arcade.academy/en/latest/arcade.color.html
       
   
        #rgb=(random.randint(0,255) , random.randint(200,255) , random.randint(0,255))           
        self.estat = self.estat +1     
        if self.estat == 1:
            self.colorCopa = (random.randint(0,255) , random.randint(200,255) , random.randint(0,255))
        if self.estat == 60:
            self.colorCopa = (random.randint(0,255) , random.randint(200,255) , random.randint(0,255))
        if self.estat == 120:
            self.estat = 0
     

    def camina(self,v):
        self.x = self.x + v
   
   

class MyGame(arcade.Window):
    """
    Main application class.
    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.llistaArbre=[]
        self.Personatge = Personatge(10,10,10)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
       
        #self.Arbre1=Arbre(100,200,10)
        #self.Arbre2=Arbre(100,100,25)
       
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        for i in self.llistaArbre:
            i.pinta()
        
        self.Personatge.moure()
        self.Personatge.pintar()
        
       
        # Call draw() on all your sprite lists below


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
     
        #hi ha d'haver un canvi de color cada 100 updates.
        pass
    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        
        
        if chr(key) == 'a':
            self.Personatge.i = -5
        if chr(key) == 'd':                     
            self.Personatge.i = 5
        if chr(key) == 'w':
            self.Personatge.j = 5
        if chr(key) == 's':
            self.Personatge.j = -5
        
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        
        if chr(key) == 'a':
            self.Personatge.i = 0
        if chr(key) == 'd':                     
            self.Personatge.i = 0
        if chr(key) == 'w':
            self.Personatge.j = 0
        if chr(key) == 's':
            self.Personatge.j = 0
        
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        self.llistaArbre.append(Arbre(x,y,20))


        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass
   

    #def __init__(self,x,y,m):
        #self.x = x
        #self.y = y
        #self.m = random.randint(10,50)
        #self.colorCopa= arcade.color.RED
        #self.estat=0
   
    #def pinta(self):
        #arcade.draw_point(x, y, arcade.color.RED, m)
        #arcade.draw_circle_filled(x,y,m/2,arcade.color.GRANNY_SMITH_APPLE)
        #self.canviColor()
        #arcade.draw_rectangle_filled(self.x,self.y+self.m,self.m/2,self.m*2,self.colorTronc)
        #arcade.draw_circle_filled(self.x, self.y+2*self.m, self.m, self.colorCopa)
   
    #def canviColor(self):
        #la copa de l'arbre ha de canviar de color
        #de manera aleatòria
        # el green ha d'estar de 200 a 255
        #https://api.arcade.academy/en/latest/arcade.color.html
       
   
     #rgb=(random.randint(0,255) , random.randint(200,255) , random.randint(0,255))    
       
"""
     self.estat = self.estat + 1
     if self.estat == 1:
        self.colorCopa = (random.randint(0,255) , random.randint(200,255) , random.randint(0,255))
     if self.estat == 60:
        self.colorCopa = (random.randint(0,255) , random.randint(200,255) , random.randint(0,255))
     if self.estat == 120:
        self.estat = 0
    

    def camina(self,v):
        self.x = self.x + v

"""   

def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

main()
