/* file: $RCSfile: ydd2ymd.c,v $
** rcsid: $Id: ydd2ymd.c,v 1.10 2003/09/09 21:18:47 jwp Exp $
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
static char *rcsid = "$Id: ydd2ymd.c,v 1.10 2003/09/09 21:18:47 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: ydd2ymd.c,v $ - given a year and a day, return a ymd structure
** note that dd is a double, not an int.
** it can have a fractional part.
** *******************************************************************
*/

#include "times.h"

YMD
ydd2ymd(int y, double dd)
{
    YMD ymd;

    ymdSetYear(ymd, y);
    ymdSetMonth(ymd, 1);
    ymdSetDay(ymd, dd);
    ymdSetHours(ymd, 0.0);
    ymdSetMinutes(ymd, 0.0);
    ymdSetSeconds(ymd, 0.0);

    return(ymd);
}
