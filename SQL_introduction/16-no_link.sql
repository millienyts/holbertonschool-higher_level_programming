-- List all records in second_table with a name value
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
