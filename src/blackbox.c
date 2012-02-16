#include <Python.h>

#include "tpm/astro.h"

void blackbox(double x1, double y1, int s1, int s2,
	      double epoch, double equinox, double timetag,
	      double *x2, double *y2)

{
  struct s_tstate tstate;
  struct s_v6 pvec[N_TPM_STATES];
  struct s_v6 v6;

  //  double epoch = J2000;
  //  double equinox = J2000;

  // Input params are in degrees. Convert them to radians & set things up.
  // **NB: Always call d2r(x1),d2r(y1) before using them.

  v6=v6init(SPHERICAL); // v6=Spherical(lon,lat) #r=FarAway
  v6SetAlpha(v6,d2r(x1));
  v6SetDelta(v6,d2r(y1));
  v6SetR(v6,1e9);

  tpm_data(&tstate, TPM_INIT); 
  tstate.utc = timetag; 
  tpm_data(&tstate, TPM_ALL);

  pvec[s1]=v6;

  (void)tpm(pvec,s1,s2,epoch,equinox,&tstate);

  v6=pvec[s2];
  v6 = v6c2s(v6);
  *x2 = r2d(v6GetAlpha(v6));
  *y2 = r2d(v6GetDelta(v6));

  return;
}


/*
* here begins the python interface
*/

static PyObject *
blackbox_shim(PyObject *self, PyObject *args)
{
	double x1;
	double y1;
	int s1;
	int s2;
	double epoch;
	double equinox;
	double timetag;
	double x2;
	double y2;

	PyObject *rval;

	if (! PyArg_ParseTuple(args, "ddiiddd", 
		&x1,&y1,&s1,&s2,&epoch,&equinox,&timetag) )
		return NULL;

	blackbox(x1, y1, s1, s2, epoch, equinox, timetag, &x2, &y2);
	rval = Py_BuildValue("dd",x2,y2);
	return rval;
}


static char *module_documentation = "";

static struct PyMethodDef methods[] = {
    {"blackbox",    blackbox_shim,    1,    "" },
    {NULL,        NULL}        /* sentinel */
};

PyMODINIT_FUNC
init_pytpm(void)
{
    /* Create the module and add the functions */
    (void) Py_InitModule4("_pytpm", methods,
        module_documentation,
        (PyObject *) NULL, PYTHON_API_VERSION);

    /* Check for errors */
    if (PyErr_Occurred())
        Py_FatalError("can't initialize module _pytpm");
}

