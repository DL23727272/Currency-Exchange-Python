from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.properties import ObjectProperty
import requests
import subprocess
import os
from database import Database
from kivy.core.window import Window

Builder.load_file('main.kv')


class CurrencyConverterScreen(Screen):
    pass


class CurrencyConverterApp(MDApp):
    db = Database()
    
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
            result_text = f"{amount} {from_currency} equals {converted_amount} {to_currency}"
            self.screen.ids.output_label.text = result_text
            self.db.insert_conversion(from_currency, to_currency, amount, converted_amount)
        except Exception as e:
            self.screen.ids.output_label.text = "Error occurred: " + str(e)
            
    def logout_button(self):
        subprocess.Popen(["python", "login.py"])
        os._exit(0)
        
    def on_stop(self):
        self.db.close_db_connection()
        
if __name__ == "__main__":
    Window.size = (368, 640)
    CurrencyConverterApp().run()
    
