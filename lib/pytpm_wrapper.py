import pytpm
""" This routine wraps the pytpm.blackbox routine in order to apply
the longitude convention preferred in coords. All astrolib.coords routines
should call pytpm_wrapper.blackbox() instead of pytpm.blackbox().
    Since pytpm is itself a wrapper for the TPM library, the change could
have been made there; but the modulo operator in C only works on integers,
so it was simpler to do it in python. Also, this leaves pytpm itself as a more
transparent wrapper for TPM."""

def blackbox(x,y,instate,outstate,epoch,equinox):
    r,d=pytpm.blackbox(x,y,instate,outstate,epoch,equinox)
    #Convert longitude to astrolib/coords convention
    r=r%360.0
    return r,d
    
