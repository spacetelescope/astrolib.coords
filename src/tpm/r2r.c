/* file: $RCSfile: r2r.c,v $
** rcsid: $Id: r2r.c,v 1.10 2003/09/09 21:18:47 jwp Exp $
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
static char *rcsid = "$Id: r2r.c,v 1.10 2003/09/09 21:18:47 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: r2r.c,v $ - normalize scalar radians
** *******************************************************************
*/

#include "times.h"

double
r2r(double r)
{
    if (r < 0.0) {
	r += ceil(r / (-2*M_PI)) * (2*M_PI);
    }
    if (r >= (2 * M_PI)) {
	r -= floor(r / (2*M_PI)) * (2*M_PI);
    }

    return(r);
}
