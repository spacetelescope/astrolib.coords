/* file: $RCSfile: rdb2ymd.c,v $
** rcsid: $Id: rdb2ymd.c,v 1.11 2003/09/09 21:18:47 jwp Exp $
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
static char *rcsid = "$Id: rdb2ymd.c,v 1.11 2003/09/09 21:18:47 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: rdb2ymd.c,v $ - convert a rdb time into a ymd time
** *******************************************************************
*/

#include "times.h"

YMD
rdb2ymd(double rdb)
{
    YMD ymd;

    ymdSetYear(ymd, (int)(rdb * 1e-4));
    rdb -= (ymdGetYear(ymd) * 1e4);
    ymdSetMonth(ymd, (int)(rdb * 1e-2));
    rdb -= (ymdGetMonth(ymd) * 1e2);
    ymdSetDay(ymd, (int)rdb);
    rdb -= (ymdGetDay(ymd));

    /* shift the fraction by 6 digits */
    rdb *= 1e6;
    rdb += 0.5;

    ymdSetHours(ymd, (int)(rdb * 1e-4));
    rdb -= (ymdGetHours(ymd) * 1e4);
    ymdSetMinutes(ymd, (int)(rdb * 1e-2));
    rdb -= (ymdGetMinutes(ymd) * 1e2);
    ymdSetSeconds(ymd, (int)rdb);
    rdb -= (ymdGetSeconds(ymd));

    ymdIncYear(ymd, 1900);

    return(ymd);
}
