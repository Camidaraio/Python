import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

A)  Al presionar el botón 'Agregar' se debera cargar el precio (ingresado por el usuario sin iva) con el iva incluido 
    en la lista correspondiente, segun se trate de un articulo con IVA del 21% o del 10.5%.

    La condicion del articulo frente al IVA es indicada mediante una lista desplegable.

** Flotantes positivos

Si existe error al validar indicarlo mediante un Alert
Si se cargo  correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los precios sin iva y su posicion en la lista (por terminal)

¡¡IMPORTANTE!!

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR.

C) Al precionar el boton Informar 
    0- Valor y posicion frente al IVA del o los Articulo/s sin IVA mas caro/s
    1- Valor y posicion frente al IVA del o los Articulo/s mas barato IVA incluido
    2- Precio promedio sin IVA
    3- Precio promedio con IVA
    4- Valor y posicion frente al IVA del o los Articulo/s que son mas caros que el promedio sin IVA
    5- Valor y posicion frente al IVA del o los Articulo/s que son mas baratos que el promedio sin IVA
    6- Valor y posicion frente al IVA del o los Articulo/s que son mas caros que el promedio con IVA
    7- Valor y posicion frente al IVA del o los Articulo/s que son mas baratos que el promedio con IVA
    8- Valor y posicion frente al IVA del o los Articulo/s cuyo valor se repite en la lista que integra
    9- Valor y posicion frente al IVA del o los Articulo/s cuyo valor NO se repite en la lista que integra

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")

        self.txt_precio_articulo = customtkinter.CTkEntry(master=self, placeholder_text="Precio")
        self.txt_precio_articulo.grid(row=1, padx=20, pady=20)

        self.combobox_iva = customtkinter.CTkComboBox(master=self, values=["10.5","21"])
        self.combobox_iva.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_precios_con_iva_21 = [121 , 242 ]
        self.lista_precios_con_iva_105 = [221, 110.50 ]


    def btn_agregar_on_click(self):
        precio_sin_iva_texto = self.txt_precio_articulo.get()
        iva_texto = self.combobox_iva.get()
        contador_puntos = 0
       
        if(precio_sin_iva_texto != ""):   #if(len(precio_sin_iva_texto) > 0):
            flag_precio_ok = True
            for letra in precio_sin_iva_texto:
                if((letra < '0' or letra > '9')  and letra != '.' ):
                    flag_precio_ok = False
                    break
                else:
                    if(letra=='.'):
                        contador_puntos = contador_puntos + 1
        else:
            flag_precio_ok = False

        if(flag_precio_ok != False and contador_puntos <= 1):
            precio_sin_iva_float= float(precio_sin_iva_texto)
            if(iva_texto == "21"):
                precio_con_iva_float = precio_sin_iva_float * 1.21
                self.lista_precios_con_iva_21.append(precio_con_iva_float)
                alert(title="Exito",message="Se cargo correctamente el dato")

            elif(iva_texto == "10.5"):
                precio_con_iva_float = precio_sin_iva_float * 1.105
                self.lista_precios_con_iva_105.append(precio_con_iva_float)
                alert(title="Exito",message="Se cargo correctamente el dato")
        else:
            alert(title="Error",message="El valor no es valido")



    def btn_mostrar_on_click(self):

        indice = 0
        for precio_con_iva in self.lista_precios_con_iva_105:
            mensaje= "En la pos: {0} - El precio es: {1} - IVA 10.5".format(indice, precio_con_iva/1.105)
            indice = indice + 1 
            print(mensaje)
                     
        logitud_lista = len(self.lista_precios_con_iva_21)
        for indice in range(logitud_lista):
            mensaje= "En la pos: {0} - El precio es: {1} - IVA 21".format(indice, self.lista_precios_con_iva_21[indice]/1.21)
            print(mensaje)


    def btn_informar_on_click(self):
        #self.informe_0()
        #self.informe_0_bis()
        #self.informe_1()
        #self.informe_2()
        # self.informe_3()
        #self.informe_4()
        #self.informe_5()
        #self.informe_6()
        #self.informe_7()
        #self.informe_8()
        self.informe_9()

    def informe_0(self):
        # 0- Valor y posicion frente al IVA del o los Articulo/s sin IVA mas caro/s
        lista_articulos_105_21_sin_iva = []

        for precio_con_iva in self.lista_precios_con_iva_105:
            precio_sin_iva = precio_con_iva / 1.105
            lista_articulos_105_21_sin_iva.append(precio_sin_iva)

        for precio_con_iva in self.lista_precios_con_iva_21:
            precio_sin_iva = precio_con_iva / 1.21
            lista_articulos_105_21_sin_iva.append(precio_sin_iva)

        precio_sin_iva_maximo = None
        for precio_sin_iva in lista_articulos_105_21_sin_iva:
            if(precio_sin_iva_maximo == None or precio_sin_iva > precio_sin_iva_maximo):
                precio_sin_iva_maximo = precio_sin_iva

        indice=0
        for precio_con_iva in self.lista_precios_con_iva_105:
            precio_sin_iva = precio_con_iva / 1.105
            if(precio_sin_iva_maximo == precio_sin_iva):
                mensaje= "En la pos: {0} - El precio es MAXIMO: {1} - IVA 10.5".format(indice, precio_sin_iva)
                print(mensaje)
            indice = indice + 1 

        indice=0
        for precio_con_iva in self.lista_precios_con_iva_21:
            precio_sin_iva = precio_con_iva / 1.21
            if(precio_sin_iva_maximo == precio_sin_iva):
                mensaje= "En la pos: {0} - El precio es MAXIMO: {1} - IVA 21".format(indice, precio_sin_iva)
                print(mensaje)
            indice = indice + 1   

    def informe_0_bis(self):
        # 0 bis- Valor y posicion frente al IVA del o los Articulo/s sin IVA mas barato/s
        lista_articulos_105_21_sin_iva = []

        for precio_con_iva in self.lista_precios_con_iva_105:
            precio_sin_iva = precio_con_iva / 1.105
            lista_articulos_105_21_sin_iva.append(precio_sin_iva)

        for precio_con_iva in self.lista_precios_con_iva_21:
            precio_sin_iva = precio_con_iva / 1.21
            lista_articulos_105_21_sin_iva.append(precio_sin_iva)

        precio_sin_iva_minimo = None
        for precio_sin_iva in lista_articulos_105_21_sin_iva:
            if(precio_sin_iva_minimo == None or precio_sin_iva < precio_sin_iva_minimo):
                precio_sin_iva_minimo = precio_sin_iva

        indice=0
        for precio_con_iva in self.lista_precios_con_iva_105:
            precio_sin_iva = precio_con_iva / 1.105
            if(precio_sin_iva_minimo == precio_sin_iva):
                mensaje= "En la pos: {0} - El precio es MINIMO: {1} - IVA 10.5".format(indice, precio_sin_iva)
                print(mensaje)
            indice = indice + 1 


        indice=0
        for precio_con_iva in self.lista_precios_con_iva_21:
            precio_sin_iva = precio_con_iva / 1.21
            if(precio_sin_iva_minimo == precio_sin_iva):
                mensaje= "En la pos: {0} - El precio es MINIMO: {1} - IVA 21".format(indice, precio_sin_iva)
                print(mensaje)
            indice = indice + 1 

    def informe_1(self):
        # 1- Valor y posicion frente al IVA del o los Articulo/s mas barato IVA incluido
        lista_articulos_105_21_con_iva = []
        lista_articulos_105_21_con_iva.extend(self.lista_precios_con_iva_105)
        lista_articulos_105_21_con_iva.extend(self.lista_precios_con_iva_21)

        precio_con_iva_minimo = None
        for precio_con_iva in lista_articulos_105_21_con_iva:
            if(precio_con_iva_minimo == None or precio_con_iva < precio_con_iva_minimo):
                precio_con_iva_minimo = precio_con_iva
                
        logitud_lista = len(self.lista_precios_con_iva_21)
        for indice in range(logitud_lista):
            if(self.lista_precios_con_iva_21[indice] == precio_con_iva_minimo):
                mensaje= "En la pos: {0} - El precio es MINIMO: {1} - IVA 21".format(indice, self.lista_precios_con_iva_21[indice])
                print(mensaje)

        logitud_lista = len(self.lista_precios_con_iva_105)
        for indice in range(logitud_lista):
            if(self.lista_precios_con_iva_105[indice] == precio_con_iva_minimo):
                mensaje= "En la pos: {0} - El precio es MINIMO: {1} - IVA 10.5".format(indice, self.lista_precios_con_iva_105[indice])
                print(mensaje)


    # 2- Precio promedio sin IVA
    def informe_2(self):
        acumulador_precios_sin_iva = 0

        for precio_con_iva in self.lista_precios_con_iva_105:
            acumulador_precios_sin_iva = acumulador_precios_sin_iva + (precio_con_iva/1.105)

        for precio_con_iva in self.lista_precios_con_iva_21:
            acumulador_precios_sin_iva = acumulador_precios_sin_iva + (precio_con_iva/1.21)
        
        cantida_precios = len(self.lista_precios_con_iva_105) + len(self.lista_precios_con_iva_21)
        promedio_precios_sin_iva = acumulador_precios_sin_iva / cantida_precios
        print("El precio promedio es: {0}".format(promedio_precios_sin_iva))


    def informe_3(self):
        # 3- Precio promedio con IVA
        lista_articulos_105_21_con_iva = []
        lista_articulos_105_21_con_iva.extend(self.lista_precios_con_iva_105)
        lista_articulos_105_21_con_iva.extend(self.lista_precios_con_iva_21)
        acumulador_precios_con_iva = 0
        for precio_con_iva in lista_articulos_105_21_con_iva:
            acumulador_precios_con_iva = acumulador_precios_con_iva + precio_con_iva
        
        cantida_precios = len(lista_articulos_105_21_con_iva)
        promedio_precios_con_iva = acumulador_precios_con_iva / cantida_precios
        print("El precio promedio es: {0}".format(promedio_precios_con_iva))


    
    # 4- Valor y posicion frente al IVA del o los Articulo/s que son mas caros que el promedio sin IVA
    def informe_4(self):
        acumulador_precios_sin_iva = 0

        for precio_con_iva in self.lista_precios_con_iva_105:
            acumulador_precios_sin_iva = acumulador_precios_sin_iva + (precio_con_iva/1.105)

        for precio_con_iva in self.lista_precios_con_iva_21:
            acumulador_precios_sin_iva = acumulador_precios_sin_iva + (precio_con_iva/1.21)
        
        cantida_precios = len(self.lista_precios_con_iva_105) + len(self.lista_precios_con_iva_21)
        promedio_precios_sin_iva = acumulador_precios_sin_iva / cantida_precios
        print("\nLos valores superiores al precio promedio que es: {0}, son :".format(promedio_precios_sin_iva))
        
        indice = 0
        for precio_con_iva in self.lista_precios_con_iva_105:
            precio_sin_iva = precio_con_iva / 1.105
            if(precio_sin_iva > promedio_precios_sin_iva):
                mensaje= "En la pos: {0} - El precio: {1} - SIN IVA 10.5".format(indice, precio_sin_iva)
                print(mensaje)
                indice = indice + 1

        indice = 0
        for precio_con_iva in self.lista_precios_con_iva_21:
            precio_sin_iva = precio_con_iva / 1.21
            if(precio_sin_iva > promedio_precios_sin_iva):
                mensaje= "En la pos: {0} - El precio: {1} - SIN IVA 21".format(indice, precio_sin_iva)
                print(mensaje)
                indice = indice + 1



    # 5- Valor y posicion frente al IVA del o los Articulo/s que son mas baratos que el promedio sin IVA
    def informe_5(self):
        acumulador_precios_sin_iva = 0

        for precio_con_iva in self.lista_precios_con_iva_105:
            acumulador_precios_sin_iva = acumulador_precios_sin_iva + (precio_con_iva/1.105)

        for precio_con_iva in self.lista_precios_con_iva_21:
            acumulador_precios_sin_iva = acumulador_precios_sin_iva + (precio_con_iva/1.21)
        
        cantida_precios = len(self.lista_precios_con_iva_105) + len(self.lista_precios_con_iva_21)
        promedio_precios_sin_iva = acumulador_precios_sin_iva / cantida_precios
        print("\nLos valores inferiores al precio promedio que es: {0}, son :".format(promedio_precios_sin_iva))
        
        indice = 0
        for precio_con_iva in self.lista_precios_con_iva_105:
            precio_sin_iva = precio_con_iva / 1.105
            if(precio_sin_iva < promedio_precios_sin_iva):
                mensaje= "En la pos: {0} - El precio: {1} - SIN IVA 10.5".format(indice, precio_sin_iva)
                print(mensaje)
                indice = indice + 1

        indice = 0
        for precio_con_iva in self.lista_precios_con_iva_21:
            precio_sin_iva = precio_con_iva / 1.21
            if(precio_sin_iva < promedio_precios_sin_iva):
                mensaje= "En la pos: {0} - El precio: {1} - SIN IVA 21".format(indice, precio_sin_iva)
                print(mensaje)
                indice = indice + 1


    # 6- Valor y posicion frente al IVA del o los Articulo/s que son mas caros que el promedio con IVA
    def informe_6(self):
        acumulador_precios_con_iva = 0
        lista_precios_con_iva_105_21 = []
        lista_precios_con_iva_105_21.extend(self.lista_precios_con_iva_105)
        lista_precios_con_iva_105_21.extend(self.lista_precios_con_iva_21)
        
        for precio_con_iva in lista_precios_con_iva_105_21:
            acumulador_precios_con_iva = acumulador_precios_con_iva + precio_con_iva

        cantida_precios = len(lista_precios_con_iva_105_21)
        precio_promedio_con_iva = acumulador_precios_con_iva / cantida_precios
        print("El precio promedio es: {0}".format(precio_promedio_con_iva))


        cantida_precios_lista_con_iva_105 = len(self.lista_precios_con_iva_105)
        for indice in range(cantida_precios_lista_con_iva_105):
            if(self.lista_precios_con_iva_105[indice] > precio_promedio_con_iva):
                mensaje= "En la pos: {0} - El precio: {1} - CON IVA 105".format(indice, self.lista_precios_con_iva_105[indice])
                print(mensaje)


        cantida_precios_lista_con_iva_21 = len(self.lista_precios_con_iva_21)
        for indice in range(cantida_precios_lista_con_iva_21):
            if(self.lista_precios_con_iva_21[indice] > precio_promedio_con_iva):
                mensaje= "En la pos: {0} - El precio: {1} - CON IVA 21".format(indice, self.lista_precios_con_iva_21[indice])
                print(mensaje)     



    # 7- Valor y posicion frente al IVA del o los Articulo/s que son mas baratos que el promedio con IVA
    def informe_7(self):
        acumulador_precios_con_iva = 0
        lista_precios_con_iva_105_21 = []
        lista_precios_con_iva_105_21.extend(self.lista_precios_con_iva_105)
        lista_precios_con_iva_105_21.extend(self.lista_precios_con_iva_21)
        
        for precio_con_iva in lista_precios_con_iva_105_21:
            acumulador_precios_con_iva = acumulador_precios_con_iva + precio_con_iva

        cantida_precios = len(lista_precios_con_iva_105_21)
        precio_promedio_con_iva = acumulador_precios_con_iva / cantida_precios
        print("El precio promedio es: {0}".format(precio_promedio_con_iva))

        cantida_precios_lista_con_iva_105 = len(self.lista_precios_con_iva_105)
        for indice in range(cantida_precios_lista_con_iva_105):
            if(self.lista_precios_con_iva_105[indice] < precio_promedio_con_iva):
                mensaje= "En la pos: {0} - El precio: {1} - CON IVA 105".format(indice, self.lista_precios_con_iva_105[indice])
                print(mensaje)

        cantida_precios_lista_con_iva_21 = len(self.lista_precios_con_iva_21)
        for indice in range(cantida_precios_lista_con_iva_21):
            if(self.lista_precios_con_iva_21[indice] < precio_promedio_con_iva):
                mensaje= "En la pos: {0} - El precio: {1} - CON IVA 21".format(indice, self.lista_precios_con_iva_21[indice])
                print(mensaje)     



    # 8- Valor y posicion frente al IVA del o los Articulo/s cuyo valor se repite en la lista que integra
    def informe_8(self):
        lista_sin_precios_repetidos = []

        for precios_con_iva in self.lista_precios_con_iva_105:
            if(precios_con_iva not in lista_sin_precios_repetidos):
                lista_sin_precios_repetidos.append(precios_con_iva) #Guardamos en una lista los precios con el incremento que no se repiten

        for precio_unico in lista_sin_precios_repetidos: #Agarramos cada uno de eso elemetos unicos
            cantida_repetidos = 0 #Contamos cuantas veces aparece cada precio unico en esa lista
            for precios_con_iva in self.lista_precios_con_iva_105:
                if(precio_unico == precios_con_iva):
                    cantida_repetidos = cantida_repetidos + 1

            if(cantida_repetidos > 1): #El univo que aparece mas de una vez, es el numero que se imprime
                indice = 0
                for precios_con_iva in self.lista_precios_con_iva_105: #Recorremos la lista completa
                    if(precio_unico == precios_con_iva):  #Que posicion coincide con el 1 (es decir el uno es un numero que se repite, entonces sigo recorriendo la lista y buscando en que posicion este numero se repite, si es que se cumple que se repite.)
                        mensaje= "En la pos: {0} - El precio: {1} - CON IVA 21".format(indice, self.lista_precios_con_iva_21[indice])
                        print(mensaje)  #Y por cada posicion que coincide (que encuentro que el numero se repite)imprimo el mensaje.
                    indice = indice + 1 



    # 9- Valor y posicion frente al IVA del o los Articulo/s cuyo valor NO se repite en la lista que integra
    def informe_9(self):
        lista_sin_precios_repetidos = []
    
        for precios_con_iva in self.lista_precios_con_iva_105:
            if(precios_con_iva not in lista_sin_precios_repetidos):
                lista_sin_precios_repetidos.append(precios_con_iva) 

        for precio_unico in lista_sin_precios_repetidos:
            cantida_repetidos = 0
            for precios_con_iva in self.lista_precios_con_iva_105:
                if(precio_unico == precios_con_iva):
                    cantida_repetidos = cantida_repetidos + 1

            if(cantida_repetidos == 1):
                indice = 0
                for precios_con_iva in self.lista_precios_con_iva_105:
                    if(precio_unico == precios_con_iva):
                        mensaje= "En la pos: {0} - El precio: {1} - CON IVA 21".format(indice, self.lista_precios_con_iva_21[indice])
                        print(mensaje)    
                    indice = indice + 1 
        


                





    





if __name__ == "__main__":
    app = App()
    app.mainloop()    