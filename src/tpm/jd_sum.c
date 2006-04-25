/* file: $RCSfile: jd_sum.c,v $
** rcsid: $Id: jd_sum.c,v 1.11 2003/09/09 21:18:47 jwp Exp $
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
static char *rcsid = "$Id: jd_sum.c,v 1.11 2003/09/09 21:18:47 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: jd_sum.c,v $ - sum of two jd times
** *******************************************************************
*/

#include "times.h"

JD
jd_sum(JD jd1, JD jd2)
{
    jdIncDay(jd1, jdGetDay(jd2));
    jd1.hms = hms_sum(jd1.hms, jd2.hms);

    return(jd1);
}
