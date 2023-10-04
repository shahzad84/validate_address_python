a. 
SELECT count(*) 
FROM taxonomy 
WHERE name LIKE '%tiger%';

SELECT ncbi_id 
FROM taxonomy
WHERE name = 'Panthera tigris sumatrae';

b. The columns that can connect tables are:
- taxonomy.ncbi_id
- rfamseq.ncbi_id 
- rfamseq.rfam_acc
- family.rfam_acc 

c. 
SELECT taxonomy.name, rfamseq.length 
FROM taxonomy JOIN rfamseq ON taxonomy.ncbi_id = rfamseq.ncbi_id
ORDER BY rfamseq.length DESC 
LIMIT 1;

d. 
SELECT family.rfam_acc, family.description, MAX(rfamseq.length) as max_len
FROM family JOIN rfamseq ON family.rfam_acc = rfamseq.rfam_acc 
WHERE rfamseq.length > 1000000
GROUP BY family.rfam_acc, family.description
ORDER BY max_len DESC
LIMIT 15 OFFSET 120;