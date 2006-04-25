/* file: $RCSfile: precess.c,v $
** rcsid: $Id: precess.c,v 1.4 2003/09/03 20:19:12 jwp Exp $
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
static char *rcsid = "$Id: precess.c,v 1.4 2003/09/03 20:19:12 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: precess.c,v $
** precess a state vector
** *******************************************************************
*/

#include "astro.h"

#undef DEBUG

V6
precess(double j1, double j2, V6 v6, int pflag)
{
    M6 pm;	/* the precession matrix */

    pm = precess_m(j1, j2, pflag, PRECESS_INERTIAL);

#ifdef DEBUG
    (void)fprintf(stdout, "precess: pm \n%s\n", m6fmt(pm));
#endif

    v6 = m6v6(pm, v6);

    return(v6);
}
