/* file: $RCSfile: m3I.c,v $
** rcsid: $Id: m3I.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: m3I.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: m3I.c,v $ - the identity 3-matrix (scaled by the given value)
** *******************************************************************
*/

#include "vec.h"

M3
m3I(double x)
{
    M3 m;

    m3SetXX(m, x);
    m3SetXY(m, 0);
    m3SetXZ(m, 0);

    m3SetYX(m, 0);
    m3SetYY(m, x);
    m3SetYZ(m, 0);

    m3SetZX(m, 0);
    m3SetZY(m, 0);
    m3SetZZ(m, x);

    return(m);

}
