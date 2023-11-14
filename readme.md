# DunchaTools V 1.1

DunchaTools est une application développée par BRH basée sur PyQT, la version Python de QT6.

Cette application regroupe les différents outils que j'ai pu coder en un seule application avec une GUI pour rendre l'experience plus agréable (et surtout accessible).

## contiens :

- extracteur de données PDF
- estimateur de temps GCODE (openSource)

## Lancer

-> cloner le repo
-> intaller les requirements
-> cloner les outil gcodeEstimator depuis son repo a part
-> lancer l'application

```bash
git clone https://github.com/0BAB1/DunchaTools
pip install -r requirements.txt
cd DunchaTools && git clone https://github.com/0BAB1/gcodeEstimator
python ./app.py
```

## build :

```bash
pip install pyinstaller
mkdir build
cd build
python -m PyInstaller -D -n dunchaToolBox --windowed --icon="../UI/logo/favicon.ico" ../app.py
```

## modifier interface :

-> Ouvrir QT Designer
-> Ouvrir UI/Interace.py
-> Faire les modifs
-> Executer :

```python -m PyQt6.uic.pyuic .\UI\interface.ui -o interface.py -x```

## Cahngelog

V1.0 : init
V1.1 : add errors handling