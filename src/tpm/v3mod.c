/* file: $RCSfile: v3mod.c,v $
** rcsid: $Id: v3mod.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: v3mod.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: v3mod.c,v $ - 3-vector modulus
** *******************************************************************
*/

#include "vec.h"

double
v3mod(V3 v)
{
    double x = 0.0;

    if (v3GetType(v) == SPHERICAL) {
	x = fabs(v3GetR(v));
    } else {
	x += v3GetX(v) * v3GetX(v);
	x += v3GetY(v) * v3GetY(v);
	x += v3GetZ(v) * v3GetZ(v);
	x = sqrt(x);
    }

    return(x);
}
