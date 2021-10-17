
def make_bricks(small, big, goal):
  """This function that takes the quantity of the bricks, size of the wall to be build, and determines if the wall can be build or not."""

  valueOfSmallBr = small*1
  valueOfBigBr = big*5
  valueOfGoal = valueOfSmallBr + valueOfBigBr
  
  if valueOfGoal < goal:
    return False
  elif valueOfSmallBr == goal or valueOfBigBr == goal or valueOfGoal == goal:
    return True
  else:
    smallBricksNeeded = goal % 5
    
    if small >= smallBricksNeeded:
      return True
    else:
      return False

print(make_bricks(3, 5, 200))
