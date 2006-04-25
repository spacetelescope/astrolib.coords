/* file: $RCSfile: v3delta.c,v $
** rcsid: $Id: v3delta.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
** Copyright Jeffrey W Percival
** *******************************************************************
** Space Astronomy Laboratory
** University of Wisconsin
** 1150 University Avenue
** Madison, WI 53706 USA
** *******************************************************************
** Do not use this software without attribution.
** Do not remove or alter any of the lines above.
** *******************************************************************
*/
static char *rcsid = "$Id: v3delta.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: v3delta.c,v $ - return the angle out of the x-y plane (declination)
** *******************************************************************
*/

#include "vec.h"

double
v3delta(V3 v)
{
    double delta;

    if (v3GetType(v) == CARTESIAN) {
	v = v3c2s(v);
    }

    delta = v3GetDelta(v);
    if (v3GetR(v) < 0.0) {
	delta *= -1.0;
    }

    /* map onto -pi to pi */
    if (delta <= -M_PI) {
	delta += ceil(delta / (-2 * M_PI)) * (2 * M_PI);
    }
    if (delta > M_PI) {
	delta -= floor(delta / (2 * M_PI)) * (2 * M_PI);
    }

    if (delta > M_PI/2) {
	delta = M_PI - delta;
    }

    if (delta < -M_PI/2) {
	delta = -M_PI - delta;
    }

    return(delta);
}
