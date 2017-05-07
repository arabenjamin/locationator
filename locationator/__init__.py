#!/usr/bin/python
from locationate import Locationator


__version__ = "0.1.0"
__author__ = "Ara"


if __name__ == "__main__":
	address = "1537 Paper St., Wilmington, DE 19886"
	location = Locationator()
	location.user_agent()
	location.geocode(address)