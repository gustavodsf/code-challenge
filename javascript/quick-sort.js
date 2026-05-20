// Function to remove duplicates and perform QuickSort
function quickSort(unsortedArray) {
    // Remove duplicates
    let j = 0;
    for (let i = 0; i < unsortedArray.length; i++) {
        if (unsortedArray[i] !== unsortedArray[i + 1]) {
            unsortedArray[j] = unsortedArray[i];
			j = j + 1
        }
    }
    const uniqueArray = unsortedArray.slice(0, j);
    // Perform QuickSort
    sortArray(uniqueArray, 0, uniqueArray.length - 1);

    return uniqueArray;
}

// Custom implementation of QuickSort
function sortArray(arr, low, high) {
    if (low < high) {
        const pi = partition(arr, low, high);

        sortArray(arr, low, pi - 1);
        sortArray(arr, pi + 1, high);
    }
}

// Custom implementation of partitioning
function partition(arr, low, high) {
    const pivot = arr[high];
    let i = low - 1;

    for (let j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            // Swap arr[i] and arr[j]
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
    }

    // Swap arr[i+1] and arr[high]
    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];

    return i + 1;
}

// Read input values from stdin
quickSort([1,2,3,4])