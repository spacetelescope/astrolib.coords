import _pytpm

# the only function defined in _pytpm
blackbox = _pytpm.blackbox

# These are constants that are supposed to be in astrolib.coords.pytpm
# These constants used to come from astrolib.coords._pytpm but without
# swig is it much easier to just define them in python here and then
# stuff them back into _pytpm.
b1950   = (2433282.42345905)
j2000   = (2451545.0)
CJ      = (36525.0)              # the julian century
CB      = (36524.21987817305)    # the tropical century at 1900.0
s01     = 1
s02     = 2
s03     = 3
s04     = 4
s05     = 5
s06     = 6

_pytpm.b1950 = b1950
_pytpm.j2000 = j2000
_pytpm.CJ = CJ
_pytpm.CB = CB
_pytpm.s01 = s01
_pytpm.s02 = s02
_pytpm.s03 = s03
_pytpm.s04 = s04
_pytpm.s05 = s05
_pytpm.s06 = s06
