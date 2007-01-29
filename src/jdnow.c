#include <stdio.h>
#include "tpm/astro.h"

/* Simple program used to test astrodate.utc2jd function     */
/* against TPM utc_now function. Use together with jdnow.py. */

int main()
{

  double stamp;
  stamp=utc_now();
  printf("Now (UTC JD): %f\n",stamp);
}
