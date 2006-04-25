/* file: $RCSfile: equ2ecl.c,v $
** rcsid: $Id: equ2ecl.c,v 1.4 2003/09/03 20:19:12 jwp Exp $
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
static char *rcsid = "$Id: equ2ecl.c,v 1.4 2003/09/03 20:19:12 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: equ2ecl.c,v $
** convert a state vector from FK4 equatorial to ecliptic
** *******************************************************************
*/

#include "astro.h"

V6
equ2ecl(V6 v6, double obl)
{
    v6 = m3v6(m3Rx(obl), v6);

    return(v6);
}
