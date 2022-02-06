CREATE TABLE customers(
    id INT AUTO_INCREMENT  PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE orders(
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE,
    amount DECIMAL (8,2),
    customer_id INT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
);

SELECT * FROM orders WHERE customer_id =
(
	SELECT id FROM customers
	WHERE last_name = 'George'
);


-- IMPLICIT INNER JOIN:
SELECT * FROM customers, orders WHERE customers.id = orders.customer_id;

-- EXPLICIT INNER JOIN (BETTER TO USE THAN IMPLICIT JOINS):
SELECT * FROM customers
JOIN orders ON customers.id = orders.customer_id;

SELECT first_name, last_name, email FROM customers
JOIN orders ON customers.id = orders.customer_id;

-- Put all columns you want from both tables after select**
-- Case statements usually go after the columns are selected and before FROM 'table'

-- Getting Fancy:
SELECT first_name, last_name, amount, email FROM customers
JOIN orders ON customers.id = orders.customer_id
ORDER BY amount DESC;

SELECT first_name, last_name, customer_id, SUM(amount) AS total_spent FROM customers
JOIN orders ON customers.id = orders.customer_id
GROUP BY orders.customer_id
ORDER BY total_spent DESC;

-- LEFT JOIN (Select everything from left table, join with matches from right table):
SELECT * FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id;

SELECT first_name, last_name, SUM(amount) AS total_spent FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.id
ORDER BY total_spent DESC;

SELECT
	first_name, 
	last_name,
	IFNULL(SUM(amount), 0) AS total_spent
FROM customers
LEFT JOIN orders
	ON customers.id = orders.customer_id
GROUP BY customers.id
ORDER BY total_spent DESC;

-- RIGHT JOIN (Select everything from right table, join with matches from left table)
SELECT * FROM customers
RIGHT JOIN orders ON customers.id = orders.customer_id;

-- ON DELETE CASCADE (When one thing from a row is deleted, delete the entire row)

SELECT first_name, IFNULL(AVG(grade), 0) AS average,
CASE
    WHEN AVG(grade) IS NULL THEN 'Failing'
    WHEN AVG(grade) >= 75 THEN 'Passing'
    ELSE 'Failing'
    END AS passing_status
FROM students
    LEFT JOIN papers
    ON students.id = papers.student_id
GROUP BY students.id
ORDER BY average DESC;