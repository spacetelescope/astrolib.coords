/* file: $RCSfile: v3scale.c,v $
** rcsid: $Id: v3scale.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: v3scale.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: v3scale.c,v $ - 3-vector scaling
** *******************************************************************
*/

#include "vec.h"

V3
v3scale(V3 v, double s)
{
    if (v3GetType(v) == CARTESIAN) {
	v3MulX(v, s);
	v3MulY(v, s);
	v3MulZ(v, s);
    } else {
	v3MulR(v, s);
    }

    return(v);
}
