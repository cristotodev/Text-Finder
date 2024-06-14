# TextFinder

TextFinder es una herramienta de línea de comandos en Python que busca texto en archivos dentro de un directorio especificado. Permite omitir ciertos directorios y resalta los resultados en la consola con colores para una mejor legibilidad.

## Características

- Busca múltiples textos en archivos de un directorio.
- Permite omitir directorios específicos.
- Permite incluir o excluir archivos por su extensión.
- Resultados presentados en una tabla con colores para facilitar la lectura.
- Soporte para expresiones regulares en las búsquedas.
- Opción para realizar búsquedas sin diferenciar entre mayúsculas y minúsculas.
- Exportación de resultados en formatos JSON y CSV

## Requisitos

- Python 3.6 o superior

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/tuusuario/Text-Finder.git
    cd Text-Finder
    ```

2. Instala el proyecto y sus dependencias:
    ```sh
    pip install .
    ```

## Uso

### Búsqueda de texto

Para buscar texto en un directorio, utiliza la opción `-p` para especificar la ruta del directorio y `-t` para especificar el texto a buscar. Puedes especificar múltiples textos utilizando la opción `-t` varias veces.

```sh
textfinder -p /ruta/del/directorio -t "texto1" -t "texto2"
```

### Omisión de directorios

Para omitir ciertos directorios durante la búsqueda, utiliza la opción -o y especifícala varias veces.

```sh
python textfinder.py -p /ruta/del/directorio -t "texto1" -t "texto2" -o dir1 -o dir2
```

### Inclusión o exclusión de archivos por extensión

Para incluir solo archivos con ciertas extensiones, utiliza la opción --include-ext y especifícala varias veces.

```sh
textfinder -p /ruta/del/directorio -t "texto1" -t "texto2" --include-ext .txt --include-ext .log
```

Para excluir archivos con ciertas extensiones, utiliza la opción --exclude-ext y especifícala varias veces.

```sh
textfinder -p /ruta/del/directorio -t "texto1" -t "texto2" --exclude-ext .txt --exclude-ext .log
```

### Búsqueda multihilo

Para realizar la búsqueda utilizando múltiples hilos y así mejorar la velocidad de búsqueda, utiliza la opción -n para especificar el número de hilos.

```sh
textfinder -p /ruta/del/directorio -t "texto1" -t "texto2" -n 4
```

### Uso de expresiones regulares

Para realizar búsquedas utilizando expresiones regulares, utiliza la opción -r.

```sh
textfinder -p /ruta/del/directorio -t "regex1" -t "regex2" -r
```

### Búsqueda sin diferenciar entre mayúsculas y minúsculas

Para realizar búsquedas sin diferenciar entre mayúsculas y minúsculas, utiliza la opción -c.

```sh
textfinder -p /ruta/del/directorio -t "Texto1" -t "Texto2" -c
```

### Exportación de resultados

Para exportar los resultados en formato JSON o CSV, utiliza las opciones -f para el formato y -O para especificar el archivo de salida.

```sh
textfinder -p /ruta/del/directorio -t "texto1" -t "texto2" -f json -O resultados.json
textfinder -p /ruta/del/directorio -t "texto1" -t "texto2" -f csv -O resultados.csv
```

## Ejemplo completo

```sh
textfinder -p /ruta/del/directorio -t "texto1" -t "texto2" -o dir1 -o dir2 --include-ext .txt --exclude-ext .log -n 4 -r -c -f json -O resultados.json
```

Este comando buscará "texto1" y "texto2" en todos los archivos del directorio especificado, omitiendo los directorios dir1 y dir2, utilizando 4 hilos, con expresiones regulares, sin diferenciar entre mayúsculas y minúsculas, y exportando los resultados en formato JSON al archivo resultados.json.

## Resultados

Los resultados se presentan en una tabla con las siguientes columnas:

- Ruta de la carpeta: La ruta del directorio donde se encontró el archivo.
- Archivo: El nombre del archivo donde se encontró el texto.
- Palabras Encontradas: Las palabras buscadas que se encontraron en el archivo.

Los mensajes se muestran en colores para facilitar la lectura:

- Verde: Número de coincidencias encontradas.
- Amarillo: Indicador de que no se encontraron coincidencias.
- Rojo: Mensajes de error durante la lectura de archivos.
- Cian: Duración de la búsqueda y número de Threads lanzados

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.