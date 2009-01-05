from distutils.core import setup, Extension
import sys, os.path, string, shutil, glob, os, re
from distutils.command.install_data import install_data



ver = sys.version_info
python_exec = 'python' + str(ver[0]) + '.' + str(ver[1])


def dolocal():
    """Adds a command line option --local=<install-dir> which is an abbreviation for
    'put all of thispackage in <install-dir>/thispackage'."""
    if "--help" in sys.argv:
        print >>sys.stderr
        print >>sys.stderr, " options:"
        print >>sys.stderr, "--local=<install-dir>    same as --install-lib=<install-dir>"
    for a in sys.argv:
        if a.startswith("--local="):
            dir =  os.path.abspath(a.split("=")[1])
            sys.argv.extend([
                "--install-lib="+dir,
                "--install-data="+os.path.join(dir,"coords")
                ])
            sys.argv.remove(a)

class smart_install_data(install_data):
    def run(self):
        install_cmd = self.get_finalized_command('install')
        self.install_dir = getattr(install_cmd, 'install_lib')
        return install_data.run(self)


tpmsrc = glob.glob('src/tpm/*.c')
tpmsrc.extend(['src/blackbox.c','src/pytpm_wrap.c'])

        
def dosetup():
    r = setup(name = "coords",
              version = "0.37",
              description  = 'Astronomical coordinates & angular separations (OO)',
              fullname     = 'AstroLib Coords',
              license      = 'BSD',
              author = "Vicki Laidler",
              author_email = "help@stsci.edu",
              url = "http://projects.scipy.org/astropy/astrolib",
              platforms = ["Linux","Solaris","Mac OS X"],
              packages=['coords'],
              package_dir={'coords':'lib'},
              cmdclass = {'install_data':smart_install_data},
	      data_files = [('coords',['lib/LICENSE.txt','src/tpm/TPM_LICENSE.txt'])],
              ext_modules = [Extension('coords._pytpmmodule', tpmsrc,
                                      include_dirs = ['src/tpm'],
                                       )],
              )

    return r

def main():
    args = sys.argv
    for a in args:
        if a.startswith('sdist'):
            try:
                #put a path to swig here or bear the consequences
                if os.system('/data/gaudete1/laidler/ssb/coord/swigstuff/swig-1.3.25/swig  -python -outdir lib src/pytpm.i') == 0:
                    continue
                else:
                    s=os.popen3('swig -version', 'r')[2].read()
                    if "command not found" in s:
                        print "SWIG not  found\n"
                        raise SystemExit, "SWIG not  found\n"
                    else:
                        p=re.compile('Version', re.IGNORECASE)
                        swig_version = re.split(p, s)[1].split()[0]
                        if swig_version < '1.3':
                            print "SWIG v 1.3 or later needed"
                            raise SystemExit, "SWIG v 1.3 or later needed"
                        else:
                            os.system('swig  -python -outdir lib src/pytpm.i')
            except:
                raise SystemExit, "Incomplete source distribution - swig files were not generated, see messages above.\n"

    dolocal()
    dosetup()


if __name__ == "__main__":
    main()

