import position as P

class Tvalues:
    def __init__(self,epsilon):
        """ All values were defined by IDL ASTROLIB routines, usually
        euler but also bprecess and jprecess for the precession routines. """
        
        self.epsilon=epsilon
        #gal coords of cel(0,0)
        self.celzero_gal=(96.337272,-60.188553)

        #cel coords of gal(0,0)
        self.galzero_cel = (266.40499,-28.936174)

        #b1950 coords of j2000(0,0)
        self.b1950_zero=(359.35928, -0.27834947)

        #j2000 coords of b1950(0,0)
        self.j2000_zero = (0.64069095,0.27840945)

        #An arbitrary J2000 coord & its transformations
        self.arb=(123.345,65.432)
        self.eclarb=(108.56604,44.127898)
        self.galarb=(150.59328,32.970253)
        self.b1950arb=(122.19076, 65.582616)

        #Now test a negative set too
        self.arbneg=(234.567,-32.123)
        self.eclarbneg=(239.82987,-12.320041)
        self.galarbneg=(339.43003,18.677436)
        self.b1950arbneg=(233.78497,-31.960057)

        #Polaris from IDL precess docs
        self.polaris_j2000=(37.942917, 89.264056)
        self.polaris_j1985=(34.094708, 89.196472)

        
def test_celzero(t):
    """celestial zero -> galactic"""
    p1=P.Position((0.0,0.0))
    p2=P.Position(p1.galactic(),system="galactic")
    assert p2.within(P.Position(t.celzero_gal,system="galactic"),t.epsilon,units='arcsec'), "Fail: right=%s ans=%s"%(t.celzero_gal, p2.dd())

def test_galzero(t):
    p1=P.Position((0.0,0.0),system='galactic')
    p2=P.Position(p1.j2000(),system='celestial')
    assert p2.within(P.Position(t.galzero_cel),t.epsilon,units='arcsec'), "Fail: right = %s ans = %s"%(t.galzero_cel,p2.dd())

def test_bjzero(t):
    p1=P.Position((0.0,0.0))
    p2=P.Position(p1.b1950())
    assert p2.within(P.Position(t.b1950_zero),t.epsilon,units='arcsec'),"Fail: right = %s ans = %s"%(t.b1950_zero,p2.dd())

def test_jbzero(t):
    p1=P.Position((0.0,0.0),equinox='b1950')
    p2=P.Position(p1.j2000())
    assert p2.within(P.Position(t.j2000_zero),t.epsilon,units='arcsec'),"Fail: right = %s ans = %s"%(t.j2000_zero,p2.dd())

def test_eclzero(t):
    p1=P.Position((0.0,0.0))
    p2=P.Position(p1.ecliptic())
    assert p2.within(P.Position((0.0,0.0)),t.epsilon,units='arcsec'),"Fail: right = %s ans = %s"%((0.0,0.0),p2.dd())

def test_eclarb(t):
    p1=P.Position(t.arb)
    p2=P.Position(p1.ecliptic())
    assert p2.within(P.Position(t.eclarb),t.epsilon,units='arcsec'),"Fail: right = %s ans = %s"%(t.eclarb,p2.dd())
    
def test_galarb(t):
    p1=P.Position(t.arb)
    p2=P.Position(p1.galactic())
    assert p2.within(P.Position(t.galarb),t.epsilon,units='arcsec'),"Fail: right = %s ans = %s"%(t.galarb,p2.dd())
def test_b1950arb(t):
    p1=P.Position(t.arb)
    p2=P.Position(p1.b1950())
    assert p2.within(P.Position(t.b1950arb),t.epsilon,units='arcsec'),"Fail: right = %s ans = %s"%(t.b1950arb,p2.dd())

def test_j2000arb(t):
    p1=P.Position(t.galarb,system='galactic')
    p2=P.Position(p1.j2000())
    assert p2.within(P.Position(t.arb),t.epsilon,units='arcsec'),"Fail: right = %s ans = %s"%(t.arb,p2.dd())

#....................................
def test_eclarbneg(t):
    p1=P.Position(t.arbneg)
    p2=P.Position(p1.ecliptic())
    assert p2.within(P.Position(t.eclarbneg),t.epsilon,units='arcsec'),"Fail: right = %s ans = %s"%(t.eclarbneg,p2.dd())
    
def test_galarbneg(t):
    p1=P.Position(t.arbneg)
    p2=P.Position(p1.galactic())
    assert p2.within(P.Position(t.galarbneg),t.epsilon,units='arcsec'),"Fail: right = %s ans = %s"%(t.galarbneg,p2.dd())
def test_b1950arbneg(t):
    p1=P.Position(t.arbneg)
    p2=P.Position(p1.b1950())
    assert p2.within(P.Position(t.b1950arbneg),t.epsilon,units='arcsec'),"Fail: right = %s ans = %s"%(t.b1950arbneg,p2.dd())

def test_j2000arbneg(t):
    p1=P.Position(t.galarbneg,system='galactic')
    p2=P.Position(p1.j2000())
    assert p2.within(P.Position(t.arbneg),t.epsilon,units='arcsec'),"Fail: right = %s ans = %s"%(t.arbneg,p2.dd())
    
#.................................
def test_polaris(t):
    p1=P.Position(t.polaris_j1985,equinox=2446066.25)  #1985.0 - not smart yet)
    p2=P.Position(p1.j2000())
    assert p2.within(P.Position(t.polaris_j2000),t.epsilon,units='arcsec'),"Fail: right = %s ans = %s"%(t.polaris_j2000,p2.dd())
                                                                                                        

    
def run():
    run_hiprec(0.5)
    run_loprec(3)
    
def run_hiprec(epsilon=0.5):
    t=Tvalues(epsilon)
    test_celzero(t)
    test_galzero(t)
    test_bjzero(t)
    test_jbzero(t)
    test_eclzero(t)
#    test_eclarb(t)
    test_galarb(t)
    test_b1950arb(t)
    test_j2000arb(t)
    test_galarbneg(t)
    test_b1950arbneg(t)
    test_j2000arbneg(t)
    test_polaris(t)

def run_loprec(epsilon=3):
    t=Tvalues(epsilon)
    test_eclarb(t)
    test_eclarbneg(t)
