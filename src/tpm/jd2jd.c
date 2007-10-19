/* file: $RCSfile: jd2jd.c,v $
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
** $RCSfile: jd2jd.c,v $ - normalize a jd time
** *******************************************************************
*/

#include "times.h"

JD
jd2jd(JD jd)
{
    double x;

    /* convert to decimal days */
    x = jd2j(jd);
    jdSetDay(jd, floor(x));

    /* promote the hours part */
    x = (x - floor(x)) * 24.0;
    jdSetHours(jd, floor(x));

    /* promote the minutes part */
    x = (x - floor(x)) * 60.0;
    jdSetMinutes(jd, floor(x));

    /* promote the seconds part */
    x = (x - floor(x)) * 60.0;
    jdSetSeconds(jd, x);

    return(jd);
}
