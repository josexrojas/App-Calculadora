#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk

def suma():
	cajaTres.delete(0, tk.END)
	a = cajaUno.get()
	a = float(a)
	b = cajaDos.get()
	b = float(b)
	c = a + b
	cajaTres.insert(0, c)
	print(c)
	
def resta():
	cajaTres.delete(0, tk.END)
	a = cajaUno.get()
	a = float(a)
	b = cajaDos.get()
	b = float(b)
	c = a - b
	cajaTres.insert(0, c)
	print(c)
	
def producto():
	cajaTres.delete(0, tk.END)
	a = cajaUno.get()
	a = float(a)
	b = cajaDos.get()
	b = float(b)
	c = a * b
	cajaTres.insert(0, c)
	print(c)
	
def division():
	cajaTres.delete(0, tk.END)
	a = cajaUno.get()
	a = float(a)
	b = cajaDos.get()
	b = float(b)
	c = 0
	
	if b == 0:
		cajaTres.insert(0, "¡Error!")
		print("No se puede dividir por 0")
	else:
		c = a / b
		cajaTres.insert(0, c)
		print(c)
	
ventana = tk.Tk()
ventana.config(width = 500, height = 200)
ventana.title("App Calculadora")

botonSuma = tk.Button(text = "Sumar (+)", command = suma)
botonSuma.place(x = 20, y = 10, width = 100, height = 30)

botonResta = tk.Button(text = "Restar (-)", command = resta)
botonResta.place(x = 130, y = 10, width = 100, height = 30)

botonProducto = tk.Button(text = "Multiplicar (*)", command = producto)
botonProducto.place(x = 240, y = 10, width = 100, height = 30)

botonDivision = tk.Button(text = "Dividir (/)", command = division)
botonDivision.place(x = 350, y = 10, width = 100, height = 30)

cajaUno = tk.Entry()
cajaUno.place(x=20, y=75, width=100, height=25)

cajaDos = tk.Entry()
cajaDos.place(x=20, y=110, width=100, height=25)

cajaTres = tk.Entry()
cajaTres.place(x=20, y=160, width=100, height=25)

etiqueta = tk.Label(text = "Ingresa valores:")
etiqueta.place(x=20, y=50)

etiqueta = tk.Label(text = "___________________")
etiqueta.place(x=20, y=130)

ventana.mainloop()
