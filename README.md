# Subtle GUI

A graphical interface for [subtle](https://github.com/fmacia/subtle/).

## Requirements

* Python 3
* PyQt 5
    * Which means: libQt5Gui, libQt5DBus-devel, libQt5Gui-devel,
        libQt5OpenGL-devel, libQt5PlatformHeaders-devel, libQt5Test-devel,
        libQt5Xml-devel, libqt5-qtbase-devel, libqt5-qtdeclarative-devel,
        libqt5-qtmultimedia-devel, libqt5-qtsvg-devel, libqt5-qttools-devel,
        libqt5-qtx11extras-devel

## Hacking

(This more a reminder than anything)

### With `virtualenvwrapper`

```sh
$ mkvirtualenv -p $( which python3 ) -r /w/subtlegui/requirements \
    -a /w/subtlegui subtlegui
```

### Install `sip`

[Download](http://www.riverbankcomputing.com/software/sip/download) and extract
it in your freshly created virtualenv.

Now compile and install it IN your virtualenv:

```sh
(subtlegui) $ python configure.py -e $HOME/.virtualenvs/subtlegui/include/python3.4m
(subtlegui) $ make
(subtlegui) $ make install
```

### Install `PyQt5`

[Download](http://www.riverbankcomputing.com/software/pyqt/download5) and extract
it in your freshly created virtualenv.

Now compile and install it IN your virtualenv:

```sh
(subtlegui) $ python configure.py -q /usr/bin/qmake-qt5 \
    --sip-incdir=$HOME/.virtualenvs/subtlegui/include/python3.4m/
(subtlegui) $ make
(subtlegui) $ make install
```
