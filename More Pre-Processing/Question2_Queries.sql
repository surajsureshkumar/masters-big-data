--Query 2.1:
SELECT COUNT(*) FROM hw_schema."Title_Actor" ta
LEFT JOIN hw_schema."Actor_Title_Character" atc
ON ta.actor = atc.actor WHERE atc.actor IS NULL;
    
    
--Query 2.2:
SELECT DISTINCT m.*
from hw_schema."Member" as m,hw_schema."Title_Actor" ta, hw_schema."Title" t
WHERE m.id = ta.actor
and m.name LIKE 'Phi%'
and m."deathYear" is NULL
and t.id = ta.title
and m.id = ta."actor"
and (t."endYear" < 2014 or t."startYear">2014);


--Query 2.3
select m.name,tp.producer,count(tp.title) show_count
from hw_schema."Title_Producer" tp,hw_schema."Genre" g,hw_schema."Title_Genre" tg,hw_schema."Member" m,hw_schema."Title" t
where g.genre = 'Talk-Show' and g.id = tg.genre and tp.title = tg.title
and t.id = tp.title
and m.id = tp.producer
and 2017 >= t."startYear"
and m.name like '%Gill%'
group by m.name,tp.producer;

--Query2.4
select m.name,count(t.id) title_count
from hw_schema."Title" t, hw_schema."Title_Producer" tp, hw_schema."Member" m
where tp.producer = m.id
and t.id = tp.title
and t.runtime > 120
and m."deathYear" is NULL
group by m.name
order by title_count desc;

--Query2.5
select DISTINCT M.name,m.id
from hw_schema."Member" m, hw_schema."Character" c, hw_schema."Actor_Title_Character" atc
where m.id = atc.actor
and atc.character = c.id
and c.character = 'Jesus Christ'
and m."deathYear" is NULL;