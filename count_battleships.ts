function countBattleships(board: string[][]): number {
  let count = 0;

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] === 'X') {
        // Check if this 'X' is the start of a new ship
        if ((i === 0 || board[i - 1][j] === '.') && (j === 0 || board[i][j - 1] === '.')) {
          count++;
        }
      }
    }
  }

  return count;
}

const res1 = countBattleships([
  ['X', '.', '.', 'X'],
  ['.', '.', '.', 'X'],
  ['.', '.', '.', 'X'],
]);
console.log('[1] EXPECTED: 2');
console.log('[1] ACTUAL:  ', res1);
console.log('----');

const res2 = countBattleships([
  ['X', 'X', '.', 'X'],
  ['.', '.', '.', '.'],
  ['.', 'X', 'X', 'X'],
]);
console.log('[2] EXPECTED: 3');
console.log('[2] ACTUAL:  ', res2);
console.log('----');

const res3 = countBattleships([
  ['X', 'X', '.', 'X'],
  ['.', '.', '.', 'X'],
  ['.', '.', '.', '.'],
  ['.', 'X', 'X', '.'],
  ['.', '.', '.', 'X'],
]);
console.log('[3] EXPECTED: 4');
console.log('[3] ACTUAL:  ', res3);
console.log('----');

const res4 = countBattleships([
  ['X', 'X', '.', 'X', 'X', 'X'],
  ['.', '.', 'X', '.', '.', '.'],
  ['X', '.', '.', '.', '.', 'X'],
  ['X', '.', 'X', 'X', '.', 'X'],
  ['X', '.', '.', '.', '.', 'X'],
]);
console.log('[4] EXPECTED: 6');
console.log('[4] ACTUAL:  ', res4);
