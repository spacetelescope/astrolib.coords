/* file: $RCSfile: v3s2c.c,v $
** rcsid: $Id: v3s2c.c,v 1.6 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: v3s2c.c,v 1.6 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: v3s2c.c,v $ - 3-vector spherical to cartesian
** *******************************************************************
*/

#include "vec.h"

/* some convenience macros */
#define X	(v3GetX(vc))
#define Y	(v3GetY(vc))
#define Z	(v3GetZ(vc))
#define R	(v3GetR(vs))
#define A	(v3GetAlpha(vs))
#define D	(v3GetDelta(vs))

V3
v3s2c(V3 vs)
{
    double rcosd;
    V3 vc;

    if (v3GetType(vs) == CARTESIAN) {
	return(vs);
    }

    vc = v3init(CARTESIAN);

    rcosd = R*cos(D);

    v3SetX(vc, rcosd*cos(A));
    v3SetY(vc, rcosd*sin(A));
    v3SetZ(vc, R*sin(D));

    return(vc);
}
