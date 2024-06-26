/* Coding challenge:
** Input: "regex input"
** Output: input respect the regex or not
**
** Regex has the following symbols:
**  + - represents one character
**  * - need to have the same character in the three positions
**  *{N} - need to have the same character in the N positions
*/ 

//Code
function Wildcards(str) { 
  const [regex, input] = str.split(' ')
  let idx = 0;
  
  
  for( let i = 0; i < regex.length; i++){
    const current = regex[i];
    const next = regex[ i + 1];

    if( current == '*' && next == '{'){
      const rep = parseInt(regex[i+2], 10)

      for(let j = 0; j < rep-1; j++){
        if(input[idx+j] != input[idx + 1]){
          return false;
        }
      }
      idx = idx + rep;
      i = i + 3
    } else if(current == '*'){
      if(input[idx] == input[idx+1] && input[idx+1] == input[idx+2]){
        idx +=3
      } else {
        return false
      }
    } else if( current == '+') {
      idx++;
    } else if( current == '$') {
        const regex = new RegExp(`^[1-9]$`);
        const match = regex.test(input[idx]);
        if(match){
          idx++;
        } else {
          return false
        }
    }
  }
  return idx === input.length
}
   
// keep this function call here 
console.log(Wildcards(readline()));

// Sample
Wildcards("++++* abcdmmmmmm")
Wildcards("**+*{2} mmmrrrkbb")
Wildcards("$**+*{2} 9mmmrrrkbb")
Wildcards("$ 9")