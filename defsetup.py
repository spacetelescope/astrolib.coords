from __future__ import division # confidence high

import distutils.extension

import glob

# list of all the packages to be installed
pkg = [ 'astrolib.coords', 'astrolib', 'astrolib.coords.tests' ]


## This is an explicit list of all the source files in the tpm
## library.  I do not want to automatically generate it because I
## would need to distinguish between stand-alone coords installs
## and stsci_python installs, then search in different places
## depending what we found.  If you get a new version of the
## tpm library, you can do this to get a list suitable to use here:
#   ls src/tpm/*.c | sed -e 's/^/    "/' -e 's/$/",/' > file
tpm_src = [
    "src/tpm/aberrate.c",
    "src/tpm/argvParse.c",
    "src/tpm/azel2hadec.c",
    "src/tpm/d2d.c",
    "src/tpm/d2dms.c",
    "src/tpm/delta_AT.c",
    "src/tpm/dms2d.c",
    "src/tpm/dms2dms.c",
    "src/tpm/dms2hms.c",
    "src/tpm/dms_diff.c",
    "src/tpm/dms_sum.c",
    "src/tpm/eccentricity.c",
    "src/tpm/ecl2equ.c",
    "src/tpm/ellab.c",
    "src/tpm/equ2ecl.c",
    "src/tpm/equ2gal.c",
    "src/tpm/eterms.c",
    "src/tpm/evp.c",
    "src/tpm/fk425.c",
    "src/tpm/fk524.c",
    "src/tpm/fmt_alpha.c",
    "src/tpm/fmt_d.c",
    "src/tpm/fmt_delta.c",
    "src/tpm/fmt_h.c",
    "src/tpm/fmt_j.c",
    "src/tpm/fmt_rdb.c",
    "src/tpm/fmt_ymd.c",
    "src/tpm/fmt_ymd_raw.c",
    "src/tpm/gal2equ.c",
    "src/tpm/gcal2j.c",
    "src/tpm/geod2geoc.c",
    "src/tpm/h2h.c",
    "src/tpm/h2hms.c",
    "src/tpm/hadec2azel.c",
    "src/tpm/hms2dms.c",
    "src/tpm/hms2h.c",
    "src/tpm/hms2hms.c",
    "src/tpm/hms_diff.c",
    "src/tpm/hms_sum.c",
    "src/tpm/j2dow.c",
    "src/tpm/j2gcal.c",
    "src/tpm/j2jcal.c",
    "src/tpm/j2jd.c",
    "src/tpm/jcal2j.c",
    "src/tpm/jd2j.c",
    "src/tpm/jd2jd.c",
    "src/tpm/jd2ymd.c",
    "src/tpm/jd_diff.c",
    "src/tpm/jd_now.c",
    "src/tpm/jd_sum.c",
    "src/tpm/ldeflect.c",
    "src/tpm/m3I.c",
    "src/tpm/m3O.c",
    "src/tpm/m3Rx.c",
    "src/tpm/m3RxDot.c",
    "src/tpm/m3Ry.c",
    "src/tpm/m3RyDot.c",
    "src/tpm/m3Rz.c",
    "src/tpm/m3RzDot.c",
    "src/tpm/m3diff.c",
    "src/tpm/m3fmt.c",
    "src/tpm/m3inv.c",
    "src/tpm/m3m3.c",
    "src/tpm/m3scale.c",
    "src/tpm/m3sum.c",
    "src/tpm/m3v3.c",
    "src/tpm/m3v6.c",
    "src/tpm/m6I.c",
    "src/tpm/m6O.c",
    "src/tpm/m6Qx.c",
    "src/tpm/m6Qy.c",
    "src/tpm/m6Qz.c",
    "src/tpm/m6diff.c",
    "src/tpm/m6fmt.c",
    "src/tpm/m6inv.c",
    "src/tpm/m6m6.c",
    "src/tpm/m6scale.c",
    "src/tpm/m6sum.c",
    "src/tpm/m6v3.c",
    "src/tpm/m6v6.c",
    "src/tpm/nutations.c",
    "src/tpm/obliquity.c",
    "src/tpm/polint.c",
    "src/tpm/precess.c",
    "src/tpm/precess_m.c",
    "src/tpm/proper_motion.c",
    "src/tpm/qromb.c",
    "src/tpm/r2r.c",
    "src/tpm/rdb2ymd.c",
    "src/tpm/refco.c",
    "src/tpm/refract.c",
    "src/tpm/refraction.c",
    "src/tpm/solar_perigee.c",
    "src/tpm/tdt2tdb.c",
    "src/tpm/theta.c",
    "src/tpm/tpm.c",
    "src/tpm/tpm_data.c",
    "src/tpm/tpm_main.c",
    "src/tpm/tpm_state.c",
    "src/tpm/trapzd.c",
    "src/tpm/ut12gmst.c",
    "src/tpm/utc_now.c",
    "src/tpm/v32v6.c",
    "src/tpm/v3alpha.c",
    "src/tpm/v3c2s.c",
    "src/tpm/v3cross.c",
    "src/tpm/v3delta.c",
    "src/tpm/v3diff.c",
    "src/tpm/v3dot.c",
    "src/tpm/v3fmt.c",
    "src/tpm/v3init.c",
    "src/tpm/v3mod.c",
    "src/tpm/v3s2c.c",
    "src/tpm/v3scale.c",
    "src/tpm/v3sum.c",
    "src/tpm/v3unit.c",
    "src/tpm/v62v3.c",
    "src/tpm/v6alpha.c",
    "src/tpm/v6c2s.c",
    "src/tpm/v6cross.c",
    "src/tpm/v6delta.c",
    "src/tpm/v6diff.c",
    "src/tpm/v6dot.c",
    "src/tpm/v6fmt.c",
    "src/tpm/v6init.c",
    "src/tpm/v6mod.c",
    "src/tpm/v6s2c.c",
    "src/tpm/v6scale.c",
    "src/tpm/v6sum.c",
    "src/tpm/v6unit.c",
    "src/tpm/y2doy.c",
    "src/tpm/y2ymd.c",
    "src/tpm/ydd2ymd.c",
    "src/tpm/ymd2dd.c",
    "src/tpm/ymd2jd.c",
    "src/tpm/ymd2rdb.c",
    "src/tpm/ymd2y.c",
    "src/tpm/ymd2ymd.c",
    "src/tpm/zee.c",
    "src/tpm/zeta.c",

]

src_src = [ 
    'src/blackbox.c',

]

setupargs = {
    'version' :         '0.37',
    'description' :     'Astronomical coordinates & angular separations (OO)',
    'long_description' : "This is not a real package.  It just shows an example of how to get all kinds of files installed.",
    'author' :          'Vicki Laidler',
    'author_email' :    'help@stsci.edu',
    'url' :             'http://www.astrolib.org',
    # 'scripts' :         [ 'lib/sample_package' ],
    'license' :         'BSD',
    'platforms' :       ["Linux","Solaris","Mac OS X" ],

    # what directory each python package comes from:
    'package_dir' :     {
                        # This causes the main package to be installed, but only the .py files
                        'astrolib' : 'lib/astrolib',
                        'astrolib.coords' : 'lib/astrolib/coords',
                        'astrolib.coords.tests' : 'lib/astrolib/coords/tests',

                        },

    # how to install your data files:
    #   [
    #       ( directory_name_files_go_to, [ file_name_in_source_tree, another_data_file, etc ] )
    #   ]
    'data_files' :      [
                        # data files in the installed package directory
                        ( 'astrolib/coords',  [ 'LICENSE.txt','src/tpm/TPM_LICENSE.txt' ] ),
                        ],

    # extension modules written in C:
    #
    'ext_modules' :     [
                        distutils.extension.Extension( 'astrolib.coords._pytpm',
                            tpm_src + src_src
                            ),
                        ]

}


