/* file: $RCSfile: h2hms.c,v $
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
** $RCSfile: h2hms.c,v $ - convert scalar time to hms time
** *******************************************************************
*/

#include "times.h"

HMS
h2hms(double h)
{
    HMS hms;

    hmsSetHours(hms, h);
    hmsSetMinutes(hms, 0.0);
    hmsSetSeconds(hms, 0.0);

    return(hms);
}
