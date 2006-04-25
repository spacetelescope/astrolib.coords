/* file: $RCSfile: ymd2y.c,v $
** rcsid: $Id: ymd2y.c,v 1.11 2003/09/09 21:18:47 jwp Exp $
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
static char *rcsid = "$Id: ymd2y.c,v 1.11 2003/09/09 21:18:47 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: ymd2y.c,v $ - convert a ymd time into a scalar year
** *******************************************************************
*/

#include "times.h"

double
ymd2y(YMD ymd)
{
    double y;

    /* normalize the time */
    ymd = ymd2ymd(ymd);

    y = (double)ymdGetYear(ymd) + (ymd2dd(ymd) / y2doy(ymdGetYear(ymd)));

    return(y);
}
