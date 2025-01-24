SELECT ca.name,count(c.id) FROM (SELECT cm.id, cm.title, cm."startYear", 'Comedy' as genre
    FROM public.comedymovie cm UNION
                               SELECT ncm.id, ncm.title, ncm."startYear", Null as genre FROM public.noncomedymovie ncm) AS c,
(SELECT ca.id, ca.name, ca."birthYear", ca."deathYear"
    FROM public.comedyactor ca UNION
                               SELECT nca.id, nca.name, nca."birthYear", nca."deathYear" FROM public.noncomedyactor nca) AS ca,
                (SELECT ain.id, ain.actor FROM public.actedin ain) ain
WHERE ca."deathYear" is not NULL
  and c."startYear" > 2000
  and c."startYear" <= 2005
  AND c.id = ca.id
  and c.id = ain.actor
GROUP BY ca.name
HAVING count(c.id) > 10;


SELECT DISTINCT ca.name FROM (SELECT cm.id, cm.title, cm."startYear", 'Comedy' as genre
    FROM public.comedymovie cm UNION
                               SELECT ncm.id, ncm.title, ncm."startYear", Null as genre FROM public.noncomedymovie ncm) AS c,
(SELECT ca.id, ca.name, ca."birthYear", ca."deathYear"
    FROM public.comedyactor ca UNION
                               SELECT nca.id, nca.name, nca."birthYear", nca."deathYear" FROM public.noncomedyactor nca) AS ca,
                (SELECT ain.id, ain.actor FROM public.actedin ain) ain
WHERE ca.name LIKE 'Ja%'
  and c.genre is NULL and ca.id = ain.id
and c.id = ain.id;

-----------------------------------------------------------------------

SELECT ca.name,count(c.id) FROM (SELECT cm.id, cm.title, cm."startYear", 'Comedy' as genre
    FROM public.comedymovie_mv cm UNION
                               SELECT ncm.id, ncm.title, ncm."startYear", Null as genre FROM public.noncomedymovie_mv ncm) AS c,
(SELECT ca.id, ca.name, ca."birthYear", ca."deathYear"
    FROM public.comedyactor_mv ca UNION
                               SELECT nca.id, nca.name, nca."birthYear", nca."deathYear" FROM public.noncomedyactor_mv nca) AS ca,
                (SELECT ain.id, ain.actor FROM public.actedin_mv ain) ain
WHERE ca."deathYear" is not NULL
  and c."startYear" > 2000
  and c."startYear" <= 2005
  AND c.id = ca.id
  and c.id = ain.actor
GROUP BY ca.name
HAVING count(c.id) > 10;


SELECT DISTINCT ca.name FROM (SELECT cm.id, cm.title, cm."startYear", 'Comedy' as genre
    FROM public.comedymovie_mv cm UNION
                               SELECT ncm.id, ncm.title, ncm."startYear", Null as genre FROM public.noncomedymovie_mv ncm) AS c,
(SELECT ca.id, ca.name, ca."birthYear", ca."deathYear"
    FROM public.comedyactor_mv ca UNION
                               SELECT nca.id, nca.name, nca."birthYear", nca."deathYear" FROM public.noncomedyactor_mv nca) AS ca,
                (SELECT ain.id, ain.actor FROM public.actedin_mv ain) ain
WHERE ca.name LIKE 'Ja%'
  and c.genre is NULL and ca.id = ain.id
and c.id = ain.id;