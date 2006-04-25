/* file: $RCSfile: v6delta.c,v $
** rcsid: $Id: v6delta.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: v6delta.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: v6delta.c,v $ - return the angle out of the x-y plane (declination)
** *******************************************************************
*/

#include "vec.h"

double
v6delta(V6 v)
{
    return(v3delta(v6GetPos(v)));
}
