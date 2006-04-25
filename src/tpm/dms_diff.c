/* file: $RCSfile: dms_diff.c,v $
** rcsid: $Id: dms_diff.c,v 1.7 2003/05/15 20:09:26 jwp Exp $
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
static char *rcsid = "$Id: dms_diff.c,v 1.7 2003/05/15 20:09:26 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: dms_diff.c,v $ - difference of dms angles
** *******************************************************************
*/

#include "times.h"

DMS
dms_diff(DMS dms1, DMS dms2)
{
    dmsDecDegrees(dms1, dmsGetDegrees(dms2));
    dmsDecMinutes(dms1, dmsGetMinutes(dms2));
    dmsDecSeconds(dms1, dmsGetSeconds(dms2));

    return(dms1);
}
