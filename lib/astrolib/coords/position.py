import types
import math

import numpy as N
import angsep
import astrodate #helper class: to be brought inside eventually

import pytpm
import pytpm_wrapper

class Position(object):
    """
    The basic class in the coords library. The Position class is designed
    to permit users to define a position and then access many representations
    of it.

    Attributes
    ----------
    input
        The input used to create the Position.
    
    units : {'degrees', 'radians'}
        Unit in which the coords were specified.

    equinox : string
        Equinox at which the coordinates were specified.
    
    system : {'celestial', 'galactic', 'ecliptic'}

    _tpmstate : integer
        The TPM state of the position.

    coord : `~position.Coord`
        A "smart" representation of the position.

    _internal : (float, float)
        The internal representation of the position (decimal degrees).

    """

    def __init__(self,input,
                 equinox='J2000',
                 system='celestial',
                 units='degrees'):
        """
        Parameters
        ----------
        input : string (hh:mm:ss.ss +dd:mm:ss.sss) or tuple of numbers (dd.ddd, dd.ddd)
            Coordinates of the position.

        equinox : string
            Equinox in which the coords are specified.

        system : string
            celestial, galactic, ecliptic, etc

        units : {'degrees', 'radians'}

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
        """Define the state for TPM based on equinox and system."""
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
        Returns
        -------
        ans : string
            Formatted `system` and `equinox` for printing.

        """
        ans=""" System: %s \n Equinox: %s """ %(self.system,self.equinox)
        return ans

    def __repr__(self):
        """
        Returns
        -------
        string
        
        """
        return "%s (%s)"%(self.coord.__repr__(),self.units)

    def _parsecoords(self):
        """
        Convert from input string into internal representation
        (decimal degrees) by invoking the appropriate type of Coord.
        Default float values will be interpreted as decimal
        degrees; radians will have to be specified as such.

        Legitimate units: hmsdms, decimal degrees, radians

            - hmsdms = "hh:mm:ss.ss -dd:mm:ss.ss"
            - decimal degrees = (ddd.dd, -ddd.dd)
            - radians = (rr.rr, rr.rr)

        .. todo:: Add support for 3vectors ("xx.xxx yy.yyy zz.zzz")

        Returns
        -------
        None

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
        Returns
        -------
        _internal : (float, float)
            Position in decimal degrees.
        
        """
        return self._internal

    def rad(self):
        """
        Returns
        -------
        r1, r2 : (float, float)
            Position in radians.
            
        """
        r1=self._internal[0]*math.pi/180.0
        r2=self._internal[1]*math.pi/180.0
        return (r1,r2)

    def hmsdms(self):
        """
        Returns
        -------
        value : string
            Position in hms dms.

        """
        a1,a2=self._internal
        sign,rhh,rmm,rss=dms(a1/15.0)
        sign,ddd,dmm,dss=dms(a2)
        return "%02i:%02i:%06.3f %s%02i:%02i:%06.3f"%(rhh,rmm,rss,
                                                      sign,ddd,dmm,dss)

#.........................................................................
# Angular separations
    def angsep(self,other):
        """
        Computes the angular separation (great circle distance)
        between two Positions.

        Parameters
        ----------
        other : another `~position.Position`

        Returns
        -------
        ans : `~angsep.AngSep`
            Angular separation.

        """
        if not isinstance(other,Position):
            raise ValueError, "angsep only defined for positions"

        if self._tpmstate != other._tpmstate:
            #convert other state to self state
            otherpos=other.tpmstate(self._tpmstate,equinox=self._tpmequinox)
            #It presently returns a tuple of (dd)
            #Convert the result to a Coord
            other_rad=Degrees(otherpos)._calcradians()
        else:
            other_rad=other.rad()
        d=gcdist(self.rad(),other_rad)
        ans=angsep.AngSep(d,units='rad')
        ans.setunits(self.units)
        return ans

    def within(self,other,epsilon,units='arcsec'):
        """
        Check if `other` is within `self`.
        
        Parameters
        ----------
        other : another `~position.Position`

        epsilon : `~angsep.AngSep` or number
            Angular separation.

        units : {'arcsec', 'degrees'}
            Unit of `epsilon`, if it is specified as a number.

        Returns
        -------
        ans : boolean
            `True` if `other` is within `epsilon` of `self`.

        """
        sep=self.angsep(other)
        sep.setunits(units)
        ans=sep.__le__(epsilon)
        return ans

#.................................................................
# Coordinate transformations using TPM.
# All "tstate" management is done inside blackbox.

    def galactic(self,timetag=None):
        """
        Return the position in IAU 1958 Galactic coordinates.

        Parameters
        ----------
        timetag : `~astrodate.AstroDate`
            Timetag of returned coordinate.

        Returns
        -------
        l, b : (float, float)
            Tuple in decimal degrees.

        """
        x,y=self.dd()
        l,b=pytpm_wrapper.blackbox(x,y,self._tpmstate,pytpm.s04,pytpm.j2000,self._tpmequinox,timetag)
        return l,b

    def j2000(self,timetag=None):
        """
        Return the position in Mean FK5 J2000 coordinates.

        Parameters
        ----------
        timetag : `~astrodate.AstroDate`
            Timetag of returned coordinate.

        Returns
        -------
        r, d : (float, float)
            Tuple of RA and DEC in decimal degrees.

        """
        x,y=self.dd()
        r,d=pytpm_wrapper.blackbox(x,y,self._tpmstate,pytpm.s06,pytpm.j2000,self._tpmequinox,timetag)
        return r,d

    def b1950(self,timetag=None):
        """
        Return the position in Mean FK4 B1950 coordinates.

        Parameters
        ----------
        timetag : `~astrodate.AstroDate`
            Timetag of returned coordinate.

        Returns
        -------
        r, d : (float, float)
            Tuple of RA and DEC in decimal degrees.

        """
        x,y=self.dd()
        r,d=pytpm_wrapper.blackbox(x,y,self._tpmstate,pytpm.s05,pytpm.j2000,self._tpmequinox,timetag)
        return r,d

    def ecliptic(self,timetag=None):
        """
        Return the position in IAU 1980 Ecliptic coordinates.

        Parameters
        ----------
        timetag : `~astrodate.AstroDate`
            Timetag of returned coordinate.

        Returns
        -------
        r, d : (float, float)
            Tuple of (le,be) in decimal degrees.

        """
        x,y=self.dd()
        r,d=pytpm_wrapper.blackbox(x,y,self._tpmstate,pytpm.s03,pytpm.j2000,self._tpmequinox,timetag)
        return r,d

    def tpmstate(self,endstate,epoch=None,equinox=None,timetag=None):
        """
        This method allows the expert user to call the blackbox
        routine of the TPM library directly, for access to more state
        transitions than are supported in this interface. Little
        documentation is provided here because it is assumed you know
        what you are doing if you need this routine.

        Parameters
        ----------
        endstate : integer
            As defined by the TPM state machine.

        epoch : float
            Epoch in Julian date; default is J2000.

        equinox : float
            Equinox in Julian date; default is `_tpmequinox`.

        timetag : `~astrodate.AstroDate`
            Timetag of returned coordinate.

        Returns
        -------
        x2, y2 : (float, float)
            Transformed coordinates in decimal degrees.

        """
        if epoch is None:
            epoch=pytpm.j2000
        if equinox is None:
            equinox=self._tpmequinox
        x1,y1=self.dd()
        x2,y2=pytpm_wrapper.blackbox(x1,y1,self._tpmstate,endstate,epoch,equinox,timetag)
        return x2,y2

#-----------------------------------------------------------------
#Coordinate object

class Coord:
    """
    General class for subclasses.

    A Coord is distinct from a Position by being intrinsically expressed in
    a particular set of units.

    Each Coord subclass knows how to parse its own input, and convert itself
    into the internal representation (decimal degrees) used by the package.
    
    """

class Degrees(Coord):
    """
    Decimal degrees coord.

    Attributes
    ----------
    a1, a2 : float
        Longitude and latitude in decimal degrees.

    """

    def __init__(self,input):
        """
        Parameters
        ----------
        input : (float, float)
            Coordinates in decimal degrees.

        """
        self.a1,self.a2=input
        #Check for valid range
        #TPM supports -180<longitude<180
        #More usual convention is 0<longitude<360
        #Support both this way
        if not -180 <= self.a1 <= 360:
            raise ValueError, "Longitude %f out of range [-180,360]"%self.a1
        if not -90 <= self.a2 <= 90:
            raise ValueError, "Latitude %f out of range [-90,90]"%self.a2

    def __repr__(self):
        """
        Returns
        -------
        string

        """
        return "%f %f"%(self.a1,self.a2)

    def _calcinternal(self):
        return self.a1,self.a2

    def _calcradians(self):
        a1=(math.pi/180.0)*self.a1
        a2=(math.pi/180.0)*self.a2
        return a1,a2

class Radians(Coord):
    """
    Radians coord.

    Attributes
    ----------
    a1, a2 : float
        Longitude and latitude in radians.

    """
    
    def __init__(self,input):
        """
        Parameters
        ----------
        input : (float, float)
            Coordinates in radians.

        """
        self.a1, self.a2=input
        if not -1*math.pi <= self.a1 <=2*math.pi:
            raise ValueError, "Longitude %f out of range [0,2pi]"%self.a1
        if not -1*math.pi <= self.a2 <=math.pi:
            raise ValueError, "Latitude %f out of range [0,2pi]"%self.a2

    def __repr__(self):
        """
        Returns
        -------
        string

        """
        return "%f %f"%(self.a1,self.a2)

    def _calcinternal(self):
        """
        Convert radians to decimal degrees.

        Returns
        -------
        a1, a2 : (float, float)
            Decimal degrees.

        """
        a1=self.a1*(180.0/math.pi)
        a2=self.a2*(180.0/math.pi)
        return a1,a2

class Hmsdms(Coord):
    """
    Sexagesimal coord: longitude in hours of time (enforced).

    Attributes
    ----------
    a1, a2 : Numpy[int,int,float]
        Longitude and latitude in hours, minutes, seconds

    """

    def __init__(self,input):
        """
        Parameters
        ----------
        input : string
            Coordinates as hh:mm:ss.sss +dd:mm:ss.sss (sign optional).

        """
        #First break into two on spaces
        a1,a2=input.split()
        #Then break each one into pieces on colons
        hh,mm,ss=a1.split(':')
        #Check range
        if not 0 <= int(hh) <= 24:
            raise ValueError, "Hours %s out of range [0,24]"%hh
        if not 0 <= int(mm) <= 60:
            raise ValueError, "Minutes %s out of range [0,60]"%mm
        if not 0 <= float(ss) <= 60:
            raise ValueError, "Seconds %s out of range [0,60]"%ss
        self.a1=N.array([int(float(hh)),int(float(mm)),float(ss)])

        dd,mm,ss=a2.split(':')
        if not -90 <= int(dd) <= 90:
            raise ValueError, "Degrees %s out of range [-90,90]"%dd
        if not 0 <= int(mm) <= 60:
            raise ValueError, "Minutes %s out of range [0,60]"%mm
        if not 0 <= float(ss) <= 60:
            raise ValueError, "Seconds %s out of range [0,60]"%ss

        self.a2=N.array([int(float(dd)),int(float(mm)),float(ss)])

        #Check & fix for negativity
        if a2.startswith('-'):
            self.a2sign = '-'
            self.a2*= -1
        else:
            self.a2sign = '+'


    def __repr__(self):
        """
        Returns
        -------
        string

        """
        return "%dh %dm %5.3fs %s%dd %dm %5.3fs"%(self.a1[0],self.a1[1],self.a1[2],self.a2sign,abs(self.a2[0]),abs(self.a2[1]),abs(self.a2[2]))

    def _calcinternal(self):
        """
        Convert hmsdms to decimal degrees.

        Returns
        -------
        a1, a2 : (float, float)
            Decimal degrees.

        """
        a1= 15*self.a1[0] +   15*self.a1[1]/60.  +  15*self.a1[2]/3600.
        a2=abs(self.a2[0]) + abs(self.a2[1])/60. + abs(self.a2[2])/3600.
        if self.a2sign == '-':
            a2 = a2*(-1)
        return a1,a2

#---------------------------------------------------------------
#Utility functions
def dms(number):
    """
    Convert from decimal to sexagesimal degrees,minutes,seconds.

    Parameters
    ----------
    number : number

    Returns
    -------
    sign, dd, mm, ss : (string, int, int, float)
        Sign, degrees, minutes, and seconds.

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
    """
    haversine function, units = radians.
    Used in calculation of great circle distance.

    Parameters
    ----------
    theta : number
        Angle in radians.

    Returns
    -------
    ans : number

    """
    ans = (math.sin(0.5*theta))**2
    return ans

def ahav(x):
    """
    archaversine function, units = radians.
    Used in calculation of great circle distance.

    Parameters
    ----------
    x : number

    Returns
    -------
    ans : number
        Angle in radians.

    """
    ans = 2.0 * math.asin(math.sqrt(x))
    return ans

def gcdist(vec1, vec2):
    """
    Input (ra,dec) vectors in radians;
    output great circle distance in radians.

    Parameters
    ----------
    vec1, vec2 : number
        Position in radians.

    Returns
    -------
    ans : number
        Great circle distance in radians.

    References
    ----------
    http://wiki.astrogrid.org/bin/view/Astrogrid/CelestialCoordinates
    
    """
    ra1,dec1=vec1
    ra2,dec2=vec2
    ans=ahav( hav(dec1-dec2) + math.cos(dec1)*math.cos(dec2)*hav(ra1-ra2) )
    return ans
