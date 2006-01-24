"""
Package: AstroLib Coords

Purpose
=======

This package aims to provide much of the IDL "astron" functionality that
pertains to coordinate manipulations in an OO framework. Our target user is
a typical astronomer who needs to analyze data, work with catalogs, prepare
observing proposals, and prepare for observing runs.

The initial version will provide simple functionality for working with
positions in the same reference frame, without having to worry about units.



Dependencies
============
numarray


Example
=======

>>> import coords as C
>>>
>>> #Specify position in hmsdms
>>> polaris=C.Position("02:31:49.08 +89:15:50.8")
>>> polaris.dd()
(37.954500000000003, 89.264111111111106)
>>> polaris.hmsdms()
"02:31:49.080 +89:15:50.800"
>>> #Specify position in decimal degrees
>>> ob=C.Position((52.9860209, -27.7510006))
>>> ob.hmsdms()
"03:31:56.645 -27:45:03.602"
>>> ob.dd()
(52.9860209, -27.751000600000001)
>>>
>>> #Use as calculator without saving the intermediate object
>>> C.Position("12:34:45.4 -22:21:45.4").dd()
(188.68916666666667, -22.362611111111111) 

@sort: Position, Coord, Degrees, Hmsdms


@see: U{http://www.scipy.org/wikis/topical_software/AstroLibCoordsHome}

@author:  Vicki Laidler
@version: '0.0.1 (2005-11-30)'

@todo: improve tests
@todo: combine with wrapped TPM library to handle limited coordinate
transformations.

@group Classes: position.Position, position.Coord, angsep.Angsep
@group Modules: position, angsep
@sort: Classes, Modules

@sort: position, angsep
"""
from position import *
from angsep import *


__version__ = '0.0.1'      #Release version number only
__vdate__ = '2005-11-30'   #Date of this version, in this (FITS-style) format
