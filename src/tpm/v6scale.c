/* file: $RCSfile: v6scale.c,v $
** rcsid: $Id: v6scale.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: v6scale.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: v6scale.c,v $ - 6-vector scaling
** *******************************************************************
*/

#include "vec.h"

V6
v6scale(V6 v, double s)
{
    if (v6GetType(v) == CARTESIAN) {
	v6MulX(v, s);
	v6MulY(v, s);
	v6MulZ(v, s);
	v6MulXDot(v, s);
	v6MulYDot(v, s);
	v6MulZDot(v, s);
    } else {
	v6MulR(v, s);
	v6MulRDot(v, s);
    }

    return(v);
}
