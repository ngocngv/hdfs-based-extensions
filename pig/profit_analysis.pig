
/* Script to Process Profit Analysis */

-- Extract Source Profit Data
in_profit = LOAD '/pig_analytics/Profit_Q1.txt' USING PigStorage('|') AS (country:chararray, date:chararray, profit:float, currency:chararray);

-- Filter Header & country not Australia
profit = FILTER in_profit BY (country != 'Country') AND (country != 'AUSTRALIA');

-- Extract Currency Exchange Data
in_xrate = LOAD '/pig_analytics/Exchange_Rate.csv' USING PigStorage(',') AS (exc_date:chararray, from_cur:chararray, to_cur:chararray, rate:float);

-- Filter Header
xrate = FILTER in_xrate BY (exc_date != 'Exc_Date');

-- Join dataset based on date & source currency
profit_xrate = JOIN profit BY (date, currency) LEFT OUTER, xrate BY (exc_date, from_cur);

-- Calculate conversion amount
profit_rate = FOREACH profit_xrate GENERATE $0 AS country, $3 AS curr, $1 AS date, $2 AS profit_base, $2 * ($7 IS NULL ? 1: $7) AS profit_usd, ToString(CurrentTime(),'yyyy-MM-dd') AS load_date;

-- Load final detail data into HDFS
STORE profit_rate INTO '/pig_analytics/out_profit_Q1_dtl' USING PigStorage (',');

-- Group dataset by Country
profit_by_country = GROUP profit_rate BY country;

-- Perform Aggregate operations based on Groups
profit_country = FOREACH profit_by_country GENERATE group as country, MIN(profit_rate.date) AS st_date, MAX(profit_rate.date) AS end_date, SUM(profit_rate.profit_usd) AS total_profit, AVG(profit_rate.profit_usd) AS avg_profit, ToString(CurrentTime(),'yyyy-MM-dd') AS load_date;

-- Load final summary data into HDFS
STORE profit_country INTO '/pig_analytics/out_profit_Q1' USING PigStorage (',');
