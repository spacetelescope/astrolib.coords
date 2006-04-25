/* file: $RCSfile: ymd2dd.c,v $
** rcsid: $Id: ymd2dd.c,v 1.12 2003/09/09 21:18:47 jwp Exp $
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
static char *rcsid = "$Id: ymd2dd.c,v 1.12 2003/09/09 21:18:47 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: ymd2dd.c,v $ - convert a ymd time into a scalar day
** note the day is a double, not an int
** *******************************************************************
*/

#include "times.h"

double
ymd2dd(YMD ymd)
{
    double dd;
    double j0;
    double j;

    /* normalize the time */
    ymd = ymd2ymd(ymd);

    /* get the julian day number of the target date */
    j = ymd2j(ymd);

    /* get the julian day number of the start of the year */
    j0 = gcal2j(ymdGetYear(ymd), 1, 1) - 0.5;

    dd = j - j0 + 1;

    return(dd);
}
