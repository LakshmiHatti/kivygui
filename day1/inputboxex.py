import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class myGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(myGridLayout, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Name:"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Pizza:"))
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Color:"))
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        self.submit = Button(text="Submit")
        # bind the widget submit button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    def press(self,instance):
        name=self.name.text
        pizza=self.pizza.text
        color=self.color.text
        # print(f"your{name},you like{pizza},and your color{color}")
        self.add_widget(Label(text=f"Hi {name} ,you like{pizza},and your color{color}"))

        # clearing the boxes
        self.name.text=""
        self.pizza.text=""
        self.color.text=""
class MyApp(App):
    def build(self):
        return myGridLayout()

if __name__ == "__main__":
    MyApp().run()
