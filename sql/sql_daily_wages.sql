SELECT laborers.name, 
       SUM(TIMESTAMPDIFF(HOUR, daily_hours.entry_time, daily_hours.exit_time) * 30) + laborers.previous_balance AS total_amount_owed
FROM laborers
JOIN daily_hours ON laborers.id = daily_hours.labor_id
GROUP BY laborers.name, laborers.previous_balance
HAVING SUM(TIMESTAMPDIFF(HOUR, daily_hours.entry_time, daily_hours.exit_time) * 30) + laborers.previous_balance > 0
ORDER BY laborers.name;