#  random_util.py
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
from collections import Generator
from random import random


def roulette(values, s=None):
  """
  Select one index from values.

  The probability to choose index k is proportional to values[k], i.e., values[k] / sum(values).

  :param values: List with values corresponding to the probability to choose index k.
  :param s: Sum of values. This may speed up the algorithm.
  :return: An integer in range [0, len(values)), the chosen index.
  """
  if s is None:
    if isinstance(values, Generator):
      values = list(values)
    s = sum(values)
  assert s > 0, "Sum of values must be > 0: {}".format(values)

  r = random()
  for i, x in enumerate(v / s for v in values):
    assert x >= 0, "Negative values aren't allowed: {} at index {}".format(x, i)
    r -= x
    if r < 0:
      return i
  return len(values) - 1
