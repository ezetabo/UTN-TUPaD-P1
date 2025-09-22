@echo off
set /p carpeta=Ingrese la ruta de la carpeta donde desea crear los archivos:
set /p cantidad=Ingrese la cantidad de archivos a crear:
set /p nombre=Ingrese el nombre para los archivos:
set /p extension=Ingrese la extension de los archivos (sin el punto):

:: Verificar si la carpeta existe; si no, crearla
if not exist "%carpeta%" (
    echo La carpeta no existe. Se creara ahora...
    mkdir "%carpeta%"
)

:: Crear los archivos en la carpeta especificada con ceros a la izquierda
for /l %%i in (1,1,%cantidad%) do (
    setlocal enabledelayedexpansion
    set "num=0%%i"
    set "num=!num:~-2!"
    type nul > "%carpeta%\%nombre%_!num!.%extension%"
    endlocal
)

echo Se han creado %cantidad% archivos en blanco con extension .%extension% en: %carpeta%
pause
