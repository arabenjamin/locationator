#!/usr/bin/python
from error_handler import NetworkError, InvalidAddressError, InvalidCoordError, EmptyParameterError, RequestException
import locationator
import requests


class Locationator():

    def __init__(self,API_KEY=None):
        self.api_key = API_KEY#change this variable
        self.headers = {"User-Agent": self.user_agent()}
        self.google_base_url = "https://maps.googleapis.com/maps/api/geocode/json"
		
        
    def user_agent(self):
	
		""" Declare ourselves """
        
		return "Locationator/{0} (A Python package for getting geocode data)".format(locationator.__version__)

    def geocode(self,address):
	
        """ Converts addresses into geographic coordinates."""
        
			#: @parameter:  Must be a string.
			#: @return:     Returns a tuple contianing lat/lng.
			#: @method:     This method DOES NOT require an API key from, the Google, 
			#:			    although if you use this method a thousand times in a secound
			#:              Google may see it fit to decline your requests.
        
        # Make sure it's not nothing
        if address is None or len(address) == 0:
            raise EmptyParameterError("Won't work with an empty address")
            
        # make sure it's the right type    
        elif not isinstance(address, (str, unicode)):
            raise InvalidAddressError("address must be a string")
            
        # set the api path
        path = '?address={0}'.format(address)      
        
        # use the api key if it's available
        if self.api_key is not None:
            path = '?address={0}&key={1}'.format(address,self.api_key)
            
        # put url together    
        url = self.google_base_url + path
        try:
            # using the url, reach out with requests and get the lat/lng of the provided address
            latlng = requests.get(url, headers = self.headers).json()['results'][0]['geometry']['location']
            return (latlng['lat'], latlng['lng'])
        except RequestException:
            raise NetworkError('Requests ran into a problem with your HTTP request')
            return None
		
    def reverse_geocode(self,lat_lng):
	
        """ Reverse geocoding is the process of converting geographic coordinates into a human-readable address."""
			#: @parameter: given a lat/lng tuple
			#: @retunr:    returns an address as string
            
        # Make sure it's not nothing, or empty, or half full
        if lat_lng is None or len(lat_lng) < 2:
            raise EmptyParameterError("Latitude and Longitude must be in a Tuple")
            
         # make sure it's the right type   
        if not isinstance(lat_lng,(tuple,tuple)):
            raise InvalidCoordError("Latitude and Longitude must be in a Tuple")
            
        # set the api path
        path = "?latlng="+str(lat_lng[0])+","+str(lat_lng[1])
        
        # use the api key if it's available
        if self.api_key is not None:
			path = "?latlng={0},{1}&key={2}".format(str(lat_lng[0]),str(lat_lng[1]),self.api_key)
            
        # put url together
        url = self.google_base_url + path    
        
        try:
            return requests.get(url, headers=self.headers).json()['results'][0]['formatted_address']
        except RequestException:
            raise NetworkError('Requests ran into a problem with your HTTP request')
            return None
        
    def geocode_ip(self,ip_address=None):
	
        """ get the geocode for the supplied Ip address """
			#: @method: Method uses ipinfo.io, it's polite to use an API key
			#:                which can be found here: https://ipinfo.io/pricing
			#: @parameter: takes an ip_address as a string
			#: @variable:   
			#: @return:
        
        if ip_address == None:
            url = "http://ipinfo.io/"
            r = requests.get(url)
            return tuple(r.json()['loc'])
            
        # Check to see if it's a valid Ip address    
        if len(ip_address.split('.')) != 4:
            raise InvalidIPAddress('Please use valid IPv4 ip address')
            
        url = "http://ipinfo.io/{0}".format(ip_address)    
        
        
        return requests.get(url, headers=self.headers).json()['loc']
 	
		
