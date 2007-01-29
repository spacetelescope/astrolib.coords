from astrodate import utc2jd
import datetime

stamp=datetime.datetime.utcnow()
print "Now (GM) = ", stamp

print "Now (UTC JD): %f"%utc2jd(stamp)
