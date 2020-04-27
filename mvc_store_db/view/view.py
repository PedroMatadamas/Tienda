class View:
    """
    *************************
    * A view for a store DB *
    *************************
    """
    def start(self):
        print('================================')
        print('= Bienvenido a nuestra tienda! =')
        print('================================')

    def end(self):
        print('================================')
        print('=        Hasta la vista!       =')
        print('================================')

    def main_menu(self):
        print('================================')
        print('=        Menu Principal        =')
        print('================================')
        print('1. CPs')
        print('2. Productos')
        print('3. Clientes')
        print('4. Ordenes')
        print('5. Salir')

    def option(self,last):
        print('Selecciona un opcion (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('Opcion no valida!\nIntenta de nuevo')
    
    def ask(self, output):
        print(output, end = '' )
    
    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))
    
    def error(self, err):
        print(' Error! '.center(len(err)+4,'-'))
        print('-'+err+'-')
        print('-'*(len(err)+4))
    
    def zips_menu(self):
        print('*********************')
        print('* -- Submenu CPs -- *')
        print('*********************')
        print('1. Agregar CP')
        print('2. Mostrar CP')
        print('3. Mostrar todos los CPs')
        print('4. Mostrar CPs de una ciudad')
        print('5. Actualizar CP')
        print('6. Borrar CP')
        print('7. Regresar')
    
    def show_a_zip(self, record):
        print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}')
    
    def show_zip_header(self, header):
        print(header.center(78,'*'))
        print('CP'.ljust(6)+'|'+'Ciudad'.ljust(35)+'|'+'Estado'.ljust(35))
        print('-'*78)

    def show_zip_midder(self):
        print('-'*78)
    
    def show_zip_footer(self):
        print('-'*78)

    """
    ***********************
    * A view for products *
    ***********************
    """
    def products_menu(self):
        print('*************************')
        print('* -- Submenu Products -- *')
        print('*************************')
        print('1. Agregar Producto')
        print('2. Mostrar Producto')
        print('3. Mostrar todos los Productos')
        print('4. Mostrar Productos de una marca')
        print('5. Mostrar productos en rango de precios')
        print('6. Actualizar Producto')
        print('7. Borrar Productos')
        print('8. Regresar')
    
    def show_a_product(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Marca:', record[2])
        print('Descripcion:', record[3])
        print('Precio:', record[4])
    
    def show_product_header(self, header):
        print(header.center(48,'*'))
        print('-'*78)

    def show_product_midder(self):
        print('-'*48)
    
    def show_product_footer(self):
        print('-'*78)
    
    """
    *****************/****
    * A view for clients *
    **********************
    """
    def Clients_menu(self):
        print('*************************')
        print('* -- Submenu clients -- *')
        print('*************************')
        print('1. Agregar Cliente')
        print('2. Mostrar Cliente')
        print('3. Mostrar todos los Clientes')
        print('4. Mostrar Clientes de un CP')
        print('5. Actualizar Cliente')
        print('6. Borrar Cliente')
        print('7. Regresar')
    
    def show_a_client(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Apellido paterno:', record[2])
        print('Apellido materno:', record[3])
        print('Calle:', record[4])
        print('No exterior:', record[5])
        print('No interior:', record[6])
        print('Colonia:', record[7])
        print('Ciudad:', record[11])
        print('Estado:', record[12])
        print('CP:', record[8])
        print('Email:', record[9])
        print('Telefono:', record[10])
    
    def show_a_Client_brief(self,record):
        print('ID:', record[0])
        if record[3] == None:
            print('Nombre:', record[1]+' '+record[2]+' ')
        else:
            print('Nombre:', record[1]+' '+record[2]+' '+ record[3])
        if record[6] == None:
            print('Calle:', record[4]+' '+ record[5]+' '+' '+ record[7])
        else:    
            print('Calle:', record[4]+' '+ record[5]+' '+ record[6]+' '+ record[7])
        print('Ciudad:', record[11]+' '+ record[12]+' '+record[8])
        print('Email:', record[9])
        print('Telefono:', record[10])

    def show_client_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)

    def show_client_midder(self):
        print('-'*53)
    
    def show_client_footer(self):
        print('-'*53)
    
    """
    *****************/****
    * A view for orders *
    **********************
    """
    def orders_menu(self):
        print('*************************')
        print('* -- Submenu Ordenes -- *')
        print('*************************')
        print('1. Agregar Orden')
        print('2. Leer Orden')
        print('3. Leer todas las Ordenes')
        print('4. Leer ordenes de una fecha')
        print('5. Leer ordenes de un cliente')
        print('6. Actualizar datos de orden')
        print('7. Agregar productos a una orden')
        print('8. Modificar productos de una orden')
        print('9. Borrar productos de una orden')
        print('10. Borrar orden')
        print('11. Regresar')
    
    def show_order(self, record):
        print('ID:', record[0])
        print('Estado de la orden',record[2])
        print('Fecha:', record[3])
        print('Datos del Cliente'.center(81,'*'))
        self.show_a_Client_brief(record[5:])
    
    def show_order_header(self, header):
        print(header.center(81,'+'))


    def show_order_midder(self):
        print('/'*81)
    
    def show_order_total(self, record):
        print('Total de la orden '+str(record[4]))

    def show_order_footer(self):
        print('-'*53)
    """
    *****************************
    * A view for orders details *
    *****************************
    """
    def show_a_order_details(self, record):
        print(f'{record[0]:<5}|{record[1]:<20}|{record[2]:<20}|{record[3]:<11}|{record[4]:<9}|{record[5]:<11}:')
    
    def show_order_details_header(self):
        print('-'*81)
        print('ID'.ljust(5)+'|'+'Producto'.ljust(20)+'|'+'Marca'+'|'+'Precio'.ljust(11)+'|'+'Cantidad'.ljust(9)+'|'.ljust(11))
        print('-'*81)

    def show_order_details_footer(self):
        print('-'*81)