from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.properties import ObjectProperty
import requests

Builder.load_file('main.kv')


class CurrencyConverterScreen(Screen):
    pass


class CurrencyConverterApp(MDApp):
    def build(self):
        self.screen = CurrencyConverterScreen()
        return self.screen

    def convert_currency(self):
        from_currency = self.screen.ids.currency1_field.text.upper()
        to_currency = self.screen.ids.currency2_field.text.upper()
        amount = self.screen.ids.amount_field.text

        try:
            response = requests.get(
                f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
            )
            data = response.json()
            converted_amount = data['rates'][to_currency]
            self.screen.ids.output_label.text = f"{amount} {from_currency} equals {converted_amount} {to_currency}"
        except Exception as e:
            self.screen.ids.output_label.text = "Error occurred: " + str(e)


if __name__ == "__main__":
    CurrencyConverterApp().run()
    
