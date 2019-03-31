Tienda de Mascotas
*******************
Este manual describe las distintas funcionalidades de la aplicacion **Tienda de Mascotas** que nos ayudara a administrar una tienda de animales.

La aplicacion esta formada por 5 ventanas:
 * Tienda Mascotas
 * Nuevo Proveedor
 * Lista Proveedores
 * Inventario
 * Crear Factura

Tienda Mascotas
+++++++++++++++
Esta es la ventana principal de la aplicacion. A partir de esta ventana podremos acceder a las otras ventanas y cambiar de una otra.

.. figure:: ./_static/TiendaMascotas.png
    :align: center


Nuevo Proveedor
+++++++++++++++++++

En esta ventana podemos añadir un nuevo provvedor de la tienda de animales. Podremos añadir el nombre, el CIF, la direccion, el telefono y el correo.

.. figure::  ./_static/NuevoProveedor.png
    :align: center


Ademas a cada proveedor se le genera un codigo unico a partir del ultimo proveedor introducido::

     cursorID = cursor.execute("SELECT id FROM 'proveedores' ORDER BY id DESC LIMIT 1")
     lastid = cursorID.fetchone()[0].split("prov")
     idNuevo = "prov" + str(int(lastid[1]) + 1)


Lista Proveedores
++++++++++++++++++

En esta ventana se muestra una lista con todos los datos de los proveedores.

.. figure::  ./_static/ListaProveedores.png
    :align: center


Si seleccionamos un elemenoto de la lista y clickamos el boton **BORRAR** el proveedor quedará eliminado de la Base de datos.

Por el contrario, si clicamos en el boton **MODIFICAR** se cargara en un formulario, que se hará visible, los datos del proveedor seleccionado y se podran modificar los datos de dicho proveedor.

Inventario
+++++++++++

En esta ventana se muestra una lista con todos los productos disponibles en la tienda.

.. figure::  ./_static/Inventario.png
    :align: center

La informacion que se muestra es el nombre del prodcuto, una breve descripcion, el numero de unidades que se tienen del producto, es decir, el stock, el precio de cada unidad y el prooveedor de dicho producto.

Ademas cada producto tiene un id unico que se genera a partir del id del producto anterior::

     cursorID = cursor.execute("SELECT id FROM 'productos' ORDER BY id DESC LIMIT 1")
     lastid = cursorID.fetchone()[0].split("pro")
     idNuevo = "pro" + str(int(lastid[1]) + 1)

Si seleccionamos un elemento de la lista y clickamos el boton **BORRAR** el producto quedará eliminado de la Base de datos.

Por el contrario, si clicamos en el boton **MODIFICAR** se cargara en un formulario, que se hará visible, los datos del producto seleccionado y se podran modificar los datos de dicho producto.

Luego, si clicamos **AÑADIR** se nos mostrara el fromulario vacio y podremos añadir un nuevo producto con su id generado automaticamente.

Por ultimo, podemos clicar el boton **GENERAR INVENTARIO** que nos generara un PDF con todos los productos que contiene la tienda.

Crear Factura
++++++++++++++

Esta ventana nos permite crear y generar una factura para un cliente de la tienda. Primero podemos introducir la informacion del cliente que nos va a hacer una compra.

.. figure:: ./_static/crearFactura.png
    :align: center

Luego seleccionamos los productos que el cliente quiere adquirir y lo añadimos a la lista. Al final guardamos la informacion en el boton **GUARDAR** y esta quedara almacenada en la base de datos.
Despues de guardarla, podemos generar la factura que deseemos. Tanto la que hemos guardado ahora como alguna factura antigua.
Al clicar el boton **GENERAR FACTURA** se creera un PDF con la informacion del cliente y la lista de productos adquirdos con su precio total.


