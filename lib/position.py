"""
Position object to manage coordinate transformations

@sort: Position, Coord, Hmsdms, Degrees, Radians
"""

import types
import math

import numarray as N
import angsep
import astrodate #helper class: to be brought inside eventually

import pytpm
        
class Position:

    """ The basic class in the coords library. The Position class is designed
    to permit users to define a position and then access many representations
    of it.

    @ivar input: the input used to create the Position
    @ivar units: in which the coords were specified (degrees, radians)
    @type units: string
    @ivar equinox: at which the coordinates were specified
    @ivar system: celestial, galactic, ecliptic
    @type system: string

    @ivar _tpmstate: the TPM state of the position
    @type _tpmstate: integer

    @ivar coord: a "smart" representation of the position
    @type coord: L{Coord}

    @ivar _internal: the internal representation of the position (decimal degrees)
    @type _internal: (float,float)

    @todo: Make the angsep method correctly calculate separations
    between positions even if they were originally specified in different
    systems -- without breaking the present behavior of the unit-related
    methods. 
    """

    def __init__(self,input,
                 equinox='J2000',
                 system='celestial',
                 units='degrees'):
        """


        @param input: coordinates of the position
        @type input: string (hh:mm:ss.ss +dd:mm:ss.sss) or tuple of numbers (dd.ddd, dd.ddd)
        @param equinox: in which the coords are specified
        @type equinox: string

        @param system: celestial, galactic, ecliptic, etc
        @type system: string

        @param units: degrees or radians
        @type units: string

        @rtype: Position

        """

        self.input=input
        try:
            self.equinox=equinox.lower()
        except:
            self.equinox=equinox #to support arbitrary equinoxes
        self.system=system.lower()
        self.units=units.lower()
        self._set_tpmstate()
        self._parsecoords()

        
    def _set_tpmstate(self):
        """ Define the state for TPM based on equinox and system """
        if self.system == 'galactic':
            self._tpmstate=4
            self._tpmequinox=astrodate.BesselDate(1958.0).jd
        elif self.system == 'ecliptic':
            self._tpmstate=3
            self._tpmequinox=astrodate.JulianDate(1984.0).jd
        elif self.system == 'celestial':
            if self.equinox == 'j2000':
                self._tpmstate=6
                self._tpmequinox=pytpm.j2000
            elif self.equinox == 'b1950':
                self._tpmstate=5
                self._tpmequinox=pytpm.b1950
            else: #arbitrary equinox. assume FK5 for now, but this is bad.
                self._tpmstate=2
                self._tpmequinox=astrodate.JulianDate(self.equinox).jd
        
    def details(self):
        """
        @return: system & equinox
        @rtype: string
        """
        ans="""
         System: %s
        Equinox: %s \n""" %(self.system,self.equinox)
        return ans

    def __repr__(self):
        """
        @rtype: string
        """

        return "%s (%s)"%(self.coord.__repr__(),self.units)
    
    def _parsecoords(self):
        """ Convert from input string into internal representation
        (decimal degrees) by invoking the appropriate type of Coord.
        Default float values will be interpreted as decimal
        degrees; radians will have to be specified as such.

        Legitimate units: hmsdms, decimal degrees, radians
        
            -  hmsdms = "hh:mm:ss.ss -dd:mm:ss.ss"
            -  decimal degrees = (ddd.dd, -ddd.dd)
            -  radians = (rr.rr, rr.rr)
        
        @todo: add support for 3vectors ("xx.xxx yy.yyy zz.zzz")

        @rtype: None
        
        """

        if type(self.input) == types.StringType:
            self.coord=Hmsdms(self.input)
##         elif len(self.input) == 3:
##             self.coord=ThreeVec(self.input)
        elif len(self.input) == 2:
            if self.units.lower().startswith('rad'):
                self.coord=Radians(self.input)
            else:
                self.coord=Degrees(self.input)
        else:
            raise ValueError, "Can't parse input %s"%self.input

        self._internal=self.coord._calcinternal()
##         if self._tpmstate != pytpm.s06:
##             self._internal = self.j2000()
        
#....................................................................
# Unit conversions
           
    def dd(self):
        """
        @return: Position in decimal degrees
        @rtype:  (float,float)
        """
        return self._internal

    def rad(self):
        """ @return: Position in radians
            @rtype: (float,float) """
        r1=self._internal[0]*math.pi/180.0
        r2=self._internal[1]*math.pi/180.0
        return (r1,r2)
    
    def hmsdms(self):
        """
        @return: Position in hms dms
        @rtype: string
        """
        a1,a2=self._internal
        sign,rhh,rmm,rss=dms(a1/15.0)
        sign,ddd,dmm,dss=dms(a2)
        return "%02i:%02i:%06.3f %s%02i:%02i:%06.3f"%(rhh,rmm,rss,
                                                      sign,ddd,dmm,dss)

#.........................................................................
# Angular separations
    def angsep(self,other):
        """ Computes the angular separation (great circle distance)
        between two Positions.

        @param other: another L{Position}
        
        @return: angular separation
        @rtype: L{angsep.AngSep}
        """

        if not isinstance(other,Position):
            raise ValueError, "angsep only defined for positions"

        d=gcdist(self.rad(),other.rad())
        ans=angsep.AngSep(d,units='rad')
        ans.setunits(self.units)
        return ans

    def within(self,other,epsilon,units='arcsec'):
        """ returns true if "other" is within "epsilon" of "self"

        @param other: Another position
        @type other: L{Position}

        @param epsilon: angular separation
        @type epsilon: L{angsep.AngSep} or number

        @param units: of the angular separation, if it's specified as a number
        @type units: string ('arcsec','degrees')

        @rtype: Boolean
        
        """
        sep=self.angsep(other)
        sep.setunits(units)
        ans=sep.__le__(epsilon)
        return ans

#.................................................................
# Coordinate transformations using TPM.
# All "tstate" management is done inside blackbox.

    def galactic(self):
        """ Return the position in IAU 1958 Galactic coordinates.

        @return: (l,b) tuple in decimal degrees
        @rtype: (float,float)
        """

        x,y=self.dd()
        l,b=pytpm.blackbox(x,y,self._tpmstate,pytpm.s04,pytpm.j2000,self._tpmequinox)
        return l,b

    def j2000(self):
        """ Return the position in Mean FK5 J2000 coordinates
        @return: (ra, dec) tuple in decimal degrees
        @rtype: (float, float)
        """
        x,y=self.dd()
        r,d=pytpm.blackbox(x,y,self._tpmstate,pytpm.s06,pytpm.j2000,self._tpmequinox)
        return r,d
    
    def b1950(self):
        """ Return the position in Mean FK4 B1950 coordinates

        @return: (ra, dec) tuple in decimal degrees
        @rtype: (float,float)

        """
        x,y=self.dd()
        r,d=pytpm.blackbox(x,y,self._tpmstate,pytpm.s05,pytpm.j2000,self._tpmequinox)
        return r,d

    def ecliptic(self):
        """ Return the position in IAU 1980 Ecliptic coordinates 

        @return: (le,be) tuple in decimal degrees
        @rtype: (float,float)

        """
        x,y=self.dd()
        r,d=pytpm.blackbox(x,y,self._tpmstate,pytpm.s03,pytpm.j2000,self._tpmequinox)
        return r,d

    def tpmstate(self,endstate,epoch=None,equinox=None):

        """ This method allows the expert user to call the blackbox
        routine of the TPM library directly, for access to more state
        transitions than are supported in this interface. Little
        documentation is provided here because it is assumed you know
        what you are doing if you need this routine.

        @param endstate: as defined by the TPM state machine
        @type endstate: integer
        
        @param epoch: in Julian date; default J2000
        @type epoch: float

        @param equinox: in Julian date; default self._tpmequinox
        @type equinox: float

        @return: transformed coordinates in decimal degrees
        @rtype: (float,float)
        """

        if epoch is None:
            epoch=pytpm.j2000
        if equinox is None:
            equinox=self._tpmequinox
        x1,y1=self.dd()
        x2,y2=pytpm.blackbox(x1,y1,self._tpmstate,endstate,epoch,equinox)
        return x2,y2
    
#-----------------------------------------------------------------
#Coordinate object

class Coord:
    """General class for subclasses.
    
    A Coord is distinct from a Position by being intrinsically expressed in
    a particular set of units.

    Each Coord subclass knows how to parse its own input, and convert itself
    into the internal representation (decimal degrees) used by the package.
   """

class Degrees(Coord):
    """Decimal degrees coord

    @ivar a1: longitude in decimal degrees
    @ivar a2: latitude in decimal degrees
    @type a1,a2: float
    """

    def __init__(self,input):
        """        
        @param input: coordinates in decimal degrees
        @type input: (float,float)
        """
        self.a1,self.a2=input

    def __repr__(self):
        """ @rtype: string """
        return "%f %f"%(self.a1,self.a2)

    def _calcinternal(self):
        return self.a1,self.a2

class Radians(Coord):
    """Radians coord

    @ivar a1: longitude in radians
    @ivar a2: latitude in radians
    @type a1,a2: float
    """
    def __init__(self,input):
        """
        @param input: coordinates in radians
        @type input: (float,float)
        """
        self.a1, self.a2=input

    def __repr__(self):
        """ @rtype: string """
        return "%f %f"%(self.a1,self.a2)

    def _calcinternal(self):
        """Convert radians to decimal degrees

        @return: Decimal degrees
        @rtype: (float,float) """

        a1=self.a1*(180.0/math.pi)
        a2=self.a2*(180.0/math.pi)
        return a1,a2
    
class Hmsdms(Coord):
    """Sexagesimal coord

    @ivar a1: longitude in hours, minutes, seconds
    @ivar a2: latitude in degrees, minutes, seconds
    @type a1,a2: Numarray[int,int,float]
    """
    def __init__(self,input):
        """
        @param input: coordinates as hh:mm:ss.sss +dd:mm:ss.sss (sign optional)
        @type input: string

        """
        
        #First break into two on spaces
        a1,a2=input.split()
        #Then break each one into pieces on colons
        hh,mm,ss=a1.split(':')
        self.a1=N.array([int(float(hh)),int(float(mm)),float(ss)])
        dd,mm,ss=a2.split(':')
        self.a2=N.array([int(float(dd)),int(float(mm)),float(ss)])

    def __repr__(self):
        """ @rtype: string """
        return "%dh %dm %5.3fs %dd %dm %5.3fs"%(self.a1[0],self.a1[1],self.a1[2],self.a2[0],self.a2[1],self.a2[2])

    def _calcinternal(self):
        """Convert hmsdms to decimal degrees
        
        @return: Decimal degrees
        @rtype: (float, float)

        """
        a1= 15*self.a1[0] +   15*self.a1[1]/60.  +  15*self.a1[2]/3600.
        a2=abs(self.a2[0]) + abs(self.a2[1])/60. + abs(self.a2[2])/3600.
        if self.a2[0] < 0: a2 = a2*(-1)
        return a1,a2

#---------------------------------------------------------------
#Utility functions
def dms(number):
    """ Convert from decimal to sexagesimal degrees,minutes,seconds

    @type number: number
    
    @return: sign,degrees,minutes,seconds
    @rtype: (string,int,int,float)
    """

    if (number < 0):
        sign='-'
    else:
        sign='+'
        
    ss=abs(3600.*number)
    mm=abs(60.*number)
    dd=abs(number)

    dd=int(dd)
    mm = int(mm-60.*dd)
    ss = ss - 3600.*dd - 60.*mm
    dd = int(dd)

    return sign,dd,mm,ss

#Great circle distance formulae:
# source http://wiki.astrogrid.org/bin/view/Astrogrid/CelestialCoordinates

def hav(theta):
    """haversine function, units = radians. Used in calculation of great
    circle distance

    @param theta: angle in radians
    @type theta: number

    @rtype: number
    """
    ans = (math.sin(0.5*theta))**2
    return ans

def ahav(x):
    """archaversine function, units = radians. Used in calculation of great
    circle distance

    @type x: number

    @return: angle in radians
    @rtype: number

    """
    
    ans = 2.0 * math.asin(math.sqrt(x))
    return ans

def gcdist(vec1, vec2):
    """Input (ra,dec) vectors in radians;
    output great circle distance in radians.

    @param vec1,vec2: position in radians
    @type vec1,vec2: number  

    @rtype: great circle distance in radians
    
    @see: U{http://wiki.astrogrid.org/bin/view/Astrogrid/CelestialCoordinates}
    """
    ra1,dec1=vec1
    ra2,dec2=vec2
    ans=ahav( hav(dec1-dec2) + math.cos(dec1)*math.cos(dec2)*hav(ra1-ra2) )
    return ans
