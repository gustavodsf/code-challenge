const binarySearch = (array, target) => {
  const middle = Math.floor(array.length/2)
  
  let lowerPointer = 0
  let highestPointer = middle
  
  if(array[middle] < target) {
     lowerPointer = middle
     highestPointer = array.length-1
  }
  
  for(let i = lowerPointer; i <= highestPointer; i++){
     if(array[lowerPointer] === target){
       return lowerPointer
     }
     if(array[highestPointer] === target){
       return highestPointer
     }
    lowerPointer++
    highestPointer--
  }
  
  return -1
 }
 
 binarySearch([1,2,3,4,5,6,7,8, 9], 7)
 