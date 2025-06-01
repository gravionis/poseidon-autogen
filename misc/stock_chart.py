# filename: stock_chart.py
import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import matplotlib.backends.backend_tkagg as tkagg
import PySimpleGUI as sg

today = datetime.date.today()
thirty_days_ago = today - datetime.timedelta(days=30)

tickers = ["MSFT", "META", "TSLA"]
data = yf.download(tickers, start=thirty_days_ago, end=today)

pe_ratios = {}
for ticker in tickers:
    try:
        info = yf.Ticker(ticker).info
        pe_ratios[ticker] = info['trailingPE']
    except (KeyError, IndexError):
        print(f"Could not retrieve P/E ratio for {ticker}")
        pe_ratios[ticker] = None

# --- Matplotlib code ---
fig = plt.figure(figsize=(10, 6))
for ticker in tickers:
    plt.plot(data['Close'][ticker], label=ticker)

plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("Stock Prices (Last 30 Days)")
plt.legend()

# --- PySimpleGUI code ---
layout = [[sg.Canvas(key='-CANVAS-')],
          [sg.Button('Ok')]]

window = sg.Window('Stock Chart', layout, finalize=True)

# Embed Matplotlib plot into Tkinter canvas
figure_canvas_agg = tkagg.FigureCanvasTkAgg(fig, window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

event, values = window.read()
window.close()

best_pe_ticker = min(pe_ratios, key=pe_ratios.get) if pe_ratios else "N/A"
best_pe_ratio = pe_ratios[best_pe_ticker] if best_pe_ticker != "N/A" else "N/A"

print(f"Best P/E ratio: {best_pe_ticker} ({best_pe_ratio if best_pe_ratio is not None else 'N/A'})")
