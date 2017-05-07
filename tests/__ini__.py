from locaionator import Locationator


def test_geocode(address):
    return Locationator().geocode(address)

def test_rev_geoocode(lat_lng):
    return Locationator.reverse_geocode(lat_lng)

def test_geocode_ip(ip_address):
    retrun Locationator().geocode_ip(ip_address)


if __name__ == "__main__":
    
    address = "1537 Paper St., Wilmington, DE 19886" 