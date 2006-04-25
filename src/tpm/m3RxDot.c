/* file: $RCSfile: m3RxDot.c,v $
** rcsid: $Id: m3RxDot.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: m3RxDot.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: m3RxDot.c,v $ - the R1-dot matrix from Yallop et al., AJ 97, 274.
** *******************************************************************
*/

#include "vec.h"

M3
m3RxDot(double x, double xdot)
{
    M3 m3;

    m3 = m3O();
    m3SetYY(m3, xdot * -sin(x));
    m3SetYZ(m3, xdot * cos(x));
    m3SetZY(m3, xdot * -cos(x));
    m3SetZZ(m3, xdot * -sin(x));

    return(m3);

}
