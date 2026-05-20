
/*
 * Complete the 'dynamicArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

function dynamicArray(n: number, queries: number[][]): number[] {
    // Write your code here
    let lastAnswer = 0;
    let arr: Array<Array<number>> = [];
    
    for(let i = 0; i < n; i++){
        arr.push([])
    }
    
    const answer = Array<number>();
    
    const getIndex = (x: number) => (x ^ lastAnswer) % n
    
    const queryOne = (x:number, y: number) =>{
        const idx = getIndex(x);
        arr[idx].push(y)
    }
    
    const queryTwo = (x:number, y:number) =>{
        const idx = getIndex(x);
        const l = arr[idx].length;
        const z = y % l
        lastAnswer = arr[idx][z]
        answer.push(lastAnswer)
    }
    
    for ( const query of queries){
        if(query[0] === 1){
            queryOne(query[1], query[2])
        } else if(query[0] === 2){
            queryTwo(query[1], query[2])
        }
    }
    
    return answer;
    
}

