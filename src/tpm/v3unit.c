/* file: $RCSfile: v3unit.c,v $
** rcsid: $Id: v3unit.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: v3unit.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: v3unit.c,v $ - return a unit 3-vector
** *******************************************************************
*/

#include "vec.h"

V3
v3unit(V3 v)
{
    double m;

    m = v3mod(v);
    if (m != 0.0) {
	v = v3scale(v, 1/m);
    }

    return(v);
}
