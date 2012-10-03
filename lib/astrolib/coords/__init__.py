"""
Package: AstroLib Coords


NOT SURE HOW TO CONVERT THESE FROM EPYDOC TO SPHINX
===================================================

@sort: Position, Coord, Degrees, Hmsdms

@group Classes: position.Position, position.Coord, angsep.Angsep
@group Modules: position, angsep

@sort: Classes, Modules
@sort: position, angsep

"""
from position import Position
from angsep import AngSep
from astrodate import AstroDate


__version__ = '0.39'      #Release version number only
__vdate__ = '2009-01-6'   #Date of this version, in this (FITS-style) format

def _test():
    """use nose to run the coords tests"""

    import nose

    # give a list of the names of modules that contain tests as
    # strings containing the fully qualified module name.  It does
    # NOT work to pass the actual module object to nose.
    nose.run(defaultTest= [ 
        'astrolib.coords.tests.test_angsep',
        'astrolib.coords.tests.test_astrodate', 
        'astrolib.coords.tests.test_tpm',
        'astrolib.coords.test'
        ] 
    )

test = _test
