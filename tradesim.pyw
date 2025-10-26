import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import os
import sys
import subprocess

def run_simulation():
    try:
        # --- READ USER INPUTS ---
        initial_capital = float(entry_capital.get())
        risk_percent = float(entry_risk.get()) / 100
        num_trades = int(entry_trades.get())
        num_runs = int(entry_runs.get())
        winrate = float(entry_winrate.get()) / 100

        rr_choices = [float(x.strip()) for x in entry_rrs.get().split(",")]
        rr_probs = [float(x.strip()) for x in entry_probs.get().split(",")]

        if len(rr_choices) != len(rr_probs):
            messagebox.showerror("Error", "RRs and probabilities count must match.")
            return
        if not np.isclose(sum(rr_probs), 1.0):
            messagebox.showerror("Error", "Probabilities must sum to 1.0.")
            return

        # --- SIMULATION CORE ---
        def simulate_run():
            capital = initial_capital
            equity_curve = []
            win_streak = 0
            loss_streak = 0
            max_win_streak = 0
            max_loss_streak = 0

            for _ in range(num_trades):
                rr = np.random.choice(rr_choices, p=rr_probs)
                risk = capital * risk_percent
                reward = risk * rr
                win = np.random.rand() < winrate
                profit = reward if win else -risk
                capital += profit
                equity_curve.append(capital)

                if win:
                    win_streak += 1
                    loss_streak = 0
                else:
                    loss_streak += 1
                    win_streak = 0

                max_win_streak = max(max_win_streak, win_streak)
                max_loss_streak = max(max_loss_streak, loss_streak)

            equity = np.array(equity_curve)
            peak = np.maximum.accumulate(equity)
            drawdown = (equity - peak) / peak
            max_drawdown = np.min(drawdown) * 100

            return {
                "equity_curve": equity,
                "final_capital": capital,
                "max_drawdown": max_drawdown,
                "max_win_streak": max_win_streak,
                "max_loss_streak": max_loss_streak
            }

        # --- RUN ALL SIMULATIONS ---
        all_runs = [simulate_run() for _ in range(num_runs)]
        all_equities = np.array([r["equity_curve"] for r in all_runs])
        average_equity = np.mean(all_equities, axis=0)

        final_balances = np.array([r["final_capital"] for r in all_runs])
        avg_drawdown = np.mean([r["max_drawdown"] for r in all_runs])
        avg_win_streak = np.mean([r["max_win_streak"] for r in all_runs])
        avg_loss_streak = np.mean([r["max_loss_streak"] for r in all_runs])

        summary_text = (
            f"Starting Capital: ${initial_capital}\n"
            f"Trades: {num_trades}     Simulations: {num_runs}\n"
            f"Risk per Trade: {risk_percent*100:.1f}%     Winrate: {winrate*100:.0f}%\n"
            f"RRs: {rr_choices}     Probabilities {rr_probs}\n"
            f"\n"
            f"Average Final Capital: ${np.mean(final_balances):.2f}\n"
            f"Best Run: ${np.max(final_balances):.2f}\n"
            f"Worst Run: ${np.min(final_balances):.2f}\n"
            f"Average Max Drawdown: {avg_drawdown:.2f}%\n"
            f"Average Max Win Streak: {avg_win_streak:.1f}\n"
            f"Average Max Loss Streak: {avg_loss_streak:.1f}"
        )

        # --- PLOT ---
        fig, ax = plt.subplots(figsize=(9, 7))

        # Plot average line
        ax.plot(average_equity, linewidth=2, color='green', label='Average')

        # Find indices of the 5 best and 5 worst runs
        sorted_indices = np.argsort(final_balances)
        worst_indices = sorted_indices[:5]
        best_indices = sorted_indices[-5:]

        # Compute the average of best and worst groups
        avg_best_run = np.mean(all_equities[best_indices], axis=0)
        avg_worst_run = np.mean(all_equities[worst_indices], axis=0)

        # Plot lines
        ax.plot(avg_best_run, color='blue', linewidth=1.2, alpha=0.8, label='Avg of 5 Best Runs')
        ax.plot(avg_worst_run, color='red', linewidth=1.2, alpha=0.8, label='Avg of 5 Worst Runs')


        ax.set_title("Average Equity (Compounding)")
        ax.set_xlabel("Trades")
        ax.set_ylabel("Balance (USD)")
        ax.grid(True)
        ax.legend()


        plt.figtext(
            0.05, 0.02, summary_text,
            fontsize=10, va='bottom', ha='left',
            family='monospace'
        )
        plt.subplots_adjust(bottom=0.35)

        # --- SAVE AND OPEN JPG ---
        timestamp = datetime.now().strftime("%m%d_%H%M%S")
        filename = f"simulation_result_{timestamp}.jpg"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close(fig)

        # Automatically open image
        if sys.platform.startswith('darwin'):
            subprocess.call(['open', filename])
        elif os.name == 'nt':
            os.startfile(filename)
        elif os.name == 'posix':
            subprocess.call(['xdg-open', filename])

        root.destroy()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- GUI ---
root = tk.Tk()
root.title("Trading Simulator")
root.geometry("420x420")
root.resizable(False, False)

tk.Label(root, text="Initial Capital ($):").pack()
entry_capital = tk.Entry(root)
entry_capital.insert(0, "1000")
entry_capital.pack()

tk.Label(root, text="Risk per Trade (%):").pack()
entry_risk = tk.Entry(root)
entry_risk.insert(0, "1")
entry_risk.pack()

tk.Label(root, text="Number of Trades:").pack()
entry_trades = tk.Entry(root)
entry_trades.insert(0, "200")
entry_trades.pack()

tk.Label(root, text="Simulations (Runs):").pack()
entry_runs = tk.Entry(root)
entry_runs.insert(0, "90")
entry_runs.pack()

tk.Label(root, text="Winrate (%):").pack()
entry_winrate = tk.Entry(root)
entry_winrate.insert(0, "40")
entry_winrate.pack()

tk.Label(root, text="RR Choices (comma separated):").pack()
entry_rrs = tk.Entry(root)
entry_rrs.insert(0, "1.4, 2, 3.3")
entry_rrs.pack()

tk.Label(root, text="RR Probabilities (comma separated, sum=1):").pack()
entry_probs = tk.Entry(root)
entry_probs.insert(0, "0.4, 0.25, 0.35")
entry_probs.pack()

tk.Button(root, text="Run Simulation", command=run_simulation, bg="green", fg="white").pack(pady=10)

root.mainloop()
