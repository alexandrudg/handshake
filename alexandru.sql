-- My First understanding (Aggregating births for my city, month, year)
SELECT COUNT(*),
  FROM_UNIXTIME(DATE, '%c') as MONTH,
  FROM_UNIXTIME(DATE, '%Y') as YEAR,
  CITY
FROM birth_report
WHERE month(FROM_UNIXTIME(DATE)) = 7 AND CITY = "Piatra Neamt"
GROUP BY MONTH, YEAR

