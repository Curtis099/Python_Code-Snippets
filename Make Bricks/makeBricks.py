def make_bricks(small, big, goal):
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
