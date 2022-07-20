import tkinter as tk
from tkinter import Entry, ttk
from PIL import ImageTk,Image
from tkinter import *

import psychrolib
psychrolib.SetUnitSystem(psychrolib.SI)

from sympy.solvers import solve
from sympy import Symbol

#Relative Humidty from T and h (SI)
def find_Rh(T_air,h):
  x = Symbol('x')
  return (solve(0.24*(T_air*1.8+32)+(0.6219)*(0.01*(0.000000007401234*(T_air*1.8+32)**4
-0.000000493526794*(T_air*1.8+32)**3+0.000071281097208*(T_air*1.8+32)**2
-0.000489806163078*(T_air*1.8+32)+0.039762055806989)*x)/(14.7-(0.01*(0.000000007401234
*(T_air*1.8+32)**4-0.000000493526794*(T_air*1.8+32)**3+0.000071281097208*(T_air*1.8+32)**2
-0.000489806163078*(T_air*1.8+32)+0.039762055806989)*x))*(1061.2+0.444*(T_air*1.8+32))-h/2.326,x))

#Vaporizing Enthapy Calculator (hfg) (input:°C)
def find_hfg(a):
  return (-2.5835)*a + 2514

# Creating tkinter root
root = tk.Tk()
root.title('\nPsychro v1.0')
root.geometry('500x600')
root.iconbitmap('./logo.ico')

ent1=tk.StringVar()
ent2=tk.StringVar()
ent3=tk.StringVar()


# label text for title
ttk.Label(root, text = "Psychrometric Calculator", 
          #background = 'red', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)
  

# label
ttk.Label(root, text = "Input types :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 2, padx = 10, pady = 25)
  

# Combobox creation
n = tk.StringVar()
cmb = ttk.Combobox(root, width = 40, textvariable = n, state="readonly")  
  
# Adding combobox drop down list
cmb['values'] = (' TDryBulb [C]    RelHum [%]    Pressure [atm]', 
                          ' TDryBulb [C]    TDewPoint [C]    Pressure [atm]',
                          ' TDryBulb [C]    TWetBulb [C]    Pressure [atm]',
                          ' TDryBulb [C]    Enthalphy [kj/kg]',
                          ' Find Water Enthalpy h_g by Temperature'
                          )
  
cmb.grid(column = 1, row = 2)
cmb.current()


def result1():
  entry1=ent1.get()
  entry2=ent2.get()
  entry3=ent3.get()
  
  hr=str(psychrolib.CalcPsychrometricsFromRelHum(float(entry1), float(entry2)*0.01,float(entry3)*101325)[0])
  Label_1 = Label(root, text = "\nHumidity Ratio [kg_w/kg_a] : " + hr)
  Label_1.grid(row=10,column=1)
  Label_1.pack

  WetBulbT=str(psychrolib.CalcPsychrometricsFromRelHum(float(entry1), float(entry2)*0.01,float(entry3)*101325)[1])
  Label_2 = Label(root, text = "\nWet Bulb Temperature [C] : " + WetBulbT)
  Label_2.grid(row=11,column=1)
  Label_2.pack

  DewT=str(psychrolib.CalcPsychrometricsFromRelHum(float(entry1), float(entry2)*0.01,float(entry3)*101325)[2])
  Label_3 = Label(root, text = "\nDew Point Temperature [C] : " + DewT)
  Label_3.grid(row=12,column=1)
  Label_3.pack

  Pres=str(psychrolib.CalcPsychrometricsFromRelHum(float(entry1), float(entry2)*0.01,float(entry3)*101325)[3])
  Label_4 = Label(root, text = "\nPartial pressure of water vapor [Pa] : " + Pres)
  Label_4.grid(row=13,column=1)
  Label_4.pack

  Enthalpy=str(float(psychrolib.CalcPsychrometricsFromRelHum(float(entry1), float(entry2)*0.01,float(entry3)*101325)[4])*0.001)
  Label_5 = Label(root, text = "\nEnthalpy [kJ/kg] : " + Enthalpy)
  Label_5.grid(row=14,column=1)
  Label_5.pack

  ro=str(1/(psychrolib.CalcPsychrometricsFromRelHum(float(entry1), float(entry2)*0.01,float(entry3)*101325)[5]))
  Label_6 = Label(root, text = "\nDensity [kg/m3] : " + ro)
  Label_6.grid(row=15,column=1)
  Label_6.pack

  Sat_Deg=str(psychrolib.CalcPsychrometricsFromRelHum(float(entry1), float(entry2)*0.01,float(entry3)*101325)[6])
  Label_7 = Label(root, text = "\nDegree of saturation [unitless] : " + Sat_Deg)
  Label_7.grid(row=16,column=1)
  Label_7.pack

def result2():
  entry1=ent1.get()
  entry2=ent2.get()
  entry3=ent3.get()
  
  hr=str(psychrolib.CalcPsychrometricsFromTDewPoint(float(entry1), float(entry2),float(entry3)*101325)[0])
  Label_1 = Label(root, text = "\nHumidity Ratio [kg_w/kg_a] : " + hr)
  Label_1.grid(row=10,column=1)
  Label_1.pack

  WetBulbT=str(psychrolib.CalcPsychrometricsFromTDewPoint(float(entry1), float(entry2),float(entry3)*101325)[1])
  Label_2 = Label(root, text = "\nWet Bulb Temperature [C] : " + WetBulbT)
  Label_2.grid(row=11,column=1)
  Label_2.pack

  Rh=str(float(psychrolib.CalcPsychrometricsFromTDewPoint(float(entry1), float(entry2),float(entry3)*101325)[2])*100)
  Label_3 = Label(root, text = "\nRelative Humidity [%] : " + Rh)
  Label_3.grid(row=12,column=1)
  Label_3.pack

  Pres=str(psychrolib.CalcPsychrometricsFromTDewPoint(float(entry1), float(entry2),float(entry3)*101325)[3])
  Label_4 = Label(root, text = "\nPartial pressure of water vapor [Pa] : " + Pres)
  Label_4.grid(row=13,column=1)
  Label_4.pack

  Enthalpy=str(float(psychrolib.CalcPsychrometricsFromTDewPoint(float(entry1), float(entry2),float(entry3)*101325)[4])*0.001)
  Label_5 = Label(root, text = "\nEnthalpy [kJ/kg] : " + Enthalpy)
  Label_5.grid(row=14,column=1)
  Label_5.pack

  ro=str(1/(psychrolib.CalcPsychrometricsFromTDewPoint(float(entry1), float(entry2),float(entry3)*101325)[5]))
  Label_6 = Label(root, text = "\nDensity [kg/m3] : " + ro)
  Label_6.grid(row=15,column=1)
  Label_6.pack

  Sat_Deg=str(psychrolib.CalcPsychrometricsFromTDewPoint(float(entry1), float(entry2),float(entry3)*101325)[6])
  Label_7 = Label(root, text = "\nDegree of saturation [unitless] : " + Sat_Deg)
  Label_7.grid(row=16,column=1)
  Label_7.pack

def result3():
  entry1=ent1.get()
  entry2=ent2.get()
  entry3=ent3.get()
  
  hr=str(psychrolib.CalcPsychrometricsFromTWetBulb(float(entry1), float(entry2),float(entry3)*101325)[0])
  Label_1 = Label(root, text = "\nHumidity Ratio [kg_w/kg_a] : " + hr)
  Label_1.grid(row=10,column=1)
  Label_1.pack

  Tdew=str(psychrolib.CalcPsychrometricsFromTWetBulb(float(entry1), float(entry2),float(entry3)*101325)[1])
  Label_2 = Label(root, text = "\nDew Point Temperature [C] : " + Tdew)
  Label_2.grid(row=11,column=1)
  Label_2.pack

  Rh=str(float(psychrolib.CalcPsychrometricsFromTWetBulb(float(entry1), float(entry2),float(entry3)*101325)[2])*100)
  Label_3 = Label(root, text = "\nRelative Humidity [%] : " + Rh)
  Label_3.grid(row=12,column=1)
  Label_3.pack

  Pres=str(psychrolib.CalcPsychrometricsFromTWetBulb(float(entry1), float(entry2),float(entry3)*101325)[3])
  Label_4 = Label(root, text = "\nPartial pressure of water vapor [Pa] : " + Pres)
  Label_4.grid(row=13,column=1)
  Label_4.pack

  Enthalpy=str(float(psychrolib.CalcPsychrometricsFromTWetBulb(float(entry1), float(entry2),float(entry3)*101325)[4])*0.001)
  Label_5 = Label(root, text = "\nEnthalpy [kJ/kg] : " + Enthalpy)
  Label_5.grid(row=14,column=1)
  Label_5.pack

  ro=str(1/(psychrolib.CalcPsychrometricsFromTWetBulb(float(entry1), float(entry2),float(entry3)*101325)[5]))
  Label_6 = Label(root, text = "\nDensity [kg/m3] : " + ro)
  Label_6.grid(row=15,column=1)
  Label_6.pack

  Sat_Deg=str(psychrolib.CalcPsychrometricsFromTWetBulb(float(entry1), float(entry2),float(entry3)*101325)[6])
  Label_7 = Label(root, text = "\nDegree of saturation [unitless] : " + Sat_Deg)
  Label_7.grid(row=16,column=1)
  Label_7.pack

def result4():
  entry1=ent1.get()
  entry2=ent2.get()
  
  relhum=str(float(find_Rh(float(entry1),float(entry2))[0]))
  Label_1 = Label(root, text = "\nRelative Humidity [%] : " + relhum)
  Label_1.grid(row=10,column=1)
  Label_1.pack

def result5():
  entry1=ent1.get()
    
  hfg=str(find_hfg(float(entry1)))
  Label_1 = Label(root, text = "\nh_fg [kj/kg] : " + hfg)
  Label_1.grid(row=10,column=1)
  Label_1.pack


def checkcmbo():

    if cmb.get() ==  " TDryBulb [C]    RelHum [%]    Pressure [atm]":

      Label1 = Label(root, text="TDryBulb [C] : ")
      Label1.grid(row=4,column=0)
      Label1.pack

      e1=Entry(root,textvariable=ent1, width=10)
      e1.grid(row=4,column=1)
      e1.pack

      Label2 = Label(root, text="RelHum [%] : ")
      Label2.grid(row=5,column=0)
      Label2.pack

      e2=Entry(root,textvariable=ent2, width=10)
      e2.grid(row=5,column=1)
      e2.pack

      Label3 = Label(root, text="Pressure [atm] : ")
      Label3.grid(row=6,column=0)
      Label3.pack

      e3=Entry(root,textvariable=ent3, width=10)
      e3.grid(row=6,column=1)
      e3.pack

      btn = ttk.Button(root, text="Show Results",command=result1)
      btn.grid(column = 3, row = 5)

    if cmb.get() ==  " TDryBulb [C]    TDewPoint [C]    Pressure [atm]":
      Label1= Label(root, text="TDryBulb [C] : ")
      Label1.grid(row=4,column=0)
      Label1.pack

      e1=Entry(root,textvariable=ent1, width=10)
      e1.grid(row=4,column=1)
      e1.pack

      Label2 = Label(root, text="T Dew Point [C] : ")
      Label2.grid(row=5,column=0)
      Label2.pack

      e2=Entry(root,textvariable=ent2, width=10)
      e2.grid(row=5,column=1)
      e2.pack

      Label3 = Label(root, text="Pressure [atm] : ")
      Label3.grid(row=6,column=0)
      Label3.pack

      e3=Entry(root,textvariable=ent3, width=10)
      e3.grid(row=6,column=1)
      e3.pack

      btn = ttk.Button(root, text="Show Results",command=result2)
      btn.grid(column = 3, row = 5)

    if cmb.get() ==  " TDryBulb [C]    TWetBulb [C]    Pressure [atm]":
      Label1= Label(root, text="TDryBulb [C] : ")
      Label1.grid(row=4,column=0)
      Label1.pack

      e1=Entry(root,textvariable=ent1, width=10)
      e1.grid(row=4,column=1)
      e1.pack

      Label2 = Label(root, text="T Wet Bulb [C] : ")
      Label2.grid(row=5,column=0)
      Label2.pack

      e2=Entry(root,textvariable=ent2, width=10)
      e2.grid(row=5,column=1)
      e2.pack

      Label3 = Label(root, text="Pressure [atm] : ")
      Label3.grid(row=6,column=0)
      Label3.pack

      e3=Entry(root,textvariable=ent3, width=10)
      e3.grid(row=6,column=1)
      e3.pack

      btn = ttk.Button(root, text="Show Results",command=result3)
      btn.grid(column = 3, row = 5)

    if cmb.get() ==  " TDryBulb [C]    Enthalphy [kj/kg]":
      Label1= Label(root, text="TDryBulb [C] : ")
      Label1.grid(row=4,column=0)
      Label1.pack

      e1=Entry(root,textvariable=ent1, width=10)
      e1.grid(row=4,column=1)
      e1.pack

      Label2 = Label(root, text="Enthalphy [kj/kg] : ")
      Label2.grid(row=5,column=0)
      Label2.pack

      e2=Entry(root,textvariable=ent2, width=10)
      e2.grid(row=5,column=1)
      e2.pack

      btn = ttk.Button(root, text="Show Results",command=result4)
      btn.grid(column = 3, row = 5)

    if cmb.get() ==  " Find Water Enthalpy h_g by Temperature":
      Label1= Label(root, text="Temperature [C] : ")
      Label1.grid(row=4,column=0)
      Label1.pack

      e1=Entry(root,textvariable=ent1, width=10)
      e1.grid(row=4,column=1)
      e1.pack

      btn = ttk.Button(root, text="Show Results",command=result5)
      btn.grid(column = 3, row = 4)


   


btn_ok = ttk.Button(root, text="OK",command=checkcmbo)

btn_ok.grid(column = 3, row = 2)


root.mainloop()