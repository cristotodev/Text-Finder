# TextFinder

TextFinder es una herramienta de línea de comandos en Python que busca texto en archivos dentro de un directorio especificado. Permite omitir ciertos directorios y resalta los resultados en la consola con colores para una mejor legibilidad.

## Características

- Busca múltiples textos en archivos de un directorio.
- Permite omitir directorios específicos.
- Resultados presentados en una tabla con colores para facilitar la lectura.

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

## Ejemplo completo

```sh
python textfinder.py -p /ruta/del/directorio -t "texto1" -t "texto2" -o dir1 -o dir2
```

Este comando buscará "texto1" y "texto2" en todos los archivos del directorio especificado, omitiendo los directorios dir1 y dir2.

## Resultados

Los resultados se presentan en una tabla con las siguientes columnas:

- Ruta de la carpeta: La ruta del directorio donde se encontró el archivo.
- Archivo: El nombre del archivo donde se encontró el texto.
- Palabras Encontradas: Las palabras buscadas que se encontraron en el archivo.

Los mensajes se muestran en colores para facilitar la lectura:

- Verde: Número de coincidencias encontradas.
- Amarillo: Indicador de que no se encontraron coincidencias.
- Rojo: Mensajes de error durante la lectura de archivos.
- Cian: Duración de la búsqueda.

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.