from locationate import Locationator
from config import Config
__version__ = "0.1.0"
__author__ = "Ara"

cfg = Config(file('config.cfg'))
G_API_KEY = cfg.GMAP_API_KEY 
