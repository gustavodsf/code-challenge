def max_earnings( earnings_per_fight ) :
	num_fights = len(earnings_per_fight)
	if num_fights == 0:
		return 0
	if num_fights == 1:
		return earnings_per_fight[0]
	
	dp = [0] * num_fights
	dp[0] = earnings_per_fight[0]
	dp[1] = max(earnings_per_fight[0], earnings_per_fight[1])

	for i in range(2, num_fights):
		dp[i] = max(dp[i-1], dp[i-2] + earnings_per_fight[i])

	return dp[-1]