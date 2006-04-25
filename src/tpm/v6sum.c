/* file: $RCSfile: v6sum.c,v $
** rcsid: $Id: v6sum.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: v6sum.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: v6sum.c,v $ - 6-vector sum
** *******************************************************************
*/

#include "vec.h"

V6
v6sum(V6 v1, V6 v2)
{
    if (v6GetType(v1) == SPHERICAL) {
	v1 = v6s2c(v1);
    }

    if (v6GetType(v2) == SPHERICAL) {
	v2 = v6s2c(v2);
    }

    v6IncX(v1, v6GetX(v2));
    v6IncY(v1, v6GetY(v2));
    v6IncZ(v1, v6GetZ(v2));
    v6IncXDot(v1, v6GetXDot(v2));
    v6IncYDot(v1, v6GetYDot(v2));
    v6IncZDot(v1, v6GetZDot(v2));

    return(v1);
}
