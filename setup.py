#!/usr/bin/env python

#
#    copyright 2008 Angus Ainslie
#
#    BtConfigure.py is free software: you can redistribute it and/or modify it
#    under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    BtConfigure.py is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this file.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os

from distutils.core import setup
from distutils.extension import Extension
from glob import glob
import commands

from distutils.command.build import build as _build
from distutils.command.clean import clean as _clean

class my_clean(_clean):
    def run(self):
        _clean.run(self)

setup(name='bt-configure',
      version='0.1',
      description="bluez4 device scanner and pairing",
      author="Angus Ainslie",
      author_email='angus@akkea.ca',
#      package_dir = {''},
#      packages = ['bt-configure', ''],
      scripts= ['BtConfigure.py'],
      # XXX: Those locations may not work on the neo !
      data_files = [('applications',
                     ['bt-configure.desktop']),
                    ('icons', ['bt-configure.png']),
                    ('bt-configure', ['BluetoothClasses.py'])],

      cmdclass = {'clean': my_clean},
      
      )


