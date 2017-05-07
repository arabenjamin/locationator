from locationator import Locationator

address = "1537 Paper St., Wilmington, DE 19886"
lat_lng = Locationator().geocode(address)

class TestClass:
    
    def test_geocode(self):
         
        assert isinstance(Locationator().geocode(address), (tuple,tuple)) == True

    def test_rev_geoocode(self):
        assert isinstance(Locationator().reverse_geocode(lat_lng), (str,unicode)) == True

    def test_geocode_ip(self):
        assert Locationator().geocode_ip()


if __name__ == "__main__":
    
    my_address = "1537 Paper St., Wilmington, DE 19886" 
    test_geocode(my_address)