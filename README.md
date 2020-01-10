# Para realizar activación del ambiente virtual, nos ubicamos en la carpeta [ROOT] y tipeamos

> source venv/Scripts/activate

# Para realizar la desactivación del ambiente virtual, nos ubicamos en la carpeta [ROOT] y tipeamos

> deactivate

```sh
Para este caso la carpeta [ROOT] = Servidor
```

# Para instalacion de paquetes creados en archivos planos

> pip install -r requirements.txt

## Para establecer ruta de origen, se agrega al final de la linea -t [FOLDER_DESTINO]

> pip install -r requirements.txt -t [FOLDER_DESTINO]

# Para visualizar las dependencias existentes en el ambiente virtual

> pip freeze