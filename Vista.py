#ESTA ES LA VISTA DE MI SERIALIZACION

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


alumnos = []
class alumno():
    def __init__(self, Nombre, Apellido, Apodo, Dni):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Apodo = Apodo
        self.Dni = Dni


#CREAMOS EL DISEÑO DE LA VISTA Y HABLITIAMOS  BOTONES
class vista(Frame):
    def __init__(self, master = None):
        super().__init__(master, width = 600, height = 300)
        self.master = master 
        self.pack()
        self.create_widgets()
        self.habilC("disabled")  
        self.habilBtnAbrir("normal")
        self.habilBtnGuardar("disabled")  
        self.id=-1 

    def habilC(self,status):
        self.txtNombre.configure(estado=status)
        self.txtApellido.configure(estado=status)
        self.txtApodo.configure(estado=status)
        self.txtDni.configure(estado=status)

    def habilBtnAbrir(self,status):
        self.NewBtn.configure(estado=status)                
        self.ModifyBtn.configure(estado=status)
        self.EliminateBtn.configure(estado=status)
        


    def habilBtnGuardar(self,status):
        self.btnGuardar.configure(estado=status)                
        self.btnCancelar.configure(estado=status)


    def limpiarC(self):
        self.txtNombre.delete(0,END)
        self.txtApellido.delete(0,END)
        self.txtApodo.delete(0,END)
        self.txtDni.delete(0,END)
        
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)     
    

    #Creamos unp predeterminado

    def fNuevo(self):
        self.habilC("normal")  
        self.habilBtnAbrir("disabled")
        self.habilBtnGuardar("normal")
        self.limpiarC()        
        self.txtNombre.focus()


    def fEliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Esta es la opcion modificar", ' selecciona un elemento.')            
        else:            
          valores = self.grid.item(selected,'values')
          data = str(clave) + ", " + valores[0] + ", " + valores[1]
          r = messagebox.askquestion(" Esta es la opcion eliminar", " elimino el registro seleccionado?\n" + data)            
          if r == messagebox.YES:
             messagebox.showinfo("Eliminar", 'Elemento eliminado ')
             self.limpiaGrid()
        

    def fModificar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Esta es la opcion modificar", ' selecciona un elemento.')            
        else:            
            self.id= clave  
            self.habilC("normal")                         
            valores = self.grid.item(selected,'values')
            self.limpiarC()            
            self.txtNombre.insert(0,valores[0])
            self.txtApellido.insert(0,valores[1])
            self.txtApodo.insert(0,valores[2])
            self.txtDni.insert(0,valores[3])            
            self.habilBtnAbrir("disabled")
            self.habilBtnGuardar("normal")
            self.txtNombre.focus()  
    

    def fGuardar(self):
        if self.id ==-1:       
            self.alumno.insert(self.txtNombre.get(),self.txtApellido.get(),self.txtApodo.get(),self.txtDni.get())            
            messagebox.showinfo("Esta es la opcion insertar", 'Elemento insertado.')
        else:
            self.alumno.insert(self.txtNombre.get(),self.txtApellido.get(),self.txtApodo.get(),self.txtDni.get())
            messagebox.showinfo("Esta es la opcion modificar", 'Elemento modificado .')
            self.id = -1 
            self.limpiaGrid()
            self.limpiarC() 
            self.habilBtnGuardar("disabled")      
            self.habilBtnAbrir("normal")
            self.habilC("disabled") 
           

    def fCancelar(self):
        r = messagebox.askquestion("Esta es la opcion calcelar", "Esta seguro que quieres cancelar la operación actual? ")
        if r == messagebox.YES:
            self.limpiarC() 
            self.habilBtnGuardar("disabled")      
            self.habilBtnAbrir("normal")
            self.habilC("disabled")
          

     #Aqui vamos a crear y modificar el panel de control del Frame 
    def create_widgets(self):
        num = 0
        frame1 = Frame(self, bg = "#bfdaff")
        frame1.place(x= 0, y=0, width= 123, height= 279)
        
        #crear boton de nuevo 
        self.NewBtn = Button(frame1, text = "Nuevo", command=self.fNuevo, bg = "green", fg = "white")
        self.NewBtn.place(x= 20, y = 60 , width = 80, height = 30)
        
        #crear boton de eliminar 
        self.EliminateBtn = Button(frame1, text = "Eliminar",command = self.fEliminar, bg = "red", fg = "white")
        self.EliminateBtn.place(x= 10, y = 100 , width = 90, height = 30)
        
        #crear el boton de modificar 
        self.ModifyBtn = Button(frame1, text = "Modificar", command = self.fModificar, bg = "blue", fg = "white")
        self.ModifyBtn.place(x= 10, y = 140 , width = 90, height = 30)
        
        #------------------------------------------------------#


        # Panel
        frame2 = Frame(self, bg= "#81BEF7")
        frame2.place(x = 100, y = 0, width = 150, height= 259)
 
        #Creacion de componentes en un panel


        lbl1 = Label(frame2, text = "Nombre:  ")
        lbl1.place(x = 3, y = 5)
        
        self.txtNombre = Entry(frame2)
        self.txtNombre.place(x=3, y= 25, width = 50, height= 20)
        
        
        lbl2 = Label(frame2, text = "Apellido:  ")
        lbl2.place(x= 3, y = 55)
        
        self.txtApellido = Entry(frame2)
        self.txtApellido.place(x=3, y= 75, width = 100, height= 20)
        
        lbl3 = Label(frame2, text = "Apodo:  ")
        lbl3.place(x =3, y= 105)
        
        self.txtApodo = Entry(frame2)
        self.txtApodo.place(x = 3, y= 125, width = 100, height= 20)
        
        lbl4 = Label(frame2, text = "Dni  ")
        lbl4.place(x = 3, y= 160)
        
        self.txtDni = Entry(frame2)
        self.txtDni.place(x = 3, y= 180, width = 100, height= 20)


        

         #creacion boton guardar y cancelar 
        
        #-----Guardar----#
        self.btnGuardar = Button(frame2, text= "Guardar", command = self.fGuardar, bg = "green" , fg = "white")
        self.btnGuardar.place(x = 10, y = 210 , width=60 , height=30)
        
        #-----Cancelar----#
        self.btnCancelar = Button(frame2, text = "Cancelar", command = self.fCancelar, bg = "red",  fg = "white")
        self.btnCancelar.place(x = 80, y = 210, width= 60, height=30)
        
        frame3 = Frame(self,bg="yellow" )
        frame3.place(x=247,y=0,width=420, height=259)   
                           
        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4"))        
        self.grid.column("#0",width=60)
        self.grid.column("col1",width=70, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)    
        
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Apellido", anchor=CENTER)
        self.grid.heading("col3", text="Apodo", anchor=CENTER)
        self.grid.heading("col4", text="Dni", anchor=CENTER) 
        
                       
        self.grid.pack(side=LEFT,fill = Y)        
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse'
        
        #Insertar datos dentro de la tabla 
        self.grid.insert("",END, text= "1", values=("Antonio", "Lizana","anto", "76634403X"))
        self.grid.insert("",END, text= "2", values=("George", "Vega", "deyvy", "76635503L"))
        self.grid.insert("",END, text= "3", values=("Dani", "Perez", "daniguti", "75534402X") )
        self.grid.insert("",END, text= "4", values=("Maria", "sanchez", "Mari", "76623390J"))
        self.grid.insert("",END, text= "5", values=("Carmern", "sanchez", "carmenchu", "96645390J"))
        self.grid.insert("",END, text= "6", values=("francisco", "Jaimez", "FJ", "77667393J"))
        self.grid.insert("",END, text= "7", values=("Javier", "Cobos", "Javi", "99623388J"))
        self.grid.insert("",END, text= "8", values=("Miguel", "Miranda", "maik", "12626690J"))