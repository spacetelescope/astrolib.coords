/* file: $RCSfile: jd_now.c,v $
** rcsid: $Id: jd_now.c,v 1.11 2003/09/09 21:18:47 jwp Exp $
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
static char *rcsid = "$Id: jd_now.c,v 1.11 2003/09/09 21:18:47 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: jd_now.c,v $ - return the current UTC julian day number
** *******************************************************************
*/

#include <time.h>
#include "times.h"

JD
jd_now(void)
{
    JD jd;
    double j;
    time_t t;

    /* get the julian day number of the epoch */
    j = gcal2j(1970, 1, 1) - 0.5;

    /* get the elapsed seconds since the unix epoch */
    t = time(&t);

    /* offset to now */
    j += (double)t / 86400;

    jd = j2jd(j);

    return(jd);
}
