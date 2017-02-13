

# Install PIG In Client Node of Hadoop Cluster

# https://dwbi.org/etl/bigdata/198-install-pig-in-client-node-of-hadoop-cluster




#------------------------------------------------------------------------------
# Data Preparation
#------------------------------------------------------------------------------

# Lets load this sample data first to local system and further put the files into HDFS.

cd ~

# Profit_Q1.txt
#----------------------------------------------------------
echo "Country|Date|Profit|Currency
INDIA|2016-01-31|4500000|INR
US|2016-01-31|9000000|USD
SINGAPORE|2016-01-31|7000000|SGD
AUSTRALIA|2016-01-31||AUD
INDIA|2016-02-29|4900000|INR
US|2016-02-29|8900000|USD
SINGAPORE|2016-02-29|7100000|SGD
AUSTRALIA|2016-02-29||AUD
INDIA|2016-03-31|5000000|INR
US|2016-03-31|9100000|USD
SINGAPORE|2016-03-31|7200000|SGD
AUSTRALIA|2016-03-31||AUD
INDIA|2016-04-30|4800000|INR
US|2016-04-30|8900000|USD
SINGAPORE|2016-04-30|7300000|SGD
AUSTRALIA|2016-04-30||AUD" >> Profit_Q1.txt



# Exchange_Rate.csv
#----------------------------------------------------------
echo "Exc_Date,From,To,Rate
2016-01-31,INR,USD,0.0147
2016-01-31,SGD,USD,0.702
2016-02-29,INR,USD,0.0146
2016-02-29,SGD,USD,0.711
2016-03-31,INR,USD,0.015
2016-03-31,SGD,USD,0.742
2016-04-30,INR,USD,0.015
2016-04-30,SGD,USD,0.7439" >> Exchange_Rate.csv




#
#----------------------------------------------------------
cd ~

hadoop fs -mkdir /pig_analytics
hadoop fs -copyFromLocal ~/Profit_Q1.txt /pig_analytics
hadoop fs -copyFromLocal ~/Exchange_Rate.csv /pig_analytics









#------------------------------------------------------------------------------
# Pig Latin Script
#------------------------------------------------------------------------------

# Pig Latin Script to process the data.

# edit ~/profit_analysis.pig
#------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------


















