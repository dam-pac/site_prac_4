import random
import arcade
import arcade.gui
WIDTH = 1024
HEIGHT = 1024
class GamePause(arcade.Window):
    def __init__(self, width,height):
        super().__init__()
        #self.sound_click = arcade.Sound('Sounds/Click.mp3')
        #self.box = arcade.gui.UIBoxLayout()
        #self.manage = arcade.gui.UIManager()
        #self.manage.enable()
        #self.contgame = contgame
        #self.box = arcade.gui.GUILayout()
        arcade.set_background_color(arcade.color.AMAZON)
        #self.start_button = arcade.gui.UIFlatButton(text='Start Window')
        #self.box.add(self.start_button.with_space_around(bottom=20))
        #self.proceed_button = arcade.gui.UIFlatButton(text='Proceed')
        #self.box.add(self.proceed_button.with_space_around(bottom=20))
    def on_draw(self):
        arcade.start_render()
    def on_update(self, delta_time: float):
        pass
def main():
    game = GamePause(WIDTH,HEIGHT)
    arcade.run()
main()
