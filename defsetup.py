from __future__ import division # confidence high

import distutils.extension

import glob

# list of all the packages to be installed
pkg = [ 'coords' ]

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
                        'coords' : 'lib', 

                        },

    # how to install your data files:
    #   [
    #       ( directory_name_files_go_to, [ file_name_in_source_tree, another_data_file, etc ] )
    #   ]
    'data_files' :      [ 
                        # data files in the installed package directory
                        ( 'coords',  [ 'lib/LICENSE.txt','src/tpm/TPM_LICENSE.txt' ] ),
                        ],

    # extension modules written in C:
    #
    'ext_modules' :     [ 
                        distutils.extension.Extension( 'coords._pytpmmodule', 
                            glob.glob('src/tpm/*.c') + [ 'src/blackbox.c','src/pytpm_wrap.c' ],
                            include_dirs= [ 'src/tpm' ] ),
                        ]

}


