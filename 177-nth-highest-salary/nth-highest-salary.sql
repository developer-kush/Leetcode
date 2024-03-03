CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below

    WITH cte as (
        SELECT e.salary, dense_rank() over(ORDER by e.salary Desc) as rank
        From Employee as e
    )

    SELECT cte.salary
    FROM cte 
    WHERE rank = N
    LIMIT 1

  );
END;
$$ LANGUAGE plpgsql;