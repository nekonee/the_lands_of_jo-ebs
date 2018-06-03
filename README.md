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

## Installing requirements
While in game directory create a virtual environment first to install requirements locally:

```
virtualenv -p python3 name_of_your_environment
```
then start it with:

```
source name_of_your_environment/bin/activate
```

and now you can finally install requirements with:
```
pip install -r requirements.txt
```

## Tests
Nosetest was already installed in the previous step so you can just proceed with
```
nosetests -s
```

## Game screenshots- will be updated after adding new features

![Glimpse of a game](https://i.imgur.com/Kun4pNp.gif)

