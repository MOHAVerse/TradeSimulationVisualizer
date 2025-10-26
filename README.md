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

![Image1](https://github-production-user-asset-6210df.s3.amazonaws.com/47677912/505731149-79c13cf1-f2f4-49c0-8ce1-88ec25d60530.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20251026%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251026T143220Z&X-Amz-Expires=300&X-Amz-Signature=b7ce6486fc90fd262dac6cc2f196857b5fa0f53d612a59cae61c355df8ef9b0a&X-Amz-SignedHeaders=host)


## or build an `.exe` using:
```python
pyinstaller --onefile --noconsole tradesim.pyw
```


## Output Example
- `simulation_result_1023_153200.jpg` (auto-saved chart with results)

![Image2](https://github-production-user-asset-6210df.s3.amazonaws.com/47677912/505731066-1e99c4ef-4b73-4f3c-bf34-71e199d77fd0.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20251026%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251026T143219Z&X-Amz-Expires=300&X-Amz-Signature=d26ea0875c322da512c0aa09a27bf9c13ccbc56df34fc61ac54c031cd8667baf&X-Amz-SignedHeaders=host)


## License
MIT License
