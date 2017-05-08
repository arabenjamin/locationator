## Locationator

A simple python package to  perform basic geocoding operations.
Currently Locationator supports:
* Geocoding
* Reverse geocoding
* geocodeing Ip addresses

## Intended Audiance 
I wrote Locationator for a project at work, and felt this would be a wonderfull oppertunity to deloy it to the wild. For those who need to geocode an address or two, here and there, Locationator might be for you. For those who are looking for simple examples of how to geocode an address without someother library at play, please read through or fork the project. 

Please keep in mind, there are a lot of python geocoding libraries available, at least on Github. Check out [geocoder by Denis Carriere](https://github.com/DenisCarriere/geocoder) for a great example. Google also offers [googlemaps 2.4.6](https://github.com/googlemaps/google-maps-services-python) that should suite any and all of your geocoding/location needs. Locationator is not intended to replace those options.

Locationator is intended to be simple, and therefore easy to read/understand and implement. With that being said, if you're not providing driving directions to your endless user base, this package might be usefull to you. Turn a street address in to latitude and longitude, or latitude and longitude into a human reabable address. There's also a method for geocoding an IPv4 address. 

Locationator uses Google maps API for both geocoding and reverse geocoding. I felt that if I were to just use and focus on one location API, Google would be the best choice. Theres also a method that uses [http://ipinfo.io/](http://ipinfo.io/) to geocode IPv4 addresses. 

Though there are many location APIs out there. If you feel like I have overlooked something usefull, please feel free to contribute.

Locationator does not explicitly need an API key from Google, but I guarantee you, if you abuse this, Google will throttle you or block your ip altogether. Although Locationator will allow you to supply an API key, and the usage limits will be governed by the key you have gotten from Google. Enjoy.



## Install:
For now I'm going with...
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



