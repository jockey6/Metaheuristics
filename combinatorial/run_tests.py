#  run_tests.py
#
#  Copyright (c) 2020 Bruno Almeda de Oliveira <abrunoaa@gmail.com>
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

from combinatorial.cvrp.cvrp import Cvrp

from time import process_time as time


# import logging
# logging.getLogger().setLevel(logging.DEBUG)

def run(filename, tests, function):
  cvrp = Cvrp.read(filename)
  total_elapsed = 0
  avg_answer = 0
  best, worst = float("inf"), 0
  print("elapsed;result;tour")

  for test in range(tests):
    start = time()
    ans = function(cvrp)
    end = time()
    elapsed = end - start

    tour = ans.get_tour()
    for i in range(len(tour)):
      if tour[i][-1] < tour[i][0]:
        tour[i] = tour[i][::-1]
    tour = sorted(tour)
    print("{:.3f}s;{};{}".format(elapsed, ans.get_fitness(), tour))

    total_elapsed += elapsed
    avg_answer += ans.get_fitness()
    best = min(best, ans.get_fitness())
    worst = max(worst, ans.get_fitness())

  print("")
  print("avg_elapsed;avg_result;best_result;worst_result")
  print("{:.3f}s;{:.3f};{};{}".format(total_elapsed / tests, avg_answer / tests, best, worst))
