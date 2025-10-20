function BracketMatcher(str) {
  // __define-ocg__: Validate matching parentheses using a simple counter
  let varOcg = 0;            // running balance of '(' minus ')'
  let varFiltersCg = false;  // track if we encountered any bracket at all

  for (let ch of str) {
    if (ch === '(') {
      varOcg++;
      varFiltersCg = true;
    } else if (ch === ')') {
      varOcg--;
      varFiltersCg = true;
      if (varOcg < 0) {
        return 0; // more closing than opening at some point
      }
    }
  }

  // If balance is zero, brackets matched. If none were found, also return 1.
  return varOcg === 0 ? 1 : 0;
}
   
// keep this function call here 
console.log(BracketMatcher(readline()));