from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class TicTacToeBoard(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.x_o = True
        self.flag = 0
        self.winner = False
        self.buttons = []
        
        for _ in range(9):
            button = Button(
                text='',
                font_size='40sp',
                background_color=(0.18, 0.77, 0.71, 1),
                background_normal='',
                size_hint=(1, 1)
            )
            button.bind(on_press=self.button_click)
            self.buttons.append(button)
            self.add_widget(button)

    def button_click(self, button):
        if button.text == '' and not self.winner:
            button.text = 'X' if self.x_o else 'O'
            self.x_o = not self.x_o
            self.flag += 1
            self.check_winner()

    def check_winner(self):
        wins = [(0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6)]
        
        for w in wins:
            if self.buttons[w[0]].text == self.buttons[w[1]].text == self.buttons[w[2]].text != '':
                self.winner = True
                self.show_popup(f'Player {self.buttons[w[0]].text} Wins!')
                return
                
        if self.flag == 9:
            self.show_popup('Match Draw!')

    def show_popup(self, text):
        popup = Popup(
            title='Game Over',
            content=Label(text=text),
            size_hint=(0.75, 0.25)
        )
        popup.open()

class TicTacToeApp(App):
    def build(self):
        return TicTacToeBoard()

if __name__ == '__main__':
    TicTacToeApp().run()
