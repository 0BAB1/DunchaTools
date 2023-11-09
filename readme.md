# DunchaTools V 1.0

## contiens :

- extracteur de données PDF
- estimateur de temps GCODE (openSource)

## Lancer

```git clone https://github.com/0BAB1/DunchaTools```
```pip install -r requirements.txt```
```cd DunchaTools && git clone https://github.com/0BAB1/gcodeEstimator```

## build :

```
pip install pyinstaller
mkdir build
cd build
python -m PyInstaller -D -n dunchaToolBox --windowed --icon="../UI/logo/favicon.ico" ../app.py
```

## modifier interface :

Ouvrir QT Designer

Ouvrir UI/Interace.py

Faire les modifs

Executer :

```python -m PyQt6.uic.pyuic .\UI\interface.ui -o interface.py -x```