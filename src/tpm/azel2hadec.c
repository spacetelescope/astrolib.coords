/* file: $RCSfile: azel2hadec.c,v $
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
** $RCSfile: azel2hadec.c,v $
** convert a state vector form (az,el) to (ha,dec)
** *******************************************************************
*/

#include "astro.h"

V6
azel2hadec(V6 v6, double latitude)
{
    /* do a simple rotation about Z through 180 degrees */
    v6 = m3v6(m3Rz(-M_PI), v6);

    /* rotate by -(90-latitude) in the plane of the meridian */
    v6 = m3v6(m3Ry(-(M_PI/2 - latitude)), v6);

    return(v6);
}
