/* DATA CLEANING  */

-- check the imported table
SELECT * 
FROM data_table;


/* 1. Make a Copy of the Data */
CREATE TABLE datatable_copy
LIKE data_table;

INSERT datatable_copy
SELECT * FROM data_table;

-- check the new table
SELECT * 
FROM datatable_copy;

-- Add a new column named ID to the table and set it as the primary key with auto-increment
ALTER TABLE datatable_copy
ADD ID INT AUTO_INCREMENT PRIMARY KEY;

/* 2. Remove Blank Rows */

-- Check for blank rows
SELECT *
FROM datatable_copy
WHERE `Declaration` = '' AND `Date reception` = '' AND `Frais engages` = '' AND `Police` = '' AND `Adherent CIN` = '' AND `Adherent ville` = '' AND `Code maladie` = '';

-- Delete the blank rows
DELETE FROM datatable_copy
WHERE `Declaration` = '' 
AND `Date reception` = '' 
AND `Frais engages` = '' 
AND `Police` = '' 
AND `Adherent CIN` = '' 
AND `Adherent Ville` = '' 
AND `Code maladie` = '';

/* 3. Remove Duplicates */

-- Identify the Duplicates
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY `Declaration`, `Date reception`, `Frais engages`, `Police`, `Adherent CIN`, `Adherent ville`, `Code maladie` ORDER BY ID) AS row_num
    FROM datatable_copy
) AS temp
WHERE row_num > 1;

-- Little check
SELECT * 
FROM datatable_copy
WHERE `Adherent CIN` = 'BE07IM';

-- Delete the Duplicates
DELETE FROM datatable_copy
WHERE ID IN (
    SELECT ID FROM (
        SELECT ID,
               ROW_NUMBER() OVER (PARTITION BY `Declaration`, `Date reception`, `Frais engages`, `Police`, `Adherent CIN`, `Adherent ville`, `Code maladie` ORDER BY ID) AS row_num
    FROM datatable_copy
    ) AS temp
    WHERE row_num > 1
);

/* 4. Standardize the Data */

ALTER TABLE datatable_copy
MODIFY COLUMN `Declaration` INT;

ALTER TABLE datatable_copy
MODIFY COLUMN `date reception` DATE;

ALTER TABLE datatable_copy
MODIFY COLUMN `Frais engages` FLOAT;

ALTER TABLE datatable_copy
MODIFY COLUMN `Code maladie` INT;




