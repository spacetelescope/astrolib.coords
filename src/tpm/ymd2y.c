/* file: $RCSfile: ymd2y.c,v $
** rcsid: $Id$
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
