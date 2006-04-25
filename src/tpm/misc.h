/* file: $RCSfile: misc.h,v $
** rcsid: $Id: misc.h,v 1.23 2003/09/22 18:25:38 jwp Exp $
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
** $RCSfile: misc.h,v $ - header file for miscellaneous routines
** *******************************************************************
*/

#ifndef MISC_H

#include <stdio.h>

#define REAL	(0)
#define IMAG	(1)

/* EXTERN_START */
extern char *basename(char *path);
extern double brent(double (*func)(double), double ax, double bx, double cx, double tol);
extern double comb(int n, int r);
extern double fact(int n);
extern double gaussian(int seed, double mean, double sigma);
extern double golden(double (*func)(double), double ax, double bx, double cx, double tol);
extern double mag2size(double mag, double scale);
extern double polint(double *xa, double *ya, int n, double x, double *dy);
extern double qromb(double (*func)(double), double a, double b, double eps, int imax);
extern double qsimp(double (*func)(double), double a, double b, double eps, int imax);
extern double qtrap(double (*func)(double), double a, double b, double eps, int imax);
extern double ratint(double *xa, double *ya, int n, double x, double *dy);
extern double rtbis(double (*func)(double), double x_1, double y_1, double x_2, double y_2, double xacc);
extern double rtflsp(double (*func)(double), double x_1, double y_1, double x_2, double y_2, double xacc);
extern double rtsec(double (*func)(double), double x_1, double y_1, double x_2, double y_2, double xacc);
extern double spline(double *xtab, double *ytab, int n, double *ypp, double x);
extern double trapzd(double (*func)(double), double a, double b, int n);
extern double uniform(int seed, double a, double b);
extern double zbrent(double (*func)(double), double x_1, double y_1, double x_2, double y_2, double tol);
extern int amoeba(double **p, double *y, int ndim, double ftol, double (*funk)(double *), int max_iter);
extern int bit_clear(long bit);
extern int bit_init(long need);
extern int bit_query(long bit);
extern int bit_set(long bit);
extern int c_contour(FILE *ostream, double *image, int nrows, int ncols, double min, double max, int nlevels, char *labels[], int nlabels);
extern int crc_16(char *buf, int n);
extern int crc_32(char *buf, int n);
extern int crc_ccitt(char *buf, int n);
extern int makeargw(char *argw[], char *buffer, char *delim);
extern int rleDecode(char *rbuf, char *ebuf, int elen);
extern int rleEncode(char *ebuf, char *rbuf, int rlen);
extern int spline_prep(double *xtab, double *ytab, int n, double *ypp);
extern int zbrac(double (*func)(double), double x_1, double x_2, double *ax, double *bx);
extern int zbrak(double (*func)(double), double x_1, double x_2, int n, double *xb1, double *xb2, int nb);
extern long bit_near(long bit);
extern void bit_status(FILE *stream);
extern void convlv(double *s, int n, double *r, int m, int isign, double *ans[2]);
extern void cosft(double *y, int n, int isign);
extern void dHeapDown(double *buf, long k, long n, long *aux);
extern void dHeapSort(double *buf, long n, long *aux);
extern void dHeapUp(double *buf, long k, long *aux);
extern void dft(double J[2], double *t, double *y, int n, double f);
extern void fft(double *y, int nn, int isign);
extern void fresnel(double w, double *C, double *S);
extern void heapSort(double *d, long n, long *aux);
extern void lHeapDown(long *buf, long k, long n, long *aux);
extern void lHeapSort(long *buf, long n, long *aux);
extern void lHeapUp(long *buf, long k, long *aux);
extern void lsnp(double *x, double *y, int n, double ofac, double hifac, double *px, double *py, int np, int *nout, int *jmax, double *prob);
extern void meanvar(double *y, int n, double *mean, double *var);
extern void mnbrak(double (*func)(double), double x_1, double x_2, double *ax, double *bx, double *cx);
extern void realft(double *f, int n, int isign);
extern void sinft(double *y, int n);
extern void twofft(double *f1, double *f2, double *F1[2], double *F2[2], int n, int isign);
/* EXTERN_STOP */

#define MISC_H

#endif
