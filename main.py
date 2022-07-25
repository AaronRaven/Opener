# Bibliotekos
# atidaryti faila
import PySimpleGUI as sg
# parodyti grafika
from tkinter import *
# gauti informacija
import yfinance as yf
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

''''
programa kuri turejo atidaryti faila
'''
'''
file_path = sg.popup_get_file("Choose Excel file", multiple_files=True, file_types=(("Excel Files", "*.xls*"),),)
if not file_path:
   sg.popup("No file selected")
   raise SystemExit("Error: no file selected")
else:
	sg.popup("The file you selected:",file_path )
'''
'''
Programa kuri turejo rodyti, and ektrano interpretacija
'''

opener = Tk()
opener.title('Analisator :D')
opener.geometry("400x200")
'''
def graph():
	maximastockprice = np.random.normal(15, 5, 500)
	plt.hist(maximastockprice, 50)
	plt.show()
	'''


def graph():
    aapl = yf.Ticker("AAPL")
    aapl = aapl[["Date", "Close"]]
    aapl = aapl.rename(columns={'Date:': 'ds', 'Close': 'y'})
    plt.hist(aapl)
    plt.show()


'''
   cia yra yfinance bugas. Jis neleidzia filtruoti
   datos. yahoo leidzia atsisiusti excell failus
   ir internete maciau, kad leidzia filtruoti
   bet pas mane nera excellio.
   bet is esmes programele veikia
   	'''

button = Button(opener, text="Graph It!", command=graph)
button.pack()

opener.mainloop()
