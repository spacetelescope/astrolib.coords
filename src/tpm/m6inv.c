/* file: $RCSfile: m6inv.c,v $
** rcsid: $Id: m6inv.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: m6inv.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: m6inv.c,v $ - invert a 6-matrix
** we assume it is composed of orthogonal 3-matrices
** *******************************************************************
*/

#include "vec.h"

M6
m6inv(M6 m)
{
    m.m[0][0] = m3inv(m.m[0][0]);
    m.m[0][1] = m3inv(m.m[0][1]);
    m.m[1][0] = m3inv(m.m[1][0]);
    m.m[1][1] = m3inv(m.m[1][1]);

    return(m);
}
