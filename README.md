# Weather App

A simple weather application built using PyQt5 that fetches current weather data for any city using the OpenWeather API.

## Features
- Input city name to get current weather data.
- Displays temperature, weather description, and an emoji representing the temperature.
- Error handling for various scenarios like HTTP errors, timeouts, and connection issues.

## Installation

### Prerequisites
- Python 3.x
- PyQt5
- Requests

### Setup
1. **Clone the repository:**
    ```bash
    git clone https://github.com/Ridham19/weather-app.git
    cd weather-app
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install PyQt5
    pip install requests
    ```

4. **Get your OpenWeather API key:**
   - Sign up at [OpenWeather](https://openweathermap.org/) and get your API key.

5. **Run the application:**
    ```bash
    python main.py
    ```

## Usage
1. Enter the name of the city in the input field.
2. Click on "Get Weather Data".
3. The app will display the current temperature, weather description, and an emoji representing the temperature.

## Code Overview

### `main.py`
The main file that initializes the PyQt5 application and handles fetching and displaying weather data.

#### Functions:
- **`initUI()`**: Sets up the user interface.
- **`get_weather()`**: Fetches weather data from the OpenWeather API.
- **`display_weather(data)`**: Displays weather information.
- **`display_error(message)`**: Displays error messages.

### Example
![Weather App Screenshot](https://raw.githubusercontent.com/Ridham19/Weather-APP/refs/heads/main/Screenshot%202024-10-16%20223455.png)
![Weather App Screenshot](https://github.com/Ridham19/Weather-APP/blob/main/Screenshot%202024-10-16%20223623.png)
![Weather App Screenshot](https://github.com/Ridham19/Weather-APP/blob/main/Screenshot%202024-10-16%20223652.png)



## Acknowledgments
- [OpenWeather](https://openweathermap.org/) for providing the weather data API.
- [PyQt5](https://pypi.org/project/PyQt5/) for the GUI components.

