# Write your MySQL query statement below
SELECT DISTINCT S.product_id, P.product_name
FROM Sales AS S
JOIN Product AS P ON P.product_id = S.product_id
WHERE S.sale_date >= "2019-01-01"
AND S.sale_date <= "2019-03-31"
AND S.product_id NOT IN 
(SELECT S.product_id
FROM Sales AS S
WHERE S.sale_date < "2019-01-01"
OR S.sale_date > "2019-03-31")