#!/usr/bin/ python
# -*- coding: utf-8 -*-

from datetime import datetime

class Driver():
  TIME_FMT = "%H:%M"

  def __init__(self, name, **kwargs):
    self.name = name
    self.trips = kwargs.get('trips', 0)
    self.miles = kwargs.get('miles', 0)
    self.hours = kwargs.get('hours', 0)
    self.omitted = ""

  def drive(self, start, end, dist):
    t_start = datetime.strptime(start, self.TIME_FMT)
    t_end = datetime.strptime(end, self.TIME_FMT)
    t_dist = float(dist)
    dt = (t_end-t_start).seconds/3600.0
    avg = t_dist/dt
    if avg > 5 and avg < 100:
      self.trips += 1
      self.miles += t_dist
      self.hours += dt
    else:
      self.omitted += " ".join([self.name, start, end, str(dist)])

  def avg_mph(self):
    return self.miles/self.hours if self.hours > 0 else 0

  def __str__(self):
    if self.trips > 0:
      miles = self.miles
      hours = self.hours
      return "{0}: {1:.0f} miles @ {2:.0f} mph\n"\
        .format(self.name, self.miles, self.avg_mph())
    else:
      return "{0}: {1:.0f} miles\n"\
        .format(self.name, self.miles)
