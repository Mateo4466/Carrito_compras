from django.shortcuts import render, redirect, get_object_or_404
from carrito.Carrito import Carrito
from carrito.models import Producto

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos': productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    if producto.stock > 0:
        carrito.agregar(producto)
        producto.stock -= 1 
        producto.save()
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.eliminar(producto)
    producto.stock += 1
    producto.save()
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.restar(producto)
    producto.stock += 1
    producto.save()
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    for key, item in carrito.carrito.items():
        producto = get_object_or_404(Producto, id=int(key))
        producto.stock += item['cantidad']
        producto.save()
    carrito.limpiar()
    return redirect("Tienda")

def pantalla_pago(request):
    carrito = Carrito(request)
    productos_carrito = carrito.carrito
    total_carrito = sum(item['acumulado'] for item in productos_carrito.values())
    
    return render(request, "pago.html", {
        'productos_carrito': productos_carrito,
        'total_carrito': total_carrito,
        'carrito': carrito
    })

def confirmar_pago(request):
    if request.method == 'POST':
        metodo_pago = request.POST.get('metodo_pago')
        carrito = Carrito(request)
        carrito.limpiar()
        return redirect('Gracias')

def gracias(request):
    return render(request, 'gracias.html')
