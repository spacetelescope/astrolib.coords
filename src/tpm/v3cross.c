/* file: $RCSfile: v3cross.c,v $
** rcsid: $Id$
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

/*
** *******************************************************************
** $RCSfile: v3cross.c,v $ - 3-vector cross product
** *******************************************************************
*/

#include "vec.h"

V3
v3cross(V3 v1, V3 v2)
{
    V3 v;

    if (v3GetType(v1) == SPHERICAL) {
	v1 = v3s2c(v1);
    }

    if (v3GetType(v2) == SPHERICAL) {
	v2 = v3s2c(v2);
    }

    v = v3init(CARTESIAN);

    v3SetX(v, v3GetY(v1) * v3GetZ(v2) - v3GetZ(v1) * v3GetY(v2));
    v3SetY(v, v3GetZ(v1) * v3GetX(v2) - v3GetX(v1) * v3GetZ(v2));
    v3SetZ(v, v3GetX(v1) * v3GetY(v2) - v3GetY(v1) * v3GetX(v2));

    return(v);
}
