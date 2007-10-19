/* file: $RCSfile: jd2j.c,v $
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
** $RCSfile: jd2j.c,v $ - convert a jd time into a scalar julian date
** *******************************************************************
*/

#include "times.h"

double
jd2j(JD jd)
{
    double j;

    j = jdGetDay(jd) + (hms2h(jd.hms) / 24.0);

    return(j);
}
