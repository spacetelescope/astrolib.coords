/* file: $RCSfile: gcal2j.c,v $
** rcsid: $Id: gcal2j.c,v 1.6 2003/09/09 21:18:47 jwp Exp $
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
static char *rcsid = "$Id: gcal2j.c,v 1.6 2003/09/09 21:18:47 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: gcal2j.c,v $ - map a gregorian proleptic calendar date onto a julian day number
** the algorithm is from
** The Explanatory Supplement to the Astronomical Almanac (1992),
** section 12.92, equation 12.92-1, page 604.
** *******************************************************************
*/

#include "times.h"

double
gcal2j(int y, int m, int d)
{
    int j;

    j = (1461 * (y + 4800 + (m - 14) / 12)) / 4;
    j += (367 * (m - 2 - 12 * ((m - 14) / 12))) / 12;
    j -= (3 * ((y + 4900 + (m - 14) / 12) / 100)) / 4;
    j += d;
    j -= 32075;

    return((double)j);
}
