from typing import List

```
  X -> position of frogs
  Y -> position of flies
  S -> tongue length of frogs

  Solution: X - Y <= S

  X and S are equal, Y has not the same size
```
def frogs (X:List[int],S:List[int],Y:List[int]) -> List[int]:
  result = []
  for frog,tongue in zip(X,S):
    counter=0
    for fly in Y:
      if fly <= frog + tongue:
        counter+=1
    result.append(counter)
  return result