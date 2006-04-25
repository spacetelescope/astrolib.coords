/* file: $RCSfile: hms_diff.c,v $
** rcsid: $Id: hms_diff.c,v 1.8 2003/09/09 21:18:47 jwp Exp $
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
static char *rcsid = "$Id: hms_diff.c,v 1.8 2003/09/09 21:18:47 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: hms_diff.c,v $ - difference of hms times
** *******************************************************************
*/

#include "times.h"

HMS
hms_diff(HMS hms1, HMS hms2)
{
    hmsDecHours(hms1, hmsGetHours(hms2));
    hmsDecMinutes(hms1, hmsGetMinutes(hms2));
    hmsDecSeconds(hms1, hmsGetSeconds(hms2));

    return(hms1);
}
