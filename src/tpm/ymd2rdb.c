/* file: $RCSfile: ymd2rdb.c,v $
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
** $RCSfile: ymd2rdb.c,v $ - convert a ymd time into an rdb time
** *******************************************************************
*/

#include "times.h"

double
ymd2rdb(YMD ymd)
{
    double rdb;

    /* make sure the time is well formed */
    ymd = ymd2ymd(ymd);

    rdb = (ymdGetYear(ymd) % 100) * 1e4;
    rdb += ymdGetMonth(ymd) * 1e2;
    rdb += ymdGetDay(ymd);
    rdb += ymdGetHours(ymd) / 1e2;
    rdb += ymdGetMinutes(ymd) / 1e4;
    rdb += ymdGetSeconds(ymd) / 1e6;

    return(rdb);
}
