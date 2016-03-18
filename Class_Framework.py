#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Top-level docstring

Remaining docstring after empty line

By: Steve Lammers, Steven.Lammers@UCDenver.edu
"""

# Imports
#import numpy as np
#import matplotlib

class ClassName():
  """
  Class Description

  Args:
    var1: var_type - Description
  """
  def __init__(self, var1, var2):
    self._var1=var1
    self._var2=var2

  def method1(self):
    """
    Method for doing something

    Args:
      var1: var_type - Description

    Return:
      return_var: return_type - Description
    """
    return_var = 1 #Dummy code, replace
    print('var1: %0d'% self._var1)

    return return_var



# Top-Level script environment, runs if main file is called as top level
# i.e. runs if the file is called from terminal using python BMI_Calculator.py
if __name__ == "__main__":
  test_classname = ClassName(1,2)
  test_classname.method1()
