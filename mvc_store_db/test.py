# from model.model import Model
# m = Model()

# data = m.read_orders_client(13)
# print(data)

# m.create_zip('36700','Salamanca','Guanajuato')
# m.create_zip('36783','Salamanca','Guanajuato')
# m.create_zip('76001','Queretaro','Queretaro')

# m.create_client('Ana','Hernandez','Lopez','Hidalgo','34',None,'Centro','76001','ana.hernandez@gmail.com','1364825972')
# m.create_client('Pedro','Matadamas',None,'Liatris','121',None,'Floresta','36783','pedro_matadamas@hotmail.com','4641661118')
# m.create_client('Sofia','Matadamas',None,'Revolcion','201',None,'Centro','36700','sofia.matadamas@gmail.com','4646473350')
# m.create_client('Pedro','Matadamas',None,'Liatris','121',None,'Floresta','36783','pedro_matadamas@hotmail.com','4641661118')

# data = m.read_a_zip('36700')
# print(data.city)

# m.update_zip('36700','Sanjuan de Razos','')

# m.update_zip('36790','','Jalisco')
# data = m.read__all__zips()
# print(data)

# data = m.read_zips_city('Salamanca')
# print(data)

# data = m.read__all__zips()
# print(data)
# m.delete_zip('36783')
# data = m.read__all__zips()
# print(data)

# m.create_product('Jabon','La corona','Jabron de 1 Kg',35)
# m.create_product('Leche','Lala','Presentacion tetrapack',22.5)
# m.create_product('Clorox 1Lt','Clorox','Limpiador liquido',37.5)


#data = m.read__all__products()
#print(data)

# products = m.read_a_products_price_range(30,40)
# print(products)

# data = m.read_a_products(3)
# print(data)

# fields = ('p_price = %s',)
# vals =(20.5,3)
# products = m.update_product(fields,vals)

# data = m.read__all__products()
# print(data)

# m.delete_product(2)
# data = m.read__all__products()
# print(data)

# data = m.read_a_products_brand('Kellogs')
# print(data)

# data = m.read_a_client_zip('36700')
# print(data)



# fields = ('c_zip = %s',)
# vals =(36783,3)
# m.update_client(fields,vals)
# client = m.read__all__clients()
# print(client)



# m.close_db()

from controller.controller import Controller

c = Controller()

c.start()