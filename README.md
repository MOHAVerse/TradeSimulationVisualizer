# TradeSimulationVisualizer
A Python-based trading simulator with adjustable parameters, equity curve visualization, and statistical summaries.

A simple Python app to simulate trading strategies with customizable parameters.  
It calculates performance over multiple runs and visualizes the average, best, and worst equity curves.

## Features
- Adjustable inputs for capital, risk, winrate, and RR ratios  
- Tracks max drawdown and win/loss streaks  
- Generates a summary and chart automatically  
- Saves results as timestamped JPG images  
- GUI-based, no command line required

## Requirements
Python 3.10+  
Libraries: `numpy`, `matplotlib`, `tkinter` (built-in)

## Run the app
python tradesim.pyw

## or build an `.exe` using:
pyinstaller --onefile --noconsole tradesim.pyw

## Output Example
- `simulation_result_1023_153200.jpg` (auto-saved chart with results)

## License
MIT License
