/* file: $RCSfile: v32v6.c,v $
** rcsid: $Id: v32v6.c,v 1.5 2003/09/09 21:52:53 jwp Exp $
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
static char *rcsid = "$Id: v32v6.c,v 1.5 2003/09/09 21:52:53 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: v32v6.c,v $ - upgrade a 3-vector to a 6-vector
** *******************************************************************
*/

#include "vec.h"

V6
v32v6(V3 v3)
{
    V6 v6;

    v6 = v6init(v3GetType(v3));
    v6SetPos(v6, v3);

    return(v6);
}
