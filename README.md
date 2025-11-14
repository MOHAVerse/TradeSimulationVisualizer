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
```python
python tradesim.pyw
```

## or build an `.exe` using:
```python
pyinstaller --onefile --noconsole tradesim.pyw
```


## Output Example
- `simulation_result_1023_153200.jpg` (auto-saved chart with results)

![Image1](https://media.licdn.com/dms/image/v2/D4D22AQE2h2YdxM_3jg/feedshare-shrink_2048_1536/B4DZog2xZXJAA0-/0/1761487822386?e=1764806400&v=beta&t=qBFcsSSmt9hAYGiTkRzcBS8bRcjFJkT7SyBwy5Bjl0Q)


## License
MIT License
