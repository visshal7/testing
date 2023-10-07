from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import re


class ChatBotApp(App):
    def build(self):
        self.title = 'ChatBot App'
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.available_keywords_label = Label(
            text="Available keywords: hello",  # Add your keywords here
            size_hint_y=None,
            height=30
        )
        self.layout.add_widget(self.available_keywords_label)

        self.scroll_view = ScrollView()
        self.layout.add_widget(self.scroll_view)

        self.output_label = Label(
            text='ChatBot: Hi! I\'m your personal chatbot. Type \'exit\' to end the conversation.',
            size_hint=(None, None),
            size=(300, 100),
            valign='top'
        )
        self.scroll_view.add_widget(self.output_label)

        self.user_input = TextInput(
            hint_text='You: ',
            size_hint=(None, None),
            size=(300, 44),
            multiline=False
        )
        self.layout.add_widget(self.user_input)

        self.submit_button = Button(
            text='Submit',
            size_hint=(None, None),
            size=(300, 44)
        )
        self.submit_button.bind(on_release=self.process_user_input)
        self.layout.add_widget(self.submit_button)

        return self.layout

    def process_user_input(self, instance):
        user_input = self.user_input.text.strip()
        self.user_input.text = ''

        if user_input.lower() == 'exit':
            self.stop()
            return

        response = self.get_chatbot_response(user_input)
        self.update_output(response)

    def get_chatbot_response(self, user_input):
        # Your chatbot logic goes here
        # You can adapt your existing code for matching keywords and generating responses

        # For demonstration, a simple response is provided
        if user_input.lower() == 'hello':
            return """
DART : NZ region :
DART : NZ region :
GBD_OB_ASSO_F LDATE_
DART : NZ region :
GBD_OB_ASSO_F LDATE_
"""

        return "ChatBot: I'm sorry, I don't understand that."

    def update_output(self, response):
        self.output_label.text += f"\n{response}"


if __name__ == '__main__':
    ChatBotApp().run()
