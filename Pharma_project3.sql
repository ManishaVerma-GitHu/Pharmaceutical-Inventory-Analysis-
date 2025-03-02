select * from project3_dataset;

#################### FIRST BUSINESS DECISION MOMENT ######################

select avg(`Qty in Un. of Entry`) as Inj1 from Project3_dataset;

select `Qty in Un. of Entry`
as mode_column from (select `Qty in Un. of Entry`, count(*) as max_count from project3_dataset
group by `Qty in Un. of Entry`
order by max_count desc
limit 1) as subquery;

select `Qty in Un. of Entry` as median_column from (select `Qty in Un. of Entry` ,Row_Number() over(order by `Qty in Un. of Entry`) as row_num, 
count(*) over() as total_count from project3_dataset) as subquery
where row_num = (total_count + 1)/2 or row_num = (total_count +2)/2;

#################### SECOND BUSINESS DECISION MOMENT ###############

select stddev(`Qty in Un. of Entry`) as col_std from project3_dataset;
select max(`Qty in Un. of Entry`) - min(`Qty in Un. of Entry`) as col_range from project3_dataset;
select variance(`Qty in Un. of Entry`) as col_variance from project3_dataset;

######################## THIRD MOMENT BUSINESS DECISION ######################

select (sum(power(`Qty in Un. of Entry` - (select avg(`Qty in Un. of Entry`)
from project3_dataset), 3))/
(count(*) * power (( select stddev(`Qty in Un. of Entry`) from project3_dataset),3))
) as skewness 
from project3_dataset;

########################## FOURTH MOMENT BUSINESS DECISION #######################

select ((SUM(power(`Qty in Un. of Entry` -(select avg(`Qty in Un. of Entry`) from project2_dataset),4 ))/
(count(*) * power(( select stddev(`Qty in Un. of Entry`) from project2_dataset), 4 ))) - 3) as kurtosis
from project3_dataset;

##################### DUPLICATES ######################

SELECT 'Qty in Un. of Entry', COUNT(*) as duplicate_count
FROM project3_dataset
GROUP BY `Qty in Un. of Entry`
HAVING COUNT(*) > 1;

##################### TYPECASTING ########################

SELECT CAST('Qty in Un. of Entry' AS CHAR(55)) AS  Entry_str
FROM project3_dataset;

################### OUTLIERS #####################

Select * , IF(ABS((`Qty in Un. of Entry` - AVG(`Qty in Un. of Entry`) OVER())/
stddev(`Qty in Un. of Entry`) OVER()) > 3,
'Outlier','Not Outlier') AS Outlier_Flag
From project3_dataset;

WITH stats AS (
    SELECT 
        AVG('Qty in Un. of Entry') AS mean_value,
        STDDEV('Qty in Un. of Entry') AS stddev_value
    FROM 
        project3_dataset
)
UPDATE project3_dataset
SET `Qty in Un. of Entry` = (SELECT mean_value FROM stats)
WHERE `Qty in Un. of Entry` < (SELECT mean_value - 3 * stddev_value FROM stats)
   OR `Qty in Un. of Entry` > (SELECT mean_value + 3 * stddev_value FROM stats);

***************** Second Column ********************
#################### FIRST BUSINESS DECISION MOMENT ######################

select avg(`Qty in OPUn`) as Inj1 from Project3_dataset;

select `Qty in OPUn`
as mode_column from (select `Qty in OPUn`, count(*) as max_count from project3_dataset
group by `Qty in OPUn`
order by max_count desc
limit 1) as subquery;

select `Qty in OPUn` as median_column from (select `Qty in OPUn` ,Row_Number() over(order by `Qty in OPUn`) as row_num, 
count(*) over() as total_count from project3_dataset) as subquery
where row_num = (total_count + 1)/2 or row_num = (total_count +2)/2;

#################### SECOND BUSINESS DECISION MOMENT ###############

select stddev(`Qty in OPUn`) as col_std from project3_dataset;
select max(`Qty in OPUn`) - min(`Qty in OPUn`) as col_range from project3_dataset;
select variance(`Qty in OPUn`) as col_variance from project3_dataset;

######################## THIRD MOMENT BUSINESS DECISION ######################

select (sum(power(`Qty in OPUn` - (select avg(`Qty in OPUn`)
from project3_dataset), 3))/
(count(*) * power (( select stddev(`Qty in OPUn`) from project3_dataset),3))
) as skewness 
from project3_dataset;

########################## FOURTH MOMENT BUSINESS DECISION #######################

select ((SUM(power(`Qty in OPUn` -(select avg(`Qty in OPUn`) from project2_dataset),4 ))/
(count(*) * power(( select stddev(`Qty in OPUn`) from project2_dataset), 4 ))) - 3) as kurtosis
from project3_dataset;

##################### DUPLICATES ######################

SELECT 'Qty in OPUn', COUNT(*) as duplicate_count
FROM project3_dataset
GROUP BY LM_WT
HAVING COUNT(*) > 1;

##################### TYPECASTING ########################

SELECT CAST('Qty in OPUn' AS CHAR(55)) AS  Entry_str
FROM project3_dataset;

################### OUTLIERS #####################

Select * , IF(ABS((`Qty in OPUn` - AVG(`Qty in OPUn`) OVER())/
stddev(`Qty in OPUn`) OVER()) > 3,
'Outlier','Not Outlier') AS Outlier_Flag
From project3_dataset;

WITH stats AS (
    SELECT 
        AVG('Qty in OPUn') AS mean_value,
        STDDEV('Qty in OPUn') AS stddev_value
    FROM 
        project3_dataset
)
UPDATE project3_dataset
SET `Qty in OPUn` = (SELECT mean_value FROM stats)
WHERE `Qty in OPUn` < (SELECT mean_value - 3 * stddev_value FROM stats)
   OR `Qty in OPUn` > (SELECT mean_value + 3 * stddev_value FROM stats);

************************* Third column *******************
#################### FIRST BUSINESS DECISION MOMENT ######################

select avg(`Qty in order unit`) as Inj1 from Project3_dataset;

select `Qty in order unit`
as mode_column from (select `Qty in order unit`, count(*) as max_count from project3_dataset
group by `Qty in order unit`
order by max_count desc
limit 1) as subquery;

select `Qty in order unit` as median_column from (select `Qty in order unit` ,Row_Number() over(order by `Qty in order unit`) as row_num, 
count(*) over() as total_count from project3_dataset) as subquery
where row_num = (total_count + 1)/2 or row_num = (total_count +2)/2;

#################### SECOND BUSINESS DECISION MOMENT ###############

select stddev(`Qty in order unit`) as col_std from project3_dataset;
select max(`Qty in order unit`) - min(`Qty in order unit`) as col_range from project3_dataset;
select variance(`Qty in order unit`) as col_variance from project3_dataset;

######################## THIRD MOMENT BUSINESS DECISION ######################

select (sum(power(`Qty in order unit` - (select avg(`Qty in order unit`)
from project3_dataset), 3))/
(count(*) * power (( select stddev(`Qty in order unit`) from project3_dataset),3))
) as skewness 
from project3_dataset;

########################## FOURTH MOMENT BUSINESS DECISION #######################

select ((SUM(power(`Qty in order unit` -(select avg(`Qty in order unit`) from project2_dataset),4 ))/
(count(*) * power(( select stddev(`Qty in order unit`) from project2_dataset), 4 ))) - 3) as kurtosis
from project3_dataset;

##################### DUPLICATES ######################

SELECT 'Qty in order unit', COUNT(*) as duplicate_count
FROM project3_dataset
GROUP BY `Qty in order unit`
HAVING COUNT(*) > 1;

##################### TYPECASTING ########################

SELECT CAST('Qty in order unit' AS CHAR(55)) AS  orderunit_str
FROM project3_dataset;

################### OUTLIERS #####################

Select * , IF(ABS((`Qty in order unit` - AVG(`Qty in order unit`) OVER())/
stddev(`Qty in order unit`) OVER()) > 3,
'Outlier','Not Outlier') AS Outlier_Flag
From project3_dataset;

WITH stats AS (
    SELECT 
        AVG('Qty in order unit') AS mean_value,
        STDDEV('Qty in order unit') AS stddev_value
    FROM 
        project3_dataset
)
UPDATE project3_dataset
SET `Qty in order unit` = (SELECT mean_value FROM stats)
WHERE `Qty in order unit` < (SELECT mean_value - 3 * stddev_value FROM stats)
   OR `Qty in order unit` > (SELECT mean_value + 3 * stddev_value FROM stats);

******************* Fourth column *********************88
#################### FIRST BUSINESS DECISION MOMENT ######################

select avg(`Amount in LC`) as Inj1 from Project3_dataset;

select `Amount in LC`
as mode_column from (select `Amount in LC`, count(*) as max_count from project3_dataset
group by `Amount in LC`
order by max_count desc
limit 1) as subquery;

select `Amount in LC` as median_column from (select `Amount in LC` ,Row_Number() over(order by `Amount in LC`) as row_num, 
count(*) over() as total_count from project3_dataset) as subquery
where row_num = (total_count + 1)/2 or row_num = (total_count +2)/2;

#################### SECOND BUSINESS DECISION MOMENT ###############

select stddev(`Amount in LC`) as col_std from project3_dataset;
select max(`Amount in LC`) - min(`Amount in LC`) as col_range from project3_dataset;
select variance(`Amount in LC`) as col_variance from project3_dataset;

######################## THIRD MOMENT BUSINESS DECISION ######################

select (sum(power(`Amount in LC` - (select avg(`Amount in LC`)
from project3_dataset), 3))/
(count(*) * power (( select stddev(`Amount in LC`) from project3_dataset),3))
) as skewness 
from project3_dataset;

########################## FOURTH MOMENT BUSINESS DECISION #######################

select ((SUM(power(`Amount in LC` -(select avg(`Amount in LC`) from project2_dataset),4 ))/
(count(*) * power(( select stddev(`Amount in LC`) from project2_dataset), 4 ))) - 3) as kurtosis
from project3_dataset;

##################### DUPLICATES ######################

SELECT 'Amount in LC', COUNT(*) as duplicate_count
FROM project3_dataset
GROUP BY `Amount in LC`
HAVING COUNT(*) > 1;

##################### TYPECASTING ########################

SELECT CAST('Amount in LC' AS CHAR(55)) AS  amount_str
FROM project3_dataset;

################### OUTLIERS #####################

Select * , IF(ABS((`Amount in LC` - AVG(`Amount in LC`) OVER())/
stddev(`Amount in LC`) OVER()) > 3,
'Outlier','Not Outlier') AS Outlier_Flag
From project3_dataset;

WITH stats AS (
    SELECT 
        AVG('Amount in LC') AS mean_value,
        STDDEV('Amount in LC') AS stddev_value
    FROM 
        project3_dataset
)
UPDATE project3_dataset
SET `Amount in LC` = (SELECT mean_value FROM stats)
WHERE `Amount in LC` < (SELECT mean_value - 3 * stddev_value FROM stats)
   OR `Amount in LC` > (SELECT mean_value + 3 * stddev_value FROM stats);

********************** Fifth column ********************
#################### FIRST BUSINESS DECISION MOMENT ######################

select avg(`Quantity`) as Inj1 from Project3_dataset;

select `Quantity`
as mode_column from (select `Quantity`, count(*) as max_count from project3_dataset
group by `Quantity`
order by max_count desc
limit 1) as subquery;

select `Quantity` as median_column from (select `Quantity` ,Row_Number() over(order by `Quantity`) as row_num, 
count(*) over() as total_count from project3_dataset) as subquery
where row_num = (total_count + 1)/2 or row_num = (total_count +2)/2;

#################### SECOND BUSINESS DECISION MOMENT ###############

select stddev(`Quantity`) as col_std from project3_dataset;
select max(`Quantity`) - min(`Quantity`) as col_range from project3_dataset;
select variance(`Quantity`) as col_variance from project3_dataset;

######################## THIRD MOMENT BUSINESS DECISION ######################

select (sum(power(`Quantity` - (select avg(`Quantity`)
from project3_dataset), 3))/
(count(*) * power (( select stddev(`Quantity`) from project3_dataset),3))
) as skewness 
from project3_dataset;

########################## FOURTH MOMENT BUSINESS DECISION #######################

select ((SUM(power(`Quantity` -(select avg(`Quantity`) from project2_dataset),4 ))/
(count(*) * power(( select stddev(`Quantity`) from project2_dataset), 4 ))) - 3) as kurtosis
from project3_dataset;

##################### DUPLICATES ######################

SELECT 'Quantity', COUNT(*) as duplicate_count
FROM project3_dataset
GROUP BY `Quantity`
HAVING COUNT(*) > 1;

##################### TYPECASTING ########################

SELECT CAST('Quantity' AS CHAR(55)) AS  quantity_str
FROM project3_dataset;

################### OUTLIERS #####################

Select * , IF(ABS((`Quantity` - AVG(`Quantity`) OVER())/
stddev(`Quantity`) OVER()) > 3,
'Outlier','Not Outlier') AS Outlier_Flag
From project3_dataset;

WITH stats AS (
    SELECT 
        AVG('Quantity') AS mean_value,
        STDDEV('Quantity') AS stddev_value
    FROM 
        project3_dataset
)
UPDATE project3_dataset
SET `Quantity` = (SELECT mean_value FROM stats)
WHERE `Quantity` < (SELECT mean_value - 3 * stddev_value FROM stats)
   OR `Quantity` > (SELECT mean_value + 3 * stddev_value FROM stats);




