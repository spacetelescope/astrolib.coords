/* file: $RCSfile: h2h.c,v $
** rcsid: $Id: h2h.c,v 1.10 2003/09/09 21:18:47 jwp Exp $
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
static char *rcsid = "$Id: h2h.c,v 1.10 2003/09/09 21:18:47 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: h2h.c,v $ scalar hours
** *******************************************************************
*/

#include <math.h>
#include "times.h"

double
h2h(double h)
{
    if (h < 0.0) {
	h += ceil(h / -24.0) * 24.0;
    }
    if (h >= 24.0) {
	h -= floor(h / 24.0) * 24.0;
    }

    return(h);
}
