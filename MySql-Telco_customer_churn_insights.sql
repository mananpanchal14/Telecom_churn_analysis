CREATE DATABASE churn_db;
USE churn_db;

#Used Table Data import hazard to upload the csv file into MySQL
SELECT * FROM telco;
SELECT MIN(tenure), MAX(tenure) 
FROM telco;

SELECT CASE WHEN Churn = "Yes" THEN 1 ELSE 0 END AS Churn_flag
	FROM telco;

ALTER TABLE telco
ADD COLUMN Churn_flag INT AFTER Churn;

SET SQL_SAFE_UPDATES = 0;
UPDATE telco
SET Churn_flag = CASE WHEN Churn = "Yes" THEN 1 ELSE 0 END;
SET SQL_SAFE_UPDATES = 1;

SELECT *
FROM telco;

SELECT Contract, COUNT(Churn_flag) AS total_customers,
	SUM(CASE WHEN Churn_flag = 1 THEN 1 END) AS churned_customers,
    ROUND(AVG(Churn_flag)*100,2) AS churn_rate
FROM telco
GROUP BY Contract
ORDER BY churn_rate DESC
LIMIT 1
;

SELECT InternetService, COUNT(Churn_flag) AS total_customers,
	SUM(CASE WHEN Churn_flag = 1 THEN 1 END) AS churned_customers,
    ROUND(AVG(Churn_flag)*100,2) AS churn_rate
FROM telco
GROUP BY InternetService
ORDER BY churn_rate DESC
;

SELECT Contract, InternetService, ROUND(AVG(Churn_flag)*100,2) AS churn_rate
	FROM telco
	GROUP BY Contract, InternetService
ORDER BY churn_rate DESC
;

