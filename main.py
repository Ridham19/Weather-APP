import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLabel, QLineEdit,
                             QPushButton, QVBoxLayout)
from  PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather Data", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 800, 800)
        self.setWindowTitle("Weather APP")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")


        self.setStyleSheet("""
                QLabel, QPushButton, QLineEdit {
                    font-family: 'Segoe UI', Georgia, serif;
                    color: #333333;
                }
                QLabel#city_label, QLabel#description_label {
                    font-size: 35px;
                    font-style: italic;
                    margin-bottom: 15px;
                }
                QLineEdit#city_input {
                    font-size: 35px;
                    padding: 10px;
                    margin-bottom: 20px;
                    border: 2px solid #333;
                    border-radius: 5px;
                }
                QPushButton#get_weather_button {
                    font-size: 30px;
                    font-weight: bold;
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                QPushButton#get_weather_button:hover {
                    font-size: 35px;
                    background-color: #45a049;
                }
                QLabel#temperature_label {
                    font-size: 75px;
                    font-weight: bold;
                    margin: 20px 0;
                }
                QLabel#emoji_label {
                    font-size: 100px;
                    margin: 10px 0;
                }
            """)





        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        city_name = self.city_input.text()
#####

      
      
        api_key = "ENTER YOUR API KEY"
# get API key from :      https://openweathermap.org/

      
#####
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city_name,
            'appid': api_key,
            'units': 'metric'  # For temperature in Celsius. Use 'imperial' for Fahrenheit.
        }

        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            if response.status_code == 200:
                weather = data['weather'][0]['description']
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                city = data['name']
                country = data['sys']['country']

                print(f"City: {city}, {country}")
                print(f"Weather: {weather}")
                print(f"Temperature: {temperature}°C")
                print(f"Humidity: {humidity}%")
                print(f"Wind Speed: {wind_speed} m/s")

                self.display_weather(data)
            else:
                print(f"Error: {data['message']}")
                self.display_error(data['message'])
        except requests.exceptions.HTTPError:
            print("HTTP Error")
            self.display_error("HTTP Error")
        except requests.exceptions.Timeout:
            print("Timeout")
            self.display_error("Timeout")
        except requests.exceptions.ConnectionError:
            print("no internet")
            self.display_error("no internet")
        except requests.exceptions.TooManyRedirects:
            print("too may redirects")
            self.display_error("too may redirects")
        except requests.exceptions.RequestException:
            print("Request Error")
            self.display_error("Request Error")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px")
        self.temperature_label.setText(message)

    def display_weather(self, data):
        temp = f"{data['main']['temp']}°C "
        self.temperature_label.setText(temp)
        self.emoji_label.setText(self.display_emoji(data['main']['temp']))

    def display_emoji(self, temp):
        if 20 > temp:
            return "🥶"
        elif 20 < temp <= 30:
            return "😊"
        elif 30 < temp <= 40:
            return "🥵"
        elif temp >= 40:
            return "🔥"
        else:
            return "⁉️"



if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
