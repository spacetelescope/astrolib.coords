/* file: $RCSfile: dms2dms.c,v $
** rcsid: $Id: dms2dms.c,v 1.14 2003/05/15 20:09:26 jwp Exp $
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
static char *rcsid = "$Id: dms2dms.c,v 1.14 2003/05/15 20:09:26 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: dms2dms.c,v $ - normalize a dms angle
** *******************************************************************
*/

#include "times.h"

DMS
dms2dms(DMS dms)
{
    double x;

    /* convert to decimal degrees */
    x = dms2d(dms);
    dmsSetDegrees(dms, floor(x));

    /* promote the minutes part */
    x = (x - floor(x)) * 60.0;
    dmsSetMinutes(dms, floor(x));

    /* promote the seconds part */
    x = (x - floor(x)) * 60.0;
    dmsSetSeconds(dms, x);

    /* normalize the degrees */
    dmsSetDegrees(dms, d2d(dmsGetDegrees(dms)));

    return(dms);
}
