""" Simple script used to test astrodate.utc2jd function
against TPM utc_now function. Use together with jdnow.c."""

from astrodate import utc2jd
import datetime

stamp=datetime.datetime.utcnow()
print "Now (GM) = ", stamp

print "Now (UTC JD): %f"%utc2jd(stamp)
