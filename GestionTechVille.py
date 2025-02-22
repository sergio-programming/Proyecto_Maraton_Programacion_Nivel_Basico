import datetime
from textwrap import dedent

class Producto:
    def __init__(self, nombreProducto, cantidadProducto, precioProducto):
        self._nombreProducto = nombreProducto
        self._cantidadProducto = cantidadProducto
        self._precioProducto = precioProducto

    def agregarProductos(productos: list):
        print()
        print("#"*30)
        print("AGREGAR PRODUCTOS")
        print("#"*30)
        while True:
            try:
                nroProductos = int(input("\nPor favor ingrese la cantidad de productos a comprar: ").strip())
                if nroProductos <= 0:
                    raise ValueError("La cantidad de productos no puede ser negativa.")
                break  # Sale del bucle si la entrada es válida
            except ValueError as e:
                print(f"\nError: {e}. Por favor intente nuevamente.")
                
        for i in range(nroProductos):
            while True:
                print(f"\nRegistre el producto #{i+1}")
                try:
                    nombreProducto = input("Por favor ingrese el nombre del producto: ").strip()
                    cantidadProducto = int(input("Por favor ingrese la cantidad del producto: ").strip())
                    precioProducto = float(input("Por favor ingrese el precio del producto: ").strip())
                    if not nombreProducto or not cantidadProducto or not precioProducto:
                        raise ValueError(f"Todos los campos son obligatorios. Por favor intente nuevamente.")
                    break
                except ValueError as e:
                    print(f"\nError: {e}")
                    
            producto = Producto(nombreProducto, cantidadProducto, precioProducto)
            productos.append(producto)
        
        if nroProductos == 1:
            print(f"Producto agregado exitosamente.")
        else:
            print(f"Productos agregados exitosamente.")
            
    def verCarrito(productos: list):
        print()
        print("#"*30)
        print("CARRITO DE COMPRA")
        print("#"*30)
        
        if not productos:
            print("\nEl carrito está vacío.")
            return
        
        for i, producto in enumerate(productos, start=1):
            print(dedent(f"""
                Producto #{i}
                Nombre de Producto: {producto._nombreProducto}
                Cantidad: {producto._cantidadProducto}
                Precio: {producto._precioProducto}
            """))
            
    def eliminarProducto(productos):
        print()
        print("#"*30)
        print("ELIMINACION DE PRODUCTOS")
        print("#"*30)
        
        if not productos:
            print("\nNo hay productos en el carrito para eliminar.")
            return
        
        print("\nProductos agregados al carrito actualmente:")
        for i, producto in enumerate(productos, start=1):
            print(dedent(f"""
                Producto #{i}
                Nombre de Producto: {producto._nombreProducto}
                Cantidad: {producto._cantidadProducto}
                Precio: {producto._precioProducto}
            """))
            
        while True:
            try:
              indice = int(input("\nPor favor ingrese el indice del producto a eliminar: ").strip())
              if indice < 1 or indice > len(productos):
                  raise ValueError("El indice ingresado esta fuera de rango. Por favor intente de nuevo.")
              break
            except ValueError as e:
              print(f"\nError: {e}")
              
        productos.pop(indice-1)
        print(f"\nProducto eliminado exitosamente.")
        
    def finalizarCompra(productos: list):
        print()
        print("#"*30)
        print("FINALIZACION DE COMPRA")
        print("#"*30)
        
        if not productos:
            print("\nNo hay productos en el carrito. Debe agregar al menos un producto para finalizar la compra.")
            return
        
        print("\nProductos comprados:")
        for i, producto in enumerate(productos, start=1):
            print(dedent(f"""
                Producto #{i}
                Nombre de Producto: {producto._nombreProducto}
                Cantidad: {producto._cantidadProducto}
                Precio: {producto._precioProducto}
            """))
        
        subtotal = 0    
        total = 0
        cantidadComprada = 0
        
        for producto in productos:
            importeNetoProducto = producto._precioProducto * producto._cantidadProducto
            cantidadComprada += producto._cantidadProducto
            subtotal += importeNetoProducto
            
        iva = subtotal * 0.19
        total = subtotal + iva
            
        print()
        print("#"*30)
        print("DETALLE DE FACTURACION")
        print("#"*30)
        
        print(dedent(f"""
              Subtotal: ${subtotal}
              Iva: ${iva}
              Total a Pagar: ${total}
              Cantidad de productos comprados: {cantidadComprada}
              """))
        
        print("\nCompra finalizada exitosamente.")
        input("Presione <Enter> para continuar")
        
    @staticmethod
    def generarRecibo(productos: list):
        if not productos:
            print("\nNo hay productos en el carrito. No se puede generar un recibo.")
            return
        
        total_compra = sum(p._cantidadProducto * p._precioProducto for p in productos)
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nombre_archivo = f"Recibo_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("="*80 + "\n")
            f.write("         RECIBO DE COMPRA\n")
            f.write("="*80 + "\n")
            f.write(f"Fecha y hora: {fecha_hora}\n\n")
            f.write("Productos comprados:\n")
            f.write("-"*80 + "\n")
            f.write(f"{'Producto':<25}{'Cantidad':<10}{'Precio':<20}{'Subtotal':<20}\n")
            f.write("-"*80 + "\n")

            for producto in productos:
                subtotal = producto._cantidadProducto * producto._precioProducto
                f.write(f"{producto._nombreProducto:<25}{producto._cantidadProducto:<10}{producto._precioProducto:<20.2f}{subtotal:<20.2f}\n")

            f.write("-"*80 + "\n")
            f.write(f"{'TOTAL:':<35}{total_compra:.2f}\n")
            f.write("="*80 + "\n")
            f.write("¡Gracias por su compra!\n")

        print(f"\nRecibo generado exitosamente: {nombre_archivo}")