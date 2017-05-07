from locationator import Locationator
from config import Config

cfg = Config('config.cfg')

if __name__ == "__main__":
    address = "1537 Paper St., Wilmington, DE 19886"
    location = Locationator(cfg.API_KEY)
    print location.user_agent()
    print location.geocode(address)