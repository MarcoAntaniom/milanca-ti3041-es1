import json
from pathlib import Path
from django.shortcuts import render
from django.http import Http404

RUTA_JSON = Path(__file__).resolve().parent.parent / "data" / "productos.json"

def cargar_productos():
    with open(RUTA_JSON, encoding="utf-8") as f:
        return json.load(f)

def lista_productos(request):
    productos = cargar_productos()
    return render(request, "catalogo/lista.html", {"productos": productos})

def detalle_producto(request, id):
    productos = cargar_productos()
    producto = next((p for p in productos if p["id"] == id), None)
    
    if not producto:
        raise Http404("Producto no encontrado")
        
    return render(request, "catalogo/detalle.html", {"producto": producto})