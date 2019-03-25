import os
from sqlite3 import dbapi2

"""
    Genera la base de datos y le mete unos datos iniciales.
"""
try:
    ###Creamos la base de datos
    baseDatos = dbapi2.connect("BaseDeDatos.dat")
    ###Un corsor para lanzar el sql
    cursor = baseDatos.cursor()

    ###Creamos las tablas de la base
    cursor.execute("create table proveedores(id text, nombre text,CIF text, direccion text, telefono text, correo text)")
    cursor.execute("create table productos(id text, nombre text , descripcion text, cantidadStock number, precioUnidad number,idProv text)")
    cursor.execute("create table facturasClientes(idFactura number, nombreCliente text, telefono text, direccion text, correo text)")
    cursor.execute("create table facturasInfo(idFactura number,idProducto text, cantidad number)")

    ###Añadimos datos a las tablas
    cursor.execute("insert into proveedores values('prov1','Petuky','111-222-333','Av. Rosalia Nº3','986524123','petuky@gmail.com')")
    cursor.execute("insert into proveedores values('prov2','Dinapet','444-555-666','C. Que Locura Nº4','988789563','dinapet@gmail.com')")

    cursor.execute("insert into productos values('pro1','Brekkies Pienso','Para Perros 15 kg', 7, 23.80,'prov1')")
    cursor.execute("insert into productos values('pro2','Ultima Pienso','Perro Adulto 7kg', 10, 24.95, 'prov2')")

    cursor.execute("insert into facturasClientes values(1,'Pepa Bueno','658741236','C. La Lameda Nº7','pepiña@gmail.com')")

    cursor.execute("insert into facturasInfo values(1,'pro1',2)")
    cursor.execute("insert into facturasInfo values(1,'pro2',1)")

    ###Guardamos los datos en la BD
    baseDatos.commit()

except (dbapi2.DatabaseError):
    print(" ERROR EN LA BASE DE DATOS")
finally:
    print("Cerramos la conexion a la BD")
    cursor.close()
    baseDatos.close()