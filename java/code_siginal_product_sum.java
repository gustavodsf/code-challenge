int solution(int n) {
    int product = 1;
    int totalSum = 0;
    
    String numberStr = Integer.toString(n);
    
    for(char digitChar : numberStr.toCharArray()) {
        int digit = Character.getNumericValue(digitChar);
        product *= digit;
        totalSum += digit;
    }
    
    return product - totalSum;
}
