# Z książki "Python 3" A. Jurkiewicza

from sys import exit

try:
    import numpy as np
    print("Moduł numpy: OK")
except ImportError:
    print("Brak modułu numpy.")

try:
    import matplotlib
    print("Moduł matplotlib: OK")
except ImportError:
    print("Brak modułu matplotlib.")

try:
    from astropy.time import Time
    print("Moduł astropy: OK.")
except ImportError:
    print("Brak modułu astropy.")

try:
    from astroquery.jplhorizons import Horizons
    print("Moduł astroquery: OK.")
except ImportError:
    print("Brak modułu astroquery.")