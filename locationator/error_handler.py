#!/usr/bin/python
from requests.exceptions import RequestException

class NetworkError(Exception):
    """something wouldn't connect"""
    pass


class InvalidAddressError(Exception):
    """Please use a valid street address """
    pass
    
    
class InvalidCoordError(Exception):
    """Please use valid geographical coordinates"""
    pass

class EmptyParameterError(Exception):
    """Empty parameter, nothing to work with"""
    pass