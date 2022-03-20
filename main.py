import tkinter
from tkinter import ttk
 
import CountriesService
import StatsService
 
from MyModel import ResultModel
import matplotlib.pyplot as plt

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)
 
form = tkinter.Tk()
 
form.title("My Covid App")
form.geometry("1000x600")
 
lblInfo = tkinter.Label(form, text="Rest api covid",
font=("Times New Roman",20),fg="blue")
 
lblInfo.grid(row=0,column=0,sticky="we")
 
left_frame=tkinter.Frame(form, bg="green", highlightbackground="black",highlightthickness=2)
left_frame.grid(row=1,column=0)
 
right_frame=tkinter.Frame(form, bg="gray",highlightbackground="black",highlightthickness=2)
right_frame.grid(row=1,column=1)
 
plot_frame=tkinter.Frame(form, bg="green",highlightbackground="black",highlightthickness=2)
plot_frame.grid(row=2,column=1)
 
 
def SelectedIndexChanged(event):
    global selectedCountry
    selectedCountry = str(event.widget.get())
 
    cs:ResultModel=StatsService.StatsService.get_stats(selectedCountry)
 
    text.set(
        str(cs.country)+"\n confirmed: "+
        str(cs.mystats["confirmed"])+"\n deaths: "+
        str(cs.mystats["deaths"])+"\n date: "+
        str(cs.mystats["date"])+"\n active: "+
        str(cs.mystats["active"])
 
    )
 
 
 
countries = CountriesService.CountriesService.get_countries()
 
cb=ttk.Combobox(left_frame,values=countries)
cb.grid(row=0,column=0)
cb.bind("<<ComboboxSelected>>",SelectedIndexChanged)
 
 
text = tkinter.StringVar()
text.set("result")
 
lblResult = tkinter.Label(right_frame,textvariable=text)
lblResult.grid(row=0,column=0,padx=20,pady=20)

countriesList=[]

def btnAddClick():
    countriesList.append(selectedCountry)
    str=""
    for c in countriesList:
        str=str+c+"\n"
    textCountries.set(str)

btn =tkinter.Button(right_frame,width=30,height=2, text="Add Country", command=btnAddClick)
btn.grid(row=1,column=0,padx=20,pady=20)


def btnShowClick():
    drawPlot()

btnShow =tkinter.Button(right_frame,width=30,height=2, text="Show plot", command=btnShowClick)
btnShow.grid(row=1,column=1,padx=20,pady=20)

textCountries = tkinter.StringVar()

lblCountries=tkinter.Label(right_frame,textvariable=textCountries)
lblCountries.grid(row=0,column=1)

def drawPlot():
    fig = Figure(figsize=(5,5),dpi=100)
    plot = fig.add_subplot(111)

    data=StatsService.StatsService.get_deaths_all_countries(countriesList)

    plot.bar(countriesList,data)
    canvas=FigureCanvasTkAgg(fig,master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)
tkinter.mainloop()