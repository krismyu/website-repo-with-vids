Title: Installing octave
Date: 2013-07-27 07:41
status: draft
Tags: octave, foss
Slug: installing-octave
Summary: 

Mountain Lion

http://wiki.octave.org/Octave_for_MacOS_X


brew tap homebrew/science

amoebe@moebius :: brew tap homebrew/science
Cloning into '/usr/local/Library/Taps/homebrew-science'...
remote: Counting objects: 2223, done.
remote: Compressing objects: 100% (1295/1295), done.
remote: Total 2223 (delta 1089), reused 1975 (delta 909)
Receiving objects: 100% (2223/2223), 459.37 KiB, done.
Resolving deltas: 100% (1089/1089), done.
Tapped 152 formula

amoebe@moebius :: brew update && brew upgrade
Already up-to-date.

amoebe@moebius :: brew install gfortran
==> Installing gfortran dependency: gmp
==> Downloading ftp://ftp.gmplib.org/pub/gmp-5.1.2/gmp-5.1.2.tar.bz2
######################################################################## 100.0%
######################################################################## 100.0%==> ./configure --prefix=/usr/local/Cellar/gmp/5.1.2 --enable-cxx
==> make
==> make check
==> make install
🍺  /usr/local/Cellar/gmp/5.1.2: 12 files, 2.5M, built in 4.6 minutes
==> Installing gfortran dependency: mpfr
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/mpfr-3.1.2.mountain_lion.bottle.tar.gz
######################################################################## 100.0%
==> Pouring mpfr-3.1.2.mountain_lion.bottle.tar.gz
🍺  /usr/local/Cellar/mpfr/3.1.2: 23 files, 3.3M
==> Installing gfortran dependency: libmpc
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/libmpc-1.0.1.mountain_lion.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libmpc-1.0.1.mountain_lion.bottle.tar.gz
🍺  /usr/local/Cellar/libmpc/1.0.1: 9 files, 292K
==> Installing gfortran dependency: isl
==> Downloading ftp://ftp.linux.student.kuleuven.be/pub/people/skimo/isl/isl-0.11.2.tar.bz2
######################################################################## 100.0%
######################################################################## 100.0%==> ./configure --prefix=/usr/local/Cellar/isl/0.11.2
==> make install
🍺  /usr/local/Cellar/isl/0.11.2: 52 files, 3.0M, built in 41 seconds
==> Installing gfortran dependency: cloog
==> Downloading http://www.bastoul.net/cloog/pages/download/count.php3?url=./cloog-0.18.0.tar.gz
######################################################################## 100.0%
==> ./configure --prefix=/usr/local/Cellar/cloog/0.18.0 --with-isl-prefix=/usr/local/opt/isl
==> make install
🍺  /usr/local/Cellar/cloog/0.18.0: 31 files, 532K, built in 3.6 minutes
==> Installing gfortran
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/gfortran-4.8.1.mountain_lion.bottle.tar.gz
######################################################################## 100.0%
==> Pouring gfortran-4.8.1.mountain_lion.bottle.tar.gz
==> Caveats
Brews that require a Fortran compiler should use:
  depends_on :fortran
==> Summary
🍺  /usr/local/Cellar/gfortran/4.8.1: 1025 files, 119M


amoebe@moebius :: brew install octave
octave: Unsatisfied dependency: XQuartz 
Homebrew does not package XQuartz. Installers may be found at:
  https://xquartz.macosforge.org
Error: An unsatisfied requirement failed this build.

[discussed on github](https://github.com/mxcl/homebrew/issues/14851)

https://xquartz.macosforge.org

![xquartz download](xquartz.png)


    brew install octave




