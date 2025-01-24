CREATE TABLE Popular_Movie_Actors AS
SELECT ta.*
FROM hw_schema."Title_Actor" ta
         JOIN (SELECT id, title, runtime
               FROM hw_schema."Title" t
               WHERE type = 'movie'
                 AND "avgRating" > 5) m ON ta.title = m.id;

CREATE TABLE L1 AS
SELECT pma.actor AS actor1, COUNT(*) AS count
FROM public.popular_movie_actors pma
GROUP BY pma.actor
HAVING COUNT(*) >= 5;

CREATE TABLE L2 AS
SELECT l1.actor1, l2.actor1 as actor2, COUNT(*) AS count
FROM public.l1 l1,
     public.l1 l2,
     public.popular_movie_actors pma,
     public.popular_movie_actors pma1
WHERE l1.actor1 = pma.actor
  and l2.actor1 = pma1.actor
  and l1.actor1 < l2.actor1
  and pma.title = pma1.title
GROUP BY l1.actor1, l2.actor1
HAVING COUNT(*) >= 5;

CREATE TABLE L3 AS
SELECT a.actor1, a.actor2, b.actor2 as actor3, COUNT(*) AS count
FROM public.l2 a,
     public.l2 b,
     public.popular_movie_actors pma1,
     public.popular_movie_actors pma2,
     public.popular_movie_actors pma3
WHERE a.actor1 = pma1.actor
  and a.actor2 = pma2.actor
  and b.actor2 = pma3.actor
  and a.actor1 = b.actor1
  and a.actor2 < b.actor2
  and pma1.title = pma2.title
  and pma2.title = pma3.title
GROUP BY a.actor1, a.actor2, b.actor2
HAVING COUNT(*) >= 5;

SELECT m1.name,m2.name,m3.name,m4.name,m5.name,m6.name FROM hw_schema."Member" m1,
                hw_schema."Member" m2,
                hw_schema."Member" m3,
                hw_schema."Member" m4,
                hw_schema."Member" m5,
                hw_schema."Member" m6,
                public.l6 l6
WHERE m1.id = l6.actor1
and m2.id = l6.actor2
and m3.id = l6.actor3
and m4.id = l6.actor4
and m5.id = l6.actor5
and m6.id = l6.actor6;