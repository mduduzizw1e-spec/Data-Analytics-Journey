-- Project: Project Title
-- Purpose: Save analysis queries here.
-- Tip: Keep each query labeled with the question it answers.

-- 1. Row count and basic inspection
SELECT COUNT(*) AS row_count
FROM table_name;

-- 2. Example aggregation
SELECT
    category_column,
    COUNT(*) AS records,
    SUM(numeric_column) AS total_value
FROM table_name
GROUP BY category_column
ORDER BY total_value DESC;
