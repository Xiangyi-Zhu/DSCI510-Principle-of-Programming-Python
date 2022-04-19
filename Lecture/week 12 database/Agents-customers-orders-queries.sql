-- Based on data from https://www.w3resource.com/sql/sql-table.php

SELECT * FROM agents;

SELECT AGENT_NAME, PHONE_NO FROM agents;

SELECT * FROM agents WHERE WORKING_AREA = 'Bangalore';

SELECT * FROM orders WHERE ORD_AMOUNT  >  3000;

SELECT * FROM orders WHERE ORD_AMOUNT >= 3000 ORDER BY ORD_AMOUNT DESC;

SELECT * FROM orders o, agents a  WHERE  o.AGENT_CODE = a.AGENT_CODE;

SELECT *
FROM orders o, agents a
WHERE o.ORD_AMOUNT >= 3000 AND
      o.AGENT_CODE = a.AGENT_CODE
ORDER BY ORD_AMOUNT DESC;


SELECT a.AGENT_NAME, o.ORD_AMOUNT, a.PHONE_NO, a.WORKING_AREA
FROM orders o, agents a
WHERE  o.AGENT_CODE = a.AGENT_CODE
       AND o.ORD_AMOUNT  >  3000
ORDER BY o.ORD_AMOUNT DESC;    


SELECT AGENT_CODE, sum(ORD_AMOUNT)
FROM orders
GROUP BY AGENT_CODE;


SELECT AGENT_CODE, sum(ORD_AMOUNT) as total_orders
FROM orders
GROUP BY AGENT_CODE
ORDER BY total_orders DESC;  


SELECT *
FROM
agents a, 
(
SELECT AGENT_CODE, sum(ORD_AMOUNT) as total_orders
FROM orders
GROUP BY AGENT_CODE
) o
WHERE o.AGENT_CODE = a.AGENT_CODE
ORDER BY total_orders DESC;  

#create a subquery called o

SELECT a.AGENT_NAME, o.total_orders, a.PHONE_NO, a.WORKING_AREA
FROM
agents a, 
(
SELECT AGENT_CODE, sum(ORD_AMOUNT) as total_orders
FROM orders
GROUP BY AGENT_CODE
) o
WHERE o.AGENT_CODE = a.AGENT_CODE
ORDER BY total_orders DESC;  








