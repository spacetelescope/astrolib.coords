// Module name
%module pytpm


// Headers: these just include the corresponding .h files
%{
#include "times.h"
#include "m3.h"
#include "v3.h"
#include "m6.h"
#include "v6.h"
#include "tpm.h"
%}

// Define some (but not all) of the useful macros
#define b1950   (2433282.42345905)
#define j2000   (2451545.0)
/* the julian century */
#define CJ	(36525.0)
/* the tropical century at 1900.0 */
#define CB	(36524.21987817305)


// Define some states so we can use them
#define s01 1
#define s02 2
#define s03 3
#define s04 4
#define s05 5
#define s06 6


// Try a black box approach
%include "typemaps.i"

void blackbox(double x1, double y1, // input position in degrees
	      int s1, int s2,       // input state, output state
	      double epoch, double equinox, // this is probably wrong...
	      double *OUTPUT, double *OUTPUT);


