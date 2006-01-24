"""
Position object to manage coordinate transformations

@sort: Position, Coord, Hmsdms, Degrees, Radians
"""

import types
import math

import numarray as N
import angsep

class Position:

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
        self.equinox=equinox
        self.system=system
        self.units=units
        self._parsecoords()

    def details(self):
        """
        @return: system & equinox
        @rtype: string
        """
        ans="""
         System: %s
        Equinox: %s \n""" %(self.system,self.equinox)
        return ans
    
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
        

           
    def dd(self):
        """
        @return: Position in decimal degrees
        @rtype: tuple (float,float)
        """
        return self._internal

    def rad(self):
        """ @return: Position in radians
            @rtype: tuple (float,float) """
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

    def angsep(self,other):
        """ Computes the angular separation (great circle distance)
        between two Positions.
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
    """Decimal degrees coord"""

    def __init__(self,input):
        """
        @param input: coordinates in decimal degrees
        @type input: tuple (float,float)
        """
        self.a1,self.a2=input

    def _calcinternal(self):
        return self.a1,self.a2

class Radians(Coord):
    """Radians coord"""
    def __init__(self,input):
        """
        @param input: coordinates in radians
        @type input: tuple (float,float)
        """
        self.a1, self.a2=input

    def _calcinternal(self):
        """Convert radians to decimal degrees

        @return: Decimal degrees
        @rtype: (float,float) """

        a1=self.a1*(180.0/math.pi)
        a2=self.a2*(180.0/math.pi)
        return a1,a2
    
class Hmsdms(Coord):
    """Sexagesimal coord"""
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
    @rtype: tuple (string,int,int,float)
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
