// ())()
const isMissMatch = (brackets) => {
  const map = {
        '(': 0,
        ')': 0,
    }
    for( let i=0; i < brackets.length; i++){
       map[brackets[i]] = map[brackets[i]] + 1
    }
    return map['('] != map[')']
}

function minimumSwaps(brackets) {
   
    if(isMissMatch(brackets)){
      return -1
    }
   
    let newBrackets = brackets.replace(/\(\)/g, '');
    while(newBrackets != brackets){
      brackets = newBrackets;
      newBrackets = brackets.replace(/\(\)/g, '');
    }
    return newBrackets.length/2
}



minimumSwaps('((()))))((')
