SELECT gaa.name, count(gam.id)
FROM public.gav_all_actor gaa,
     public.gav_all_movie gam,
     public.gav_all_movie_actor gama
WHERE gaa."deathYear" is not NULL
  and gam."startYear" > 2000
  and gam."startYear" <= 2005
  AND gam.id = gama.id
  and gaa.id = gama.actor
GROUP BY gaa.name
HAVING count(gam.id) > 10;

SELECT DISTINCT gaa.name
FROM public.gav_all_actor gaa,
     public.gav_all_movie gam,
     public.gav_all_movie_actor gama
WHERE gaa.name LIKE 'Ja%'
  and gam.genre is NULL and gam.id = gama.id
and gaa.id = gama.id;
