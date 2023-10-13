from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class TicTacToeGame(GridLayout):
    def __init__(self, **kwargs):
        super(TicTacToeGame, self).__init__(**kwargs)
        self.cols = 3
        self.buttons = [[Button(font_size=40) for _ in range(3)] for _ in range(3)]

        for row in self.buttons:
            for button in row:
                button.bind(on_press=self.on_button_click)
                self.add_widget(button)

        self.current_player = 'X'
        self.game_over = False

    def on_button_click(self, instance):
        if not self.game_over and instance.text == '':
            instance.text = self.current_player
            if self.check_winner():
                print(f'Player {self.current_player} wins!')
                self.game_over = True
            else:
                self.toggle_player()

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if (self.buttons[i][0].text == self.buttons[i][1].text == self.buttons[i][2].text == self.current_player or
                    self.buttons[0][i].text == self.buttons[1][i].text == self.buttons[2][i].text == self.current_player):
                return True
        if (self.buttons[0][0].text == self.buttons[1][1].text == self.buttons[2][2].text == self.current_player or
                self.buttons[0][2].text == self.buttons[1][1].text == self.buttons[2][0].text == self.current_player):
            return True
        return False

    def toggle_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

class TicTacToeApp(App):
    def build(self):
        return TicTacToeGame()

if __name__ == '__main__':
    TicTacToeApp().run()