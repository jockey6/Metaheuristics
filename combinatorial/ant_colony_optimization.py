#  ant_colony_optimization.py
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

from copy import copy
from typing import List

from combinatorial.ant import Ant
from combinatorial.metaheuristic import MetaheuristicPopulationBased


# TODO: document this file when it's done
class AntColonyOptimization(MetaheuristicPopulationBased):
  """
  Ant Colony Optimization implementation.
  """

  @staticmethod
  def build(iterations, pheromone, alpha, beta, rho):
    return AntColonyOptimization((alpha, beta, rho, iterations, pheromone))

  @staticmethod
  def default_pheromone(n):
    return [[0.5] * n] * n

  def __init__(self, args):
    # TODO: change args to **kwargs
    # TODO: add validation
    self.__alpha = args[0]
    self.__beta = args[1]
    self.__rho = args[2]
    self.__iterations = args[3]
    self.__pheromone = args[4]

  def _update_pheromone(self, population):
    n = len(self.__pheromone)
    delta = [[0] * n] * n
    for x in population:
      for i in range(n):
        delta[x.tour[i - 1]][x.tour[i]] += 1.0 / x.get_fitness()
    for i in range(n):
      for j in range(n):
        self.__pheromone[i][j] = (1 - self.__rho) * self.__pheromone[i][j] + self.__rho * delta[i][j]

  def execute(self, population: List[Ant]):
    instance = population[0].get_instance()
    n = instance.get_n()

    # TODO: raise this value to the power of beta instead of calculating inside ant, which may improve speed
    quality = [[1.0 / instance.cost(u, v) if instance.cost(u, v) != 0 else 0 for v in range(n)] for u in range(n)]

    population.sort(key=lambda x: x.get_fitness())
    best = population[0]
    for iteration in range(self.__iterations):
      for ant in population:
        ant.travel(self.__alpha, self.__beta, self.__pheromone, quality)

      population.sort(key=lambda x: x.get_fitness())
      if population[0].get_fitness() < best.get_fitness():
        best = copy(population[0])

      self._update_pheromone(population)

    return best