/* file: $RCSfile: dms2hms.c,v $
** rcsid: $Id: dms2hms.c,v 1.7 2003/05/15 20:09:26 jwp Exp $
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
static char *rcsid = "$Id: dms2hms.c,v 1.7 2003/05/15 20:09:26 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: dms2hms.c,v $ - convert dms angle to hms time
** *******************************************************************
*/

#include "times.h"

HMS
dms2hms(DMS dms)
{
    HMS hms;

    hmsSetHours(hms, dmsGetDegrees(dms) / 15.0);
    hmsSetMinutes(hms, dmsGetMinutes(dms) / 15.0);
    hmsSetSeconds(hms, dmsGetSeconds(dms) / 15.0);

    return(hms);
}
