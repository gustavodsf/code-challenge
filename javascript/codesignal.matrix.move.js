/* Coding challenge:
** Input: Matrix 
** Output: Matrix with all cells moved as much as possible
**
** Cell Symbols:
**  F - represents a filled cell
**  # - represents a obstacle should not be moved
**  - - empty cell
**
** Our work is to move as much as possible the F cell until reach an obstacle 
** or the bottom of the matrix.
*/  

const matrix = [
  ['F','F','F'],
  ['-','F','-'],
  ['-','F','-'],
  ['#','F','F'],
  ['-','F','-'],
  ['F','F','-'],
  ['-','-','-'],
  ['-','-','#'],
  ['-','-','-'],
  ['-','-','-'],
]

const findAllIndex = (array, row=0, item = '#') => {
  const positions = []; 
  let idx = array.indexOf(item);
  while(idx !== -1){
    positions.push([row, idx]);
    idx = array.indexOf(item, idx+1)
  } 
  return positions;
}

const obstacleIndex = []
const cellIndex = []

for(let i=0; i< matrix.length; i++){
  obstacleIndex.push(...findAllIndex(matrix[i],i))
  cellIndex.push(...findAllIndex(matrix[i],i, 'F'))
}

let lowestDistance = 9999;

// add ground to avoid moving beyond it
for(obstaclePosition of [...obstacleIndex, [matrix.length, 0], [matrix.length, 1], [matrix.length, 2]] ){
  for(cellPosition of cellIndex ){
    const [obsRow, obsCol] = obstaclePosition;
    const [celRow, celCol] = cellPosition;
    if(obsCol == celCol && celRow < obsRow) {
        const diff = obsRow - celRow - 1
        lowestDistance = (diff < lowestDistance ? diff : lowestDistance);
    }
  }
}

const newMatrix = new Array(matrix.length);
for (let i = 0; i < newMatrix.length; i++) {
  newMatrix[i] = new Array(3).fill('-');
}

for(obstaclePosition of obstacleIndex ){
  const [obsRow, obsCol] = obstaclePosition;
   newMatrix[obsRow][obsCol]='#'
}

for(cellPosition of cellIndex ){
  const [celRow, celCol] = cellPosition;
   newMatrix[celRow + lowestDistance][celCol]='F'
}

console.log(newMatrix)
