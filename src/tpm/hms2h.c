/* file: $RCSfile: hms2h.c,v $
** rcsid: $Id: hms2h.c,v 1.8 2003/09/09 21:18:47 jwp Exp $
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
static char *rcsid = "$Id: hms2h.c,v 1.8 2003/09/09 21:18:47 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: hms2h.c,v $ - convert hms time into scalar time
** *******************************************************************
*/

#include "times.h"

double
hms2h(HMS hms)
{
    double h;

    h = hmsGetHours(hms);
    h += hmsGetMinutes(hms) / 60.0;
    h += hmsGetSeconds(hms) / 3600.0;

    return(h);
}
