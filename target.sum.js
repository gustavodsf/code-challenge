//   Write a function that takes in a non-empty array of distinct integers and an
//   integer representing a target sum. If any two numbers in the input array sum
//   up to the target sum, the function should return them in an array, in any
//   order. If no two numbers sum up to the target sum, the function should return
//   an empty array.
//   Note that the target sum has to be obtained by summing two different integers
//   in the array; you can't add a single integer to itself in orde

//Naive
function twoNumberSum(array, targetSum) {
    sums = [];
    for(let i = 0; i < array.length ; i++){
        for( let j = i + 1; j < array.length; j++){
            if(array[i] + array[j] === targetSum){
                sums.push([array[i], array[j]])
            }
        }
    }
    return sums
}


//faster solution
function twoNumberSum(array, targetSum) {
    const sums = [];
    const hashTable = {}
  
    for(let i = 0; i < array.length ; i++){
       const sumMinusElement = targetSum - array[i];
       if( hashTable[sumMinusElement.toString()] !== undefined ) {
         sums.push([array[i], sumMinusElement])
       }
      
      hashTable[array[i].toString()] = array[i]
      
    }
    return sums
}

function twoNumberSum(array, targetSum) {
    const sorted = array.sort((a,b) => a - b)
    let left = 0
    let right = sorted.length - 1
    console.log(sorted)
    
    while(left < right){
      const currentSum = sorted[left] + sorted[right]
      console.log([sorted[left] , sorted[right]])
      if(currentSum > targetSum){
        right = right - 1
      } else if(currentSum < targetSum){
        left = left + 1
      } else {
        return [
          sorted[left] , sorted[right]
        ]
      }
    }
      
    const sums = []
   
    return sums
  }

console.log(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10));
console.log(twoNumberSum([3, 5, 2, -4, 8, 11], 7));       