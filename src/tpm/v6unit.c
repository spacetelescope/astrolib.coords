/* file: $RCSfile: v6unit.c,v $
** rcsid: $Id: v6unit.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: v6unit.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: v6unit.c,v $ - return a unit 6-vector
** *******************************************************************
*/

#include "vec.h"

V6
v6unit(V6 v)
{
    double m;

    m = v6mod(v);
    if (m != 0.0) {
	v = v6scale(v, 1/m);
    }

    return(v);
}
