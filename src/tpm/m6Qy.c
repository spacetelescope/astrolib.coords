/* file: $RCSfile: m6Qy.c,v $
** rcsid: $Id: m6Qy.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: m6Qy.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: m6Qy.c,v $ - the Q2 matrix from Yallop et al., AJ 97, 274.
** *******************************************************************
*/

#include "vec.h"

M6
m6Qy(double y, double ydot)
{
    M6 m6;

    m6SetPP(m6, m3Ry(y));
    m6SetPV(m6, m3O());
    m6SetVP(m6, m3RyDot(y, ydot));
    m6SetVV(m6, m3Ry(y));

    return(m6);

}
