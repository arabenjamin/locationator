## Locationator

A simple python package to  perform basic geocoding operations.
Currently Locationator supports:
* Geocoding
* Reverse geocoding
* geocodeing Ip addresses

## Install:
```
git clone https://github.com/arabenjamin/locationator.git
cd locationator
pip install .
```

## Usage:
```python
   from locationator import Locationator
   location = Locationator()
   location.geocode(address)
```

## Todo:

* add error handlers

