Promise.resolve(
  setTimeout(()=> console.log('Hello World!'), 3000)
)

const number = [5,6,5,4,1,8,]

const bubbleSort = ( array ) => {
  for(let i = 0; i < array.length -1; i++ ){
    for( let j = i+1; j < array.length; j++ ){
       if( array[i] > array[j]  && i != j){
           const temp = array[i]
           array[i] = array[j]
           array[j] = temp
       } 
    }  
  }
  return array
}

bubbleSort(number)

const add = ( array, position, element ) => {
    const newArray = []
    for(let i = 0; i < array.length; i++){
        if(i == position - 1){
          newArray.push(element)
        }
        newArray.push(array[i])
    }
    return newArray;
}
add([ 1,2,3,4,5,6 ], 3, 7)
