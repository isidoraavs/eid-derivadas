# Animacion de sumas de Riemann

## Requisitos

- Python 3.10 o superior
- Manim Community (`manim==0.22.0`, indicado en `requirements.txt`)
- MiKTeX, para compilar las expresiones matematicas de Manim
- FFmpeg, para crear el archivo de video

En Windows, instala las dependencias externas con WinGet si aun no estan instaladas:

```powershell
winget install --id MiKTeX.MiKTeX --source winget --accept-source-agreements --accept-package-agreements
winget install --id Gyan.FFmpeg.Essentials --source winget --accept-source-agreements --accept-package-agreements
```

Reinicia VS Code despues de instalar MiKTeX o FFmpeg para que sus comandos queden
disponibles en la terminal integrada. MiKTeX puede descargar paquetes adicionales
la primera vez que Manim compila las formulas.

## Instalar y renderizar

Desde la carpeta del proyecto, usando Python 3.14:

```powershell
py -3.14 -m pip install -r requirements.txt
py -3.14 -m manim -pqm extremos_riemann.py ComparacionExtremos
```

Tambien puedes abrir `extremos_riemann.py` en VS Code y apretar el boton ▶
de ejecutar el archivo. Renderiza la escena y abre el video al terminar.

El video se guarda en `media/videos/extremos_riemann/720p30/ComparacionExtremos.mp4`.
Para renderizar en baja calidad y mas rapido, cambia `-pqm` por `-pql`.

La escena muestra la funcion `f(x) = x + 1` en `[0, 4]`, con cuatro rectangulos:
la suma izquierda es 10, la suma derecha es 14 y el area exacta es 12.
