#!/bin/sh
rm -fr bin develop-eggs eggs .installed.cfg parts bootstrap.py
#downloads url bootstrap.py :
# http://downloads.buildout.org/2.1/bootstrap.py
wget http://downloads.buildout.org/2.1/bootstrap.py
python2.7 bootstrap.py -v 2.1.1
./bin/buildout -Nv $@ 2>&1 | tee buildout.log
