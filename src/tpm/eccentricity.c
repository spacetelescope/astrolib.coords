/* file: $RCSfile: eccentricity.c,v $
** rcsid: $Id: eccentricity.c,v 1.10 2003/09/03 20:19:12 jwp Exp $
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
static char *rcsid = "$Id: eccentricity.c,v 1.10 2003/09/03 20:19:12 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: eccentricity.c,v $
** return the eccentricity of the earth's orbit
** from Exp. Supp. 1992, p. 171
** *******************************************************************
*/

#include "astro.h"

double
eccentricity(double tdt)
{
    double T;	/* elapsed julian centuries */
    double e;

    T = (tdt - B1950) / CJ;

    e = 0.01673011 + T * (-0.00004193 + (T * (-0.000000126)));

    return(e);
}

double
eccentricity_dot(double tdt)
{
    double T;	/* elapsed julian centuries */
    double edot;

    T = (tdt - B1950) / CJ;

    edot = (-0.00004193 + 2 * (T * (-0.000000126)));

    return(edot);
}
