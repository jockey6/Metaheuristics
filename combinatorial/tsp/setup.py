#  setup.py
#
#  Copyright (c) 2020 Bruno Almêda de Oliveira <abrunoaa@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <https://www.gnu.org/licenses/>.
#
from distutils.core import setup, Extension


"""
This file compiles tsp_optimal.cpp into a python library. Don't forget to cythonize before compiling the library.

The library compilation was separated from cythonize to allow compilation from distinct python interpreters. 
"""

module = Extension('tsp_optimal',
                   sources = ['tsp_optimal.cpp'])

setup(name = 'tsp_optimal',
      version = '1.0',
      ext_modules = [module])