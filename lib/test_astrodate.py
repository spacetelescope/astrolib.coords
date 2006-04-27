import astrodate as A

def test_jd():
    """ GIven a julian decimal year, convert it to JD """
    j1984=2445700.0
    d=A.AstroDate('J1984.0')
    ans=d.jd
    assert ans==j1984, "Fail: right = %f ans = %f"%(j1984,ans)

def test_inverse(epsilon):
    """ See if a round trip works """
    d1=A.AstroDate(1997.123)
    d2=A.AstroDate('JD%f'%d1.jd)
    assert abs(d1.year-d2.year)<epsilon, "Fail: d1.year %f, d2.year %f"%(d1.year,d2.year)

def test_jcase():
    d=A.AstroDate('J2345.3')
    assert isinstance(d,A.JulianDate),"jcase fails: not a JulianDate"

def test_jdcase():
    d=A.AstroDate('JD2345423.234')
    assert isinstance(d,A.JulianDate),"jdcase fails: not a JulianDate"

def test_mjdcase():
    d=A.AstroDate('MJD34546')
    assert isinstance(d,A.JulianDate),"mjdcase fails: not a JulianDate"

def test_numcase():
    d=A.AstroDate(1997.3)
    assert isinstance(d,A.JulianDate),"numcase fails: not a JulianDate"

def test_numstringcase():
    d=A.AstroDate('1997.3')
    assert isinstance(d,A.JulianDate),"numstrcase fails: not a JulianDate"

def test_numstringcase2():
    d=A.AstroDate('1997.3')
    assert d.year == 1997.3, "numstrcase2 fails: %f"%d.year

def test_bcase():
    d=A.AstroDate('B1964.3')
    assert isinstance(d,A.BesselDate),"bcase fails: not a BesselDate"

def test_repr():
    d1=A.AstroDate('J2003.4')
    assert d1.__repr__() == 'J2003.4', "repr failed: right %s ans %s"%(d1,'J2003.4')
    
def test_equals():
    d1=A.AstroDate('J1993.123')
    d2=A.AstroDate('J1993.123')
    assert d1.__equals__(d2), "equal fails"

def test_lt():
    d1=A.AstroDate('J2004.9')
    d2=A.AstroDate('J1950.3')
    assert d2.__lt__(d1), "lt fails"
    
def test_gt():
    d1=A.AstroDate('J2004.9')
    d2=A.AstroDate('J1950.3')
    assert d1.__gt__(d2), "gt fails"

def test_le():
    d1=A.AstroDate('J2004.9')
    d2=A.AstroDate('J1950.3')
    assert d2.__le__(d1), "lt fails"
    
def test_ge():
    d1=A.AstroDate('J2004.9')
    d2=A.AstroDate('J1950.3')
    assert d1.__ge__(d2), "gt fails"
    
def test_bequals():
    d1=A.AstroDate('B1993.123')
    d2=A.AstroDate('B1993.123')
    assert d1.__equals__(d2), "equal fails"

def test_blt():
    d1=A.AstroDate('B2004.9')
    d2=A.AstroDate('B1950.3')
    assert d2.__lt__(d1), "lt fails"
    
def test_bgt():
    d1=A.AstroDate('B2004.9')
    d2=A.AstroDate('B1950.3')
    assert d1.__gt__(d2), "gt fails"

def test_ble():
    d1=A.AstroDate('B2004.9')
    d2=A.AstroDate('B1950.3')
    assert d2.__le__(d1), "lt fails"
    
def test_bge():
    d1=A.AstroDate('B2004.9')
    d2=A.AstroDate('B1950.3')
    assert d1.__ge__(d2), "gt fails"

def test_crosscomp():
    d1=A.AstroDate('J2004.5')
    d2=A.AstroDate('B1956.8')
    assert d1.__ge__(d2), "crosscomp fails"
 
def run():
    test_jcase()
    test_jdcase()
    test_mjdcase()
    test_numcase()
    test_numstringcase()
    test_numstringcase2()
    test_bcase()
    test_inverse(0.0000000001)
#    test_jd()
    test_equals()
    test_repr()
    test_lt()
    test_gt()
    test_le()
    test_ge()
    test_bequals()
    test_blt()
    test_bgt()
    test_ble()
    test_bge()
    test_crosscomp()