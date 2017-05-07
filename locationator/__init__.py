from locationate import Locationator


__version__ = "0.1.0"
__author__ = "Ara"


if __name__ == "__main__":
	address = "3009 NE 120th St, Seattle Wa, 98125"
	location = Locationator()
	location.user_agent()
	location.geocode(address)