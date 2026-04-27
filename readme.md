# Electrical Tool - Interactive Calculator

An interactive electrical calculator that supports Ohm's Law, Power calculations, and Capacitance calculations with both CLI and GUI interfaces.

## Features

- **Ohm's Law Calculator**: Calculate voltage, current, or resistance (V = I × R)
- **Power Calculator**: Calculate power using various formulas (P = V × I, P = I² × R, etc.)
- **Capacitance/Resistance Calculator**: Calculate equivalent capacitance/resistance in series and parallel configurations
- **Interface**: graphical user interface using Tkinter

## Installation

1. Clone or download the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application
```bash
python FinalProjectElectricalTool.py
```

The application will launch a GUI window. You can also interact via command-line menus.

### Running Tests
```bash
python -m pytest Tests/Tests.py -v
```

## Project Structure

- `FinalProjectElectricalTool.py`: Main application with CLI and GUI
- `Tests/Tests.py`: Unit tests for the calculator functions
- `requirements.txt`: Python dependencies
- `readme.md`: This file