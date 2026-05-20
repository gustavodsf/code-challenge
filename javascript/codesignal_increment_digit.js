  /*
You are given an array of integers digits representing the digits of a positive integer. For example, digits = [1, 2, 3] represents the integer 123.
It is guaranteed that digits does not have any leading zeros.
Assuming that digits represents the integer n, your task is to return an array that represents the integer n + 1.
Example
For digits = [1, 2, 3], the output should be solution(digits) = [1, 2, 4];
For digits = [1, 2, 9], the output should be solution(digits) = [1, 3, 0];
For digits = [9, 9, 9], the output should be solution(digits) = [1, 0, 0, 0].
Input/Output
[execution time limit] 4 seconds (js)
[memory limit] 1 GB
[input] array.integer digitsAn array with integer digits from 0 to 9.Guaranteed constraints:1 ≤ digits.length ≤ 104,0 ≤ digits[i] ≤ 9.
[output] array.integerReturn an array that represents the digits of n + 1.
*/
// Prints help message to the console
// Returns a string
function solution(digits) {
  let sunOfAllValues = digits.reduce((acc, cur) => acc+cur ,0);
  let valueIfAllValuesAreNine = digits.length * 9

  if(sunOfAllValues == valueIfAllValuesAreNine){
      digits = [0, ...digits]
  }
  
  for(let idx = digits.length-1; idx >= 0; idx-- ){
     if(digits[idx] < 9){
       digits[idx] = digits[idx] + 1;
       return digits
     } else {
       digits[idx] = 0;
     }
  }
}
