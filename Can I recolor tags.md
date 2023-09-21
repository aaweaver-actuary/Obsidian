```dataview
TABLE WITHOUT ID (tag + "(" + length(rows.file.link) + ")") AS Tags, length(rows.file.link) AS Count
FROM ""
WHERE file.tags
FLATTEN file.tags AS tag
GROUP BY tag
SORT tag
```
