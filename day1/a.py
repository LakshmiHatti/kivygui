import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class myGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(myGridLayout, self).__init__(**kwargs)
        self.cols = 1
        # Create a second gridlayout
        # Set default size of cols and rows
        self.row_force_default=True
        self.row_default_height=120
        self.col_force_default=True
        self.col_default_width=100
        # Create a second gridlayout
        self.top_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=100
            )
		# Set number of columns in our new top_grid
        self.top_grid.cols = 2


		# Add widgets
        self.top_grid.add_widget(Label(text="Name: "))
		# Add Input Box
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name)
        self.top_grid.add_widget(Label(text="Favorite Pizza: "))
		# Add Input Box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)
        self.top_grid.add_widget(Label(text="Favorite Color: "))
		# Add Input Box
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)
		# Add the new top_grid to our app
        self.add_widget(self.top_grid) 

        self.submit = Button(text="Submit")
        # bind the widget submit button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    def press(self,instance):
        name=self.name.text
        pizza=self.pizza.text
        color=self.color.text
        # print(f"your{name},you like{pizza},and your color{color}")
        self.op_grid.add_widget(Label(text=f"Hi {name} ,you like{pizza},and your color{color}"))

        # clearing the boxes
        self.name.text=""
        self.pizza.text=""
        self.color.text=""
class MyApp(App):
    def build(self):
        return myGridLayout()

if __name__ == "__main__":
    MyApp().run()
