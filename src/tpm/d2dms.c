/* file: $RCSfile: d2dms.c,v $
** rcsid: $Id: d2dms.c,v 1.10 2003/05/15 20:09:26 jwp Exp $
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
static char *rcsid = "$Id: d2dms.c,v 1.10 2003/05/15 20:09:26 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: d2dms.c,v $ - convert scalar degrees to dms angle
** *******************************************************************
*/

#include "times.h"

DMS
d2dms(double d)
{
    DMS dms;

    dmsSetDegrees(dms, d);
    dmsSetMinutes(dms, 0.0);
    dmsSetSeconds(dms, 0.0);

    return(dms);
}
