#  stopping_condition.py
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
from abc import ABC, abstractmethod


class StoppingCondition(ABC):
  """
  Abstract class to represent a stop criteria and define what it must have.
  """

  def __bool__(self):
    return self.finished()

  @abstractmethod
  def start(self) -> None:
    """
    Start this criteria.

    :return: None.
    """
    pass

  @abstractmethod
  def finished(self) -> bool:
    """
    Check if the stopping criteria was reached.

    :return: True if stopping criteria was reached. False otherwise.
    """
    pass

  @abstractmethod
  def update(self, improved: bool) -> None:
    """
    Update the state of current criteria.

    :param improved: True if the solution improved on current iteration. False otherwise.
    :return: None.
    """
    pass

  @abstractmethod
  def timing(self) -> float:
    """
    Calculates a factor that indicates how close the algorithm is to ending in range [0, 1].

    0 means the algorithm just started, while 1 means the algorithm is finished.

    :return: The factor of how close is to ending.
    """
    pass
