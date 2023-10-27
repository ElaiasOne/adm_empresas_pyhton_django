from django.urls import path
from inventario.views import listarProductos, eliminarProducto, editarProducto, crearProducto

urlpatterns = [
    path('', listarProductos, name="index"),
    path('eliminar/<int:id>/', eliminarProducto, name="eliminar"),
    path('editar/<int:id>/', editarProducto, name="editar"),
    path('crear/', crearProducto, name='crear'),
]
