def solution(buckets):
    n = len(buckets)
    num_balls = buckets.count('B')
    
    # If no balls or one ball, no swaps needed
    if num_balls <= 1:
        return 0
    
    # Check if alternating pattern is possible
    max_balls = (n + 1) // 2
    
    # Only return -1 if we have too many balls for any alternating pattern
    if num_balls > max_balls:
        return -1
    
    # Count balls at even and odd positions
    balls_at_even = 0
    balls_at_odd = 0
    
    for i in range(n):
        if buckets[i] == 'B':
            if i % 2 == 0:
                balls_at_even += 1
            else:
                balls_at_odd += 1
    
    # Strategy 1: Balls at even indices (0, 2, 4, ...) - pattern: B.B.B...
    available_even_slots = (n + 1) // 2
    if num_balls <= available_even_slots:
        misplaced_s1 = balls_at_odd  # These need to move to even positions
    else:
        misplaced_s1 = float('inf')
    
    # Strategy 2: Balls at odd indices (1, 3, 5, ...) - pattern: .B.B.B...
    available_odd_slots = n // 2
    if num_balls <= available_odd_slots:
        misplaced_s2 = balls_at_even  # These need to move to odd positions
    else:
        misplaced_s2 = float('inf')
    
    # Return minimum swaps needed
    result = min(misplaced_s1, misplaced_s2)
    
    if result == float('inf'):
        return -1
    
    return result