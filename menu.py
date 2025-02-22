from GestionTechVille import Producto
from textwrap import dedent

productos = []

def menu():
    while True:
        print()
        print("#"*30)
        print("BIENVENIDO A LA PLATAFORMA DE TECHVILLE")
        print("#"*30)
    
        print(dedent("""
              1. Agregar Productos.
              2. Ver Carrito de Compra.
              3. Eliiminar Producto del Carrito.
              4. Finalizar compra.
              5. Generar Recibo.
              6. Salir.
          """))
    
        while True:
            try:
                opcion = int(input("Por favor ingrese una opción: "))
                break
            except ValueError:
                print("El tipo de dato ingresado no es valido. Por favor intente nuevamente")
                input("Presione <Enter> para continuar")
    
        if opcion == 1:
            Producto.agregarProductos(productos)
        
        elif opcion == 2:
            Producto.verCarrito(productos)
        
        elif opcion == 3:
            Producto.eliminarProducto(productos)
        
        elif opcion == 4:
            Producto.finalizarCompra(productos)
    
        elif opcion == 5:
            Producto.generarRecibo(productos)
                
        elif opcion == 6:
            print("Gracias por usar nuestra plataforma. Hasta pronto!!")
            break
        
        else:
            print("La opcion ingresada no es valida. Por favor intente nuevamente.")
            input("Presione <Enter> para continuar")
        
    