# DunchaTools V 1.0

## contiens :

- extracteur de données PDF
- estimateur de temps GCODE (openSource)

## fonctionalités a venir :

- etendre l'éstimateur de temps
- FAO de base
- Visulisation OPENGL

### build :

```
pip install pyinstaller
mkdir build
cd build
python -m PyInstaller -D -n dunchaToolBox --windowed --icon="../UI/logo/favicon.ico" ../app.py
```