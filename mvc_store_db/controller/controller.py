from model.model import Model
from view.view import View
from datetime import date
 
class Controller:
    """
    *******************************
    * A controller for a store DB *
    *******************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):
        self.view.start()
        self.main_menu()

    """
    ***********************
    * General controllers *
    ***********************
    """   
    def main_menu(self):
        o = '0'
        while o != '5':
            self.view.main_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.zips_menu()
            elif o == '2':
                self.products_menu()
            elif o == '3':
                self.clients_menu()
            elif o == '4':
                self.orders_menu()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self, fs , vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals

    """
    ********************
    * General for zips *
    ********************
    """
    def zips_menu(self):
        o = '0'
        while o != '7':
            self.view.zips_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_zip()
            elif o == '2':
                self.read_a_zip()
            elif o == '3':
                self.read_all_zips()
            elif o == '4':
                self.read_zips_city()
            elif o == '5':
                self.update_zip()
            elif o == '6':
                self.delete_zip()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_zip(self):
        self.view.ask('Ciudad: ')
        city = input()
        self.view.ask('Estado: ')
        state = input()
        return [city,state]
    
    def create_zip(self):
        self.view.ask('CP: ')
        i_zip = input()
        city, state = self.ask_zip()
        out = self.model.create_zip(i_zip,city,state)
        if out == True:
            self.view.ok(i_zip, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('El CP esta repetido')
            else:
                self.view.error('No se pudo agregar el CP')
        return

    def read_a_zip(self):
        self.view.ask('CP: ')
        i_zip = input()
        zip = self.model.read_a_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_zip_header('Datos del CP  '+i_zip+' ')
            self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            if zip == None:
                self.view.error('El CP no existe')
            else:
                self.view.error('Hay un problema al leer el CP')
        return
    
    def read_all_zips(self):
        zips = self.model.read_all_zips()
        if type(zips) ==  list:
            self.view.show_zip_header(' Todos los CPs ')
            for zip in zips:
                self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            self.view.error('Hay un problema al leer los CPs ')
        
    def read_zips_city(self):
        self.view.ask('Ciudad: ')
        city = input()
        zips = self.model.read_zips_city(city)
        if type(zips) == list:
            self.view.show_zip_header('CP para la ciudad de  '+city+' ')
            for zip in zips:
                self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            self.view.error('Hay un problema al leer los CPs ')
        return

    def update_zip(self):
        self.view.ask('CP a modificar: ')
        i_zip = input()
        zip = self.model.read_a_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_zip_header(' Datos del CP '+i_zip+' ')
            self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            if zip == None:
                self.view.error('El CP no existe')
            else:
                self.view.error('Hay un problema al leer el CP')
            return
        self.view.msg(' Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals =self.ask_zip()
        fields, vals = self.update_lists(['z_city','z_state'], whole_vals)
        vals.append(i_zip)
        vals = tuple(vals)
        out = self.model.update_zip(fields,vals)
        if out == True:
            self.view.ok(i_zip, 'actualizo')
        else: 
            self.view.error('No se pudo actualizar el CP')
        return
        
    def delete_zip(self):
        self.view.ask('CP a borrar: ')
        i_zip = input()
        count = self.model.delete_zip(i_zip)
        if count != 0:
            self.view.ok(i_zip, 'borro')
        else:
            if count == 0:
                self.view.error('El CP no exite')
            else:
                self.view.error('Problema al borrar el CP')
        return
    
    """ 
    ***************************
    * Controllers for products*
    ***************************
    """

    def products_menu(self):
        o = '0'
        while o != '8':
            self.view.products_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_product()
            elif o == '2':
                self.read_a_product()
            elif o == '3':
                self.read_all_products()
            elif o == '4':
                self.read_products_brand()
            elif o == '5':
                self.read_products_price_range()
            elif o == '6':
                self.update_product()
            elif o == '7':
                self.delete_product()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_poduct(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Marca: ')
        brand = input()
        self.view.ask('Descripcion: ')
        descrip = input()
        self.view.ask('Precio: ')
        price = input()
        return [name, brand,descrip,price]
    
    def create_product(self):
        name, brand, descrip, price = self.ask_poduct()
        out = self.model.create_product(name, brand, descrip, price)
        if out == True:
            self.view.option(name+' '+ 'agrego')
        else:
            self.view.error('No se pudo agregar el producto')
        return

    def read_a_product(self):
        self.view.ask('ID producto: ')
        id_producto = input()
        product = self.model.read_a_product(id_producto)
        if type(product) == tuple:
            self.view.show_product_header('Datos del producto  '+id_producto+' ')
            self.view.show_a_product(product)
            self.view.show_product_midder()
            self.view.show_product_footer()
        else:
            if product == None:
                self.view.error('El producto no existe')
            else:
                self.view.error('Hay un problema al leer el producto')
        return
    
    def read_all_products(self):
        products = self.model.read_all_products()
        if type(products) ==  list:
            self.view.show_product_header(' Todos los productos ')
            for product in products:
                self.view.show_a_product(product)
            self.view.show_product_midder()
            self.view.show_product_footer()
        else:
            self.view.error('Hay un problema al leer los productos ')

    def read_products_brand(self):
        self.view.ask('Marca: ')
        brand = input()
        products = self.model.read_a_products_brand(brand)
        if type(products) == list:
            self.view.show_order_header('Producto de la marca '+brand+' ')
            for product in products:
                self.view.show_a_product(product)
                self.view.show_product_midder
            self.view.show_product_footer()
        else:
            self.view.error('Problema al leer los prodcutos')
        return
    
    def read_products_price_range(self):
        self.view.ask('Precio inferior: ')
        price_ini = input()
        self.view.ask('Precio superior: ')
        price_end = input()
        products = self.model.read_a_products_price_range(float(price_ini),float(price_end))
        if type(products) == list:
            self.view.show_product_header(' Productos entre '+price_ini+' y '+price_end+' ')
            for product in products:
                self.view.show_a_product(product)
                self.view.show_product_midder()
            self.view.show_product_footer
        else:
            self.view.error('Problema al leer los productos')
        return
    
    def update_product(self):
        self.view.ask(' ID de producto a modificar: ')
        id_product = input()
        product = self.model.read_a_product(id_product)
        if type(product) == tuple:
            self.view.show_product_header(' Datos del produtco '+id_product+' ')
            self.view.show_a_product(product)
            self.view.show_product_midder
            self.view.show_product_footer()
        else:
            if product == None:
                self.view.error('El producto no existe')
            else:
                self.view.error('Problema al leer el producto')
            return
        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_poduct()
        fields, vals = self.update_lists(['p_name','p_brand','p_descrip','p_price'],whole_vals)
        vals.append(id_product)
        vals = tuple(vals)
        out = self.model.update_product(fields,vals)
        if out == True:
            self.view.ok(id_product, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return

    def delete_product(self):
        self.view.ask('ID de producto a borrar: ')
        id_product = input()
        count = self.model.delete_product(id_product)
        if count != 0:
            self.view.ok(id_product, 'Borro')
        else:
            if count == 0:
                self.view.error('El produco no exite')
            else:
                self.view.error('Prblema al borrar el producto')
        return

    """ 
    ***************************
    * Controllers for clients*
    ***************************
    """    

    def clients_menu(self):
        o = '0'
        while o != '7':
            self.view.Clients_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_client()
            elif o == '2':
                self.read_a_client()
            elif o == '3':
                self.read_all_clients()
            elif o == '4':
                self.read_client_zip()
            elif o == '5':
                self.update_client()
            elif o == '6':
                self.delete_client()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_client(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        sname1 = input()
        self.view.ask('Apellido Materno: ')
        sname2 = input()
        self.view.ask('Calle: ')
        street = input()
        self.view.ask('No exterior: ')
        noext = input()
        self.view.ask('No interior: ')
        noint = input()
        self.view.ask('Colonia: ')
        col = input()
        self.view.ask('CP: ')
        zip = input()
        self.view.ask('Email: ')
        email = input()
        self.view.ask('telefono: ')
        phone = input() 
        return(name,sname1,sname2,street,noext,noint,col,zip,email,phone)   
        
    def create_client(self):
        name,sname1,sname2,street,noext,noint,col,zip,email,phone = self.ask_client()
        out = self.model.create_client(name,sname1,sname2,street,noext,noint,col,zip,email,phone)
        if out == True:
            self.view.ok(name+' '+sname1+' '+sname2, 'agrego')
        else:
            self.view.error('No se pudo agregar cliente')
        return

    def read_a_client(self):
        self.view.ask('ID cliente: ')    
        id_client = input()
        client = self.model.read_a_client(id_client)
        if type(client) == tuple:
            self.view.show_client_header('Datos del cliente  '+id_client+' ')
            self.view.show_a_client(client)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            if client == None:
                self.view.error('El cliente no existe')
            else:
                self.view.error('Hay un problema al leer el cliente')
        return              
    
    def read_all_clients(self):
        clients = self.model.read__all__clients()
        if type(clients) == list:
            self.view.show_client_header(' Todos los clientes ')
            for client in clients:
                self.view.show_a_client(client)
                self.view.show_zip_midder()
            self.view.show_zip_footer
        else:
            self.view.error('Problema al leer los clientes')
        return
    
    def read_client_zip(self):
        self.view.ask('CP: ')
        zip = input()
        clients = self.model.read_a_client_zip(zip)
        if type(clients) == list:
            self.view.show_client_header('Clientes con el cp '+zip+' ')
            for client in clients:
                self.view.show_a_client(client)
                self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            self.view.error('Problema al leer los clientes')
        return
    
    def update_client(self):
        self.view.ask('ID de cliente a modificar: ')
        id_client = input()
        client = self.model.read_a_client(id_client)
        if type(client) == tuple:
            self.view.show_client_header(' Datos del cliente '+id_client+ ' ')
            self.view.show_a_client(client)
            self.view.show_client_midder()
            self.view.show_product_footer
        else:
            if client == None:
                self.view.error('El cliente no existe')
            else:
                self.view.error('Problema al leer el cliente')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_client()
        fields, vals = self.update_lists(['c_fname','c_sname1','c_sname2','c_noext','c_noint','c_col','c_zip','c_email','c_phone'], whole_vals)
        vals.append(id_client)
        vals = tuple(vals)
        out = self.model.update_client(fields,vals)
        if out == True:
            self.view.ok(id_client, 'actualizo')
        else:
            self.view.error('Error no se pudo actualizar el cliente')
        return
    
    def delete_client(self):
        self.view.ask('ID de cliente a borrar: ')
        id_client = input()
        count = self.model.delete_client(id_client)
        if count != 0:
            self.view.ok(id_client, 'Borro')
        else:
            if count == 0:
                self.view.error('El cliente no exite')
            else:
                self.view.error('Prblema al borrar el cliente')
        return
    
    """ 
    **************************
    * Controllers for orders *
    **************************
    """    

    def orders_menu(self):
        o = '0'
        while o != '11':
            self.view.orders_menu()
            self.view.option('11')
            o = input()
            if o == '1':
                self.create_order()
            elif o == '2':
                self.read_a_order()
            elif o == '3':
                self.read_all_orders()
            elif o == '4':
                self.read_orders_date()
            elif o == '5':
                self.read_orders_client()
            elif o == '6':
                self.update_orders()
            elif o == '7':
                self.add_order_details()
            elif o == '8':
                self.update_order_details()
            elif o == '9':
                self.delete_order_details()
            elif o == '10':
                self.delete_order()
            elif o == '11':
                return
            else:
                self.view.not_valid_option()
        return

    def create_order(self):
        self.view.ask('ID cliente: ')
        id_cliente = input()
        o_status = 'PROCESSIN'
        today = date.today()
        o_date = today.strftime('%y-%m-%d')
        o_total =  0.0
        id_order = self.model.create_order(id_cliente, o_status, o_date, o_total)
        if type(id_order) == int:
            id_product = ' '
            while id_product != '':
                self.view.msg('--- Agrega productos a la ordej (deja vacio el id del producto para salir ---')
                id_product, od_total = self.create_order_details(id_order)
                o_total += od_total
            self.model.update_order(('o_total = %s',),(o_total, id_order))
        else:
            self.view.error('No se pudo crear la orden')
        return


    def read_a_order(self):
        self.view.ask('ID order: ')
        id_order = input()
        order = self.model.read_a_order(id_order)
        if type(order) == tuple:
            order_details = self.model.read_order_details(id_order)
        
            if type(order_details) != list and order_details != None:
                self.view.error('Problema al leer la orden')
            else:
                self.view.show_order_header('Datos de la orden '+id_order+' ')
 
                self.view.show_order(order)

                self.view.show_order_details_header()

                for order_detail in order_details:
                    self.view.show_a_order_details(order_detail)
                self.view.show_order_details_footer()
                self.view.show_order_total(order)
                self.view.show_order_footer()
                return order
        else:
            if order == None:
                self.view.error('La orden no existe')
            else:
                self.view.error('Problema al leer la orden')
        return

    def read_all_orders(self):
        orders = self.model.read_all_orders()
        if type(orders) == list:
            self.view.show_order_header(' Todas las ordenes ')
            for order in orders:
                id_order = order[0]
                order_details = self.model.read_order_details(id_order)
                if type(order_details) != list and order_details != None:
                    self.view.error('Problema al leer la orden '+id_order+'. REVISA .')
                else:
                    self.view.show_order(order)
                    self.view.show_order_details_header()
                    for order_detail in order_details:
                        self.view.show_a_order_details(order_detail)
                    self.view.show_order_details_footer()
                    self.view.show_order_total(order)
                    self.view.show_order_midder()
            self.view.show_order_footer
        else:
            self.view.error('Problema al leer las ordenes')
        return

    def read_orders_date(self):
        self.view.ask('Fecha: ')
        date = input()
        orders = self.model.read_orders_date(date)
        if type(orders) == list:
            self.view.show_order_header(' Ordenes para la fecha '+date+' ')
            for order in orders:
                id_order = order[0]
                order_details = self.model.read_order_details(id_order)
                if type(order_details) != list and order_details != None:
                    self.view.error('Problema al leer la orden'+id_order+' .Revisa. ')
                else:
                    self.view.show_order(order)
                    self.view.show_order_details_header()
                    for order_detail in order_details:
                        self.view.show_a_order_details(order_detail)
                    self.view.show_order_details_footer()
                    self.view.show_order_total(order)
                    self.view.show_order_midder()
        else:
            self.view.error('Problemas a leer las ordenes')
        return

    def read_orders_client(self):
        self.view.ask('ID cliente: ')
        id_client = input()
        orders = self.model.read_orders_client(id_client)
        if type(orders) == list:
            self.view.show_order_header(' Ordnes para el cliente '+id_client+' ')
            for order in orders:
                id_order = order[0]
                order_details = self.model.read_order_details(id_order)
                if type(order_details) != list and order_details != None:
                    self.view.error('Problema al leer la orden '+id_order+' .Revisa ')
                else:
                    self.view.show_order(order)
                    self.view.show_order_details_header()
                    for order_detail in order_details:
                        self.view.show_a_order_details(order_detail)
                    self.view.show_order_details_footer()
                    self.view.show_order_total(order)
                    self.view.show_order_midder
            self.view.show_order_footer()
        else:
            self.view.error('Problema al leer las ordenes')
        return


    def update_orders(self):
        self.view.ask('ID orden a modificar')
        id_orden = input()
        order = self.model.read_a_order(id_orden)
        if type(order) == tuple:
            self.view.show_order_header('Datos de la orden'+id_orden+' ')
            self.view.show_order(order)
            self.view.show_order_total(order)
            self.view.show_order_footer()
        else:
            if id_orden == None:
                self.view.error('La orden no exite')
            else:
                self.view.error('Problema al leer la orden')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        self.view.ask('ID cliente: ')
        id_client = input()
        self.view.ask('Estado (processing,acepted, sent recived): ')
        o_status = input()
        self.view.ask('Fecha (yyyy/mm/dd): ')
        o_date = input()
        whole_vals = [id_client,o_status, o_date]
        fields,vals = self.update_lists(['id_client','o_status', 'o_date'], whole_vals)
        vals.append(id_orden)
        vals = tuple(vals)
        out = self.model.update_order(fields,vals)
        if out == True:
            self.view.ok(id_orden, ' se actualizo')
        else:
            self.view.error('No se pudo actualizar la orden')
        return

    def delete_order(self):
        self.view.ask('ID de orden a borrar: ')
        id_order = input()
        count = self.model.delete_order(id_order)
        if count != 0:
            self.view.ok(id_order, 'Borro')
        else:
            if count == 0:
                self.view.error('La orden no exite')
            else:
                self.view.error('Problema al borrar la orden')
        return

    """ 
    **********************************
    * Controllers for orders details *
    **********************************
    """   

    def create_order_details(self, id_order):
        od_total = 0.0
        self.view.ask('ID producto: ')
        id_product = input()
        if id_product != '':
            product = self.model.read_a_product(id_product)
            if type(product) == tuple:
                self.view.show_product_header(' Datos del producto '+id_product+' ')
                self.view.show_a_product(product)
                self.view.show_product_footer()
                self.view.ask('Cantidad: ')
                od_amount = int(input())

                od_total = od_amount*product[4]
                out = self.model.create_order_detail(id_order, id_product,od_amount, od_total)
                if out == True:
                    self.view.ok(product[1]+' '+product[2], 'agrego a la orden')
                else:
                    if out.errno == 1062:
                        self.view.error(' El producto ya esta en la orden')
                    else:
                        self.view.error('No se pudo agregar el producto')
                    od_total = 0.0
            else:
                if product == None:
                    self.view.error('El produdcto no existe')
                else:
                    self.view.error('Problema al leer el producto')
        return id_product, od_total

    def add_order_details(self):
        order = self.read_a_order()
        if type(order) == tuple:
            id_order = order[0]
            o_total = order[4]
            id_product = ' '
            while id_product != '':
                self.view.msg('--- Agrega productos a la orden (deja vacio el id del producto para salir) ---')
                id_product, od_total = self.create_order_details(id_order)
                o_total += od_total
            self.model.update_order(('o_total = %s',),(o_total,id_order))
        return

    def update_order_details(self):
        order = self.read_a_order()
        if type(order) == tuple:
            id_order = order[0]
            o_total = order[4]
            id_product = ' '
            while id_product != '':
                self.view.msg('--- Modifica productos de la orden (deja vacio el id del producto para salir) ---')
                self.view.ask('ID producto: ')
                id_product = input()
                if id_product != '':
                    order_detail = self.model.read_order_detail(id_order, id_product)
                    print(order_detail)
                    if type(order_detail) == tuple:
                        od_total_old = order_detail[5]
                        o_total -= od_total_old
                        product = self.model.read_a_product(id_product)
                        price = product[4]
                        self.view.ask('Cantidad: ')
                        od_amount = int(input())
                        od_total = price*od_amount
                        o_total += od_total
                        fields, whole_vals = self.update_lists(['od_amount','od_total'],[od_amount,od_total])
                        whole_vals.append(id_order)
                        whole_vals.append(id_product)
                        self.model.update_order_details(fields, whole_vals)
                        self.view.ok(id_product, 'actrualizo la orden')
                    else:
                        if order_detail == None:
                            self.view.error('El producto no existe')
                        else:
                            self.view.error('Problema al actualizar el producto :(')
            self.model.update_order(('o_total = %s',),(o_total, id_order))
        return

    def delete_order_details(self):
        order = self.read_a_order()
        if type(order) == tuple:
            id_order = order[0]
            o_total = order[4]
            id_product = ' '
            while id_product != '':
                self.view.msg('--- Borrar productos de la orden (deja vacio el id del producto para salir) ---')
                self.view.ask('ID producto: ')
                id_product = input()
                if id_product != '':
                    order_detail = self.model.read_order_detail(id_order,id_product)
                    count = self.model.delelete_oder_details(id_order,id_product)
                    if type(order_detail) == tuple and count != 0:
                        od_total = order_detail[5]
                        o_total -= od_total
                        self.view.ok(id_product, 'borro la orden ')
                    else:
                        if order_detail == None:
                            self.view.error('El producto no existe en la orden')
                        else:
                            self.view.error('Problema al borrar el producto')
            self.model.update_order(('o_total = %s',),(o_total, id_order))
        return

