
#ESTE ES EL MAIN DE MI EJERCICIO DE SERIALIZACION.

from tkinter import *
from Vista import *

#FUNCION PRINCIPAL
def main():
    root = Tk()
    root.wm_title("Ejercicio_Serializacion_Main")
    app = vista(root)
    app.mainloop()
    

if __name__ == "__main__":
    main()