from django.shortcuts import render,redirect,get_object_or_404
from inventario.models import Productos,Categorias
from django.contrib.auth.decorators import login_required
from .forms import FormProducto
# Create your views here.


def listarProductos(req):
    productos = Productos.objects.all() # equivale a un "SELECT * FROM productos"
    categorias = Categorias.objects.all() #equivale a un "SELECT * FROM categorias"
    formulario = FormProducto()
    #rendericemos en el CONTEXTO 
    contexto = {"productos":productos,"categorias":categorias,"formulario":formulario}
    return render(req,'index.html',contexto)

def eliminarProducto(req, id):
    producto = get_object_or_404(Productos, id=id)
    producto.delete()
    return redirect('index')

@login_required
def editarProducto(req, id):
    producto = get_object_or_404(Productos, id=id)
    
    if req.method == "GET":
        formulario = FormProducto(instance=producto)
        contexto = {"producto": producto, "formulario": formulario}
        return render(req, 'editar.html', contexto)
    
    elif req.method == "POST":
        formulario = FormProducto(req.POST,req.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')

@login_required
def crearProducto(req):
    form_producto = FormProducto(req.POST,req.FILES)
    if req.method == "POST":
        if form_producto.is_valid():
            form_producto.save()
            return redirect('index')

    productos = Productos.objects.all()
    categorias = Categorias.objects.all()
    contexto = {"productos": productos, "categorias": categorias, "formulario": form_producto}
    return render(req, 'index.html', contexto)