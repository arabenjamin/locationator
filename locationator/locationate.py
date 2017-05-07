import locationator
import requests


class Locationator():

    def __init__(self,API_KEY=None):
		self.api_key = API_KEY#change this variable
		self.headers = {"User-Agent": self.user_agent()} 
		
    def user_agent(self):
	
		""" Declare ourselves """
		return "Locationator/{0} (A Python package for getting geocode data)".format(locationator.__version__)

    def geocode(self,address):
	
        """ Converts addresses into geographic coordinates."""
			#: @parameter:  Must be a string.
			#: @return:       Returns a tuple contianing lat/lng.
			#: @method:     This method DOES NOT require an API key from, the Google, 
			#:			           although if you use this method a thousand times in a secound
			#:                    Google may see it fit to decline your requests.
			
        url =  'https://maps.googleapis.com/maps/api/geocode/json?address={0}'.format(address)
        latlng = requests.get(url).json()['results'][0]['geometry']['location']
        return (latlng['lat'], latlng['lng'])
		
    def reverse_geocode(self,lat_lng):
	
		""" Reverse geocoding is the process of converting geographic coordinates into a human-readable address."""
			#: @parameter: given a lat/lng 
			#: @retunr:       returns an address as string
			
		url = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+str(lat_lng[0])+","+str(lat_lng[1])
		return requests.get(url).json()['results'][0]['formatted_address']
		
    def geocode_ip(self,ip_address):
	
		""" get the geocode for the supplied Ip address """
			#: @method: Method uses ipinfo.io, it's polite to use an API key
			#:                which can be found here: https://ipinfo.io/pricing
			#: @parameter: takes an ip_address as a string
			#: @variable:   
			#: @return:       
			
		url = "http://ipinfo.io/{0}".format(ip_address)	
		return requests.get(url).json()['loc']
 	
		
if __name__ == "__main__":
	address = "3009 NE 120th St, Seattle Wa, 98125"
	location = Locationator(locationator.G_API_KEY)
	location.geocode(address)