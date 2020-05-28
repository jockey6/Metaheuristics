#  crp_sa.py
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
import sys

from combinatorial.crp.crp import Crp
from combinatorial.crp.crp_solution import CrpSolution
from combinatorial.simulated_annealing import SimulatedAnnealing
from run_tests import run_and_print
from stopping.time_limit import TimeLimit

if __name__ == "__main__":
  instance = Crp.read(sys.argv[1][2:])
  # instance = Crp.read('instances/crp/Fischetti2017/wf05_cb05_capex.crp')

  tests = 20
  cpus = 7

  sa = SimulatedAnnealing.build(10, 1, .9999, TimeLimit(2 * 60 * 60))
  run_and_print(instance, sa, CrpSolution, tests, cpus)
