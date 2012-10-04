"""
This routine wraps the `pytpm.blackbox` routine in order to apply
the longitude convention preferred in coords. All `astrolib.coords`
routines should call `~astrolib.coords.pytpm_wrapper.blackbox`
instead of `pytpm.blackbox`.

Since pytpm is itself a wrapper for the TPM library, the change
could have been made there; but the modulo operator in C only
works on integers, so it was simpler to do it in python. Also,
this leaves pytpm itself as a more transparent wrapper for TPM.

"""
import pytpm
import astrodate, datetime

def blackbox(x,y,instate,outstate,epoch,equinox,timetag=None):
    """
    Parameters
    ----------
    x, y : float
        Position in decimal degrees.

    instate, outstate : int
        The TPM states of the position.

    epoch : float
        Epoch of the position.

    equinox : float
        Equinox of the position.

    timetag : `~astrolib.coords.astrodate.AstroDate`
        Timetag of returned coordinate.

    Returns
    -------
    r, d : float
        Converted coordinate.

    """
    if timetag == None:
        timetag=astrodate.AstroDate()
    try:
        r,d=pytpm.blackbox(x,y,instate,outstate,epoch,equinox,timetag.jd)
    except AttributeError: #support forgetful users
        astrotag=astrodate.AstroDate(timetag)
        r,d=pytpm.blackbox(x,y,instate,outstate,epoch,equinox,astrotag.jd)
        
    #Convert longitude to astrolib/coords convention
    r=r%360.0
    return r,d
