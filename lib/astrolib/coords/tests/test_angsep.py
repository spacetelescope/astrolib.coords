import astrolib.coords.angsep as angsep
import math
import nose.tools

# not sure what this is... looks like something for interactive use
@nose.tools.nottest
def test_init(value, units):
    s=angsep.AngSep(value,units=units)
    assert s.value == value, "Value failed: %f != %f"%(s.value,value)
    assert s.units == units, "Units failed: %s != %s"%(s.units,units)

def test_gt_sep():
    s1=angsep.AngSep(5)
    s2=angsep.AngSep(7)
    assert s2 > s1, "gt failed"

def  test_ge_sep():
    s1=angsep.AngSep(5)
    s2=angsep.AngSep(7)
    assert s2 >= s1, "ge failed"

def test_lt_sep():
    s1=angsep.AngSep(10)
    s2=angsep.AngSep(7)
    assert s2 < s1, "lt failed"

def test_eq_sep():
    s1=angsep.AngSep(10)
    s2=angsep.AngSep(4)
    assert s1 == s1, "eq failed"
    assert s1 != s2, "ne failed"


#................................................

def test_gt_num():
    s2=angsep.AngSep(7)
    assert s2 > 3, "gt failed"

def test_lt_num():
    s2=angsep.AngSep(7)
    assert s2 < 10, "lt failed"

def test_eq_num():
    s1=angsep.AngSep(10)
    assert s1 == 10, "eq failed"
    assert s1 != 6, "ne failed"

#..................................
def test_addsep():
    s1=angsep.AngSep(3)
    s2=angsep.AngSep(5)
    s3=s1+s2
    assert s3._internal == s1._internal+s2._internal, "addsep failed"

def test_addnum():
    s1=angsep.AngSep(3)
    s2=s1+5
    assert s2.value == s1.value + 5, "addnum failed"

def test_subtractsep():
    s1=angsep.AngSep(3)
    s2=angsep.AngSep(5)
    s3=s2-s1
    assert s3._internal == s2._internal-s1._internal, "subtractsep failed"

def test_subtractnum():
    s1=angsep.AngSep(30)
    s2=s1-5
    assert s2.value == s1.value - 5, "subtractnum failed"


#def test_iaddsep():
    #s1=angsep.AngSep(3)
    #s2=angsep.AngSep(5)
    #old=s1._internal
    #s1.__iadd__(s2)
    #assert s1._internal == old+s2._internal, "iaddsep failed"

#def test_iaddnum():
    #s1=angsep.AngSep(3)
    #s1.__iadd__(5)
    #assert s1.value == 8, "iaddnum failed"

#def test_isubtractsep():
    #s1=angsep.AngSep(30)
    #s2=angsep.AngSep(5)
    #old=s1._internal
    #s1.__isub__(s2)
    #assert s1._internal == old-s2._internal, "isubtractsep failed"

#def test_isubtractnum():
    #s1=angsep.AngSep(30)
    #s1.__isub__(5)
    #assert s1.value == 30 - 5, "isubtractnum failed"

def test_mulsep():
    s1=angsep.AngSep(3)
    s2=angsep.AngSep(5)
    s3=s1*s2
    assert s3._internal == s1._internal*s2._internal, "mulsep failed"

def test_mulnum():
    s1 = angsep.AngSep(10)
    s2=s1*3
    assert s2.value == s1.value * 3, "mulnum failed"

#.............................................................
def test_approx_sep():
    s1=angsep.AngSep(22,units='deg')
    s2=angsep.AngSep(21.999,units='deg')
    assert s1.approx(s2,0.1), "approx sep failed"
    assert not s1.approx(s2,0.00001), "approx sep failed"

def test_approx_num():
    s1=angsep.AngSep(22)
    assert s1.approx(23,2), "approx num failed"
    assert not s1.approx(26,2), "approx num failed"

def test_approx_bug():
    """Demonstrate the bug related to units"""
    s1=angsep.AngSep(5)
    s2=angsep.AngSep(3)
    assert not s1.approx(s2,0.5), "approx bugtest failed"

#.............................................................
def test_setunit():
    s1=angsep.AngSep(3600)
    s1.setunits('deg')
    assert s1.value == 1.0 , "set unit to degrees failed"
    s1.setunits('rad')
    assert s1.value == math.pi/180.0, "set unit to rad failed"
    s1.setunits('arcsec')
    assert s1.value == 3600, "set unit to arcsec failed"
#.............................................................

def run():
    test_gt_sep()
    test_lt_sep()
    test_eq_sep()

    test_gt_num()
    test_lt_num()
    test_eq_num()

    test_addsep()
    test_addnum()
    test_subtractsep()
    test_subtractnum()

    test_mulsep()
    test_mulnum()

    test_approx_sep()
    test_approx_num()
    test_approx_bug()

    test_setunit()

    #test_iaddsep()
    #test_iaddnum()
    #test_isubtractsep()
    #test_isubtractnum()

