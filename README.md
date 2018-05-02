# The land and/or lands of JO-EB

Land of great warriors, unknown mysteries, forgotten treasures, bottmless dungeons.


# Setting up the project on GNU/Linux

## Installing SDL

```
sudo apt install libsdl2-2.0
```
To install everything necessary for building programs that include it
```
sudo apt install libsdl2-dev
```

## Installing libtcod
```
wget https://bitbucket.org/libtcod/libtcod/downloads/20161228-libtcod-1.6.2.tbz2
tar xf 20161228-libtcod-1.6.2.tbz2
cd 20161228-libtcod-1.6.2
 
cd build/autotools/
autoreconf -i
```
At this point you can run into some errors, probably because you don't have automake and libtool installed. You can install them by typing
```
sudo apt install automake
sudo apt install libtool
```
After installing the packages you can proceed with
```
./configure
make
cd ../..
```
