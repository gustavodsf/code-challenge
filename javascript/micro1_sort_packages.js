/*
Imagine you are a software engineer working for a logistics company. You have 
been tasked with optimizing the package sorting process in the warehouse. The 
warehouse uses a conveyor system that transports packages to different sorting 
stations based on their destination postal codes. Your challenge is to design an 
algorithm that efficiently sorts the packages and ensures they reach the correct 
sorting station. Given a queue of packages, each represented by its destination 
postal code, your algorithm should sort the packages based on their postal codes 
and send them to the corresponding sorting stations. The sorting stations are 
represented by an array, where each element represents the range of postal codes 
handled by that station. Implement a function called 'sortPackages' that takes 
two parameters: 1. 'packages': A queue of integers representing the destination 
postal codes of the packages. 2. 'sortingStations': An array of pairs, where each 
pair represents the range of postal codes handled by a sorting station. The first 
element of the pair is the lower bound (inclusive), and the second element is the 
upper bound (inclusive). Your function should return an array of integers, where 
each element represents the number of packages sent to each sorting station in 
the order they appear in the 'sortingStations' array.

EXAMPLE 1
Input:packages = [3, 8, 2, 5, 9, 1, 7, 4, 6]
sortingStations = [[1, 3], [4, 6], [7, 9]]

Output:[3, 3, 3]

Explanation:The packages with postal codes [1, 2, 3] are sent to the first sorting 
station, packages with postal codes [4, 5, 6] are sent to the second sorting station, 
and packages with postal codes [7, 8, 9] are sent to the third sorting station. 
Therefore, the output is [3, 3, 3], indicating the number of packages sent to each sorting station.

EXAMPLE 2
Input:packages = [10, 5, 7, 8, 2, 6, 9, 1, 4, 3]
sortingStations = [[1, 4], [5, 8], [9, 10]]

Output:[4, 4, 2]

Explanation:The packages with postal codes [1, 2, 3, 4] are sent to the first sorting 
station, packages with postal codes [5, 6, 7, 8] are sent to the second sorting 
station, and packages with postal codes [9, 10] are sent to the third sorting 
station. Therefore, the output is [4, 4, 2], indicating the number of packages sent to each sorting station.
*/

const sortPackages = (packages, sortingStations) => {
  const response = Array(sortingStations.length).fill(0)
  packages.forEach(pkg => {
     for(let idx=0; idx < sortingStations.length; idx++){
          const [ lower, higher ] = sortingStations[idx];
          if(pkg >= lower && pkg <= higher){
              response[idx] = response[idx] + 1;
          }
     }
  })
  return response
}

console.log(sortPackages(
  [3, 8, 2, 5, 9, 1, 7, 4, 6],
  [[1, 3], [4, 6], [7, 9]]
))

console.log(sortPackages(
  [10, 5, 7, 8, 2, 6, 9, 1, 4, 3],
  [[1, 4], [5, 8], [9, 10]]
))
