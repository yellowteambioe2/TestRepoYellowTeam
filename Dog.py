#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class definition Dog

By: Steve Lammers, Steven.Lammers@UCDenver.edu
"""

# Imports
#import numpy as np
#import matplotlib

class Dog():
  """
  Class Description

  Args:
    _color: string - dog color
    _name:  string - name of dog
  """
  def __init__(self, color, name):
    self._color=color
    self._name=name

  def bark(self):
    """
    Make dog bark
    """
    print('Woof')

  def eat(self,food):
    """
    Make dog eat
    """
    if food == 'treat':
      self.bark()
    elif food == 'dog food':
      print 'Dog unimpressed'
    elif food == 'bully stick':
      self.bark()
      self.bark()
      self.bark()
      self.bark()
    else:
      print 'Dog sits and stares'

# Top-Level script environment, runs if main file is called as top level
# i.e. runs if the file is called from terminal using python Dog.py
if __name__ == "__main__":
  test_dog = Dog('yellow','buddy')
  #test_dog.bark()
  test_dog.eat(1)
