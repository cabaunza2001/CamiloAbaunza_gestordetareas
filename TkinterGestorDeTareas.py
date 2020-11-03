"""
Fecha: Noviembre 02 2020
Autor: Camilo Andres Abaunza Suarez
Documentacion:
Programa GESTOR DE TAREAS
Funcion principal: Nuestro proyecto consiste en una aplicación que registre, asigne y que mantenga
seguimiento de las tareas que se pueden presentar en un ambiente.  Esta aplicación se encargará de
facilitar lo más posible la repartición de los deberes, así mismo se encargará de repartirlas de
manera equitativa entre los integrantes.
Objetivo:El objetivo de la aplicación es el de simplemente facilitar la asignación junto a la
gestión de las tareas, así mismo se busca que el programa mejore el uso de tiempo y ayude con
la organización a la hora de realizar las diferentes actividades.
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk

#Definicion de variables
NumTareas = 10   #Cantidad de tareas habilitadas por defecto.
tareas = ['Arreglar Patio', 'Barrer', 'Lavar Loza','Lavar Ropa', 'Limpiar Baños', 'Limpiar Cocina', 'Limpiar Ventanas', 'Organizar Habitaciones', 'Planchar Ropa', 'Trapear Hall']
vector_integrantes = []
vector_integrantes.append('')
vector_tareas = []
vector_tareas.append('')
ContadorTareas = 1
ContadorIntegrantes = 1


#Se declara funcion principal
def GestorTareas():
    ventanaprincipal = Tk()
    ventanaprincipal.geometry('500x500')
    ventanaprincipal.title('Gestor de Tareas (Beta 1.0)')
    #num_integrantes = IntVar(value=1)

    #Menu con opcion para salir de la aplicacion
    menu = Menu(ventanaprincipal)
    new_item = Menu(menu)
    new_item.add_command(label='Salir', command=ventanaprincipal.destroy)
    menu.add_cascade(label='Archivo', menu=new_item)
    ventanaprincipal.config(menu=menu)    
    #Fin Menu

    #Control para seleccion de numero de integrantes
    texto1 = tk.Label(ventanaprincipal, text = 'Seleccione el número de integrantes: ', font=('Arial bold',10))
    texto1.grid(column=0, row=2)
    caja1 = Spinbox(ventanaprincipal, from_=1, to=10, wrap=True, state='readonly', width = 5)
    caja1.grid(column = 1 , row = 2)
    
    #Mostrar lista tareas a modo referencial nada mas
    
    Texto2 = tk.Label(ventanaprincipal, text = 'Lista de tareas existentes: ', font=('Arial bold', 10))
    Texto2.grid(column=0, row=6)
    combo_tareas = ttk.Combobox(ventanaprincipal, state='readonly')
    combo_tareas['values'] = ['Arreglar Patio', 'Barrer', 'Lavar Loza','Lavar Ropa', 'Limpiar Baños', 'Limpiar Cocina', 'Limpiar Ventanas', 'Organizar Habitaciones', 'Planchar Ropa', 'Trapear Hall']
    combo_tareas.current(0)
    combo_tareas.grid(column = 1 , row = 6)

    
    ###Inicio Funcion Asignar Tareas
    def AsignarTareas():
        NumTareas = 10   #Cantidad de tareas habilitadas por defecto. 10 tareas y en la primer posicion valor en blanco
        vector_integrantes = []
        vector_tareas = []
        ContadorTareas = 0
        ContadorIntegrantes = 1
        TotalIntegrantes = int(caja1.get()) #aca se debe tomar el valor de la caja1
 
        while ContadorTareas < NumTareas: #Control de tareas asignadas
            if ContadorIntegrantes <= TotalIntegrantes:
                vector_integrantes.append(ContadorIntegrantes)
                vector_tareas.append(tareas[ContadorTareas])
                print('Integrante: ',vector_integrantes[ContadorIntegrantes-1],'Tarea: ',vector_tareas[ContadorTareas])  #Imprime la asignacion por Shell
                if ContadorTareas < NumTareas:
                    ContadorTareas = ContadorTareas + 1
                if ContadorIntegrantes <= TotalIntegrantes:
                    ContadorIntegrantes = ContadorIntegrantes + 1
            else:
                ContadorIntegrantes = 1  #reinicia para asignar nueva ronda de tareas
        print()     
    ###Final funcion Asignar tareas
       

    #Boton para asignar tareas de forma automatica
    boton2 = Button(ventanaprincipal, text=" Asignar Tareas ", bg="red",fg="white", command=AsignarTareas)
    boton2.grid(column=6, row=6)
    
    ventanaprincipal.mainloop()
#Fin de la funcion GestorTareas
   

def main():
    GestorTareas()


#Ejecucion de aplicacion principal
main()    
