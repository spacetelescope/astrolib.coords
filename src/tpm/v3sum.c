/* file: $RCSfile: v3sum.c,v $
** rcsid: $Id: v3sum.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: v3sum.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: v3sum.c,v $ - 3-vector sum
** *******************************************************************
*/

#include "vec.h"

V3
v3sum(V3 v1, V3 v2)
{
    if (v3GetType(v1) == SPHERICAL) {
	v1 = v3s2c(v1);
    }

    if (v3GetType(v2) == SPHERICAL) {
	v2 = v3s2c(v2);
    }

    v3IncX(v1, v3GetX(v2));
    v3IncY(v1, v3GetY(v2));
    v3IncZ(v1, v3GetZ(v2));

    return(v1);
}
