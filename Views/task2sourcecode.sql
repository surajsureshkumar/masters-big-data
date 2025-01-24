CREATE VIEW gav_all_movie AS
    SELECT cm.id, cm.title, cm."startYear", 'Comedy' as genre
    FROM public.comedymovie cm UNION
                               SELECT ncm.id, ncm.title, ncm."startYear", Null as genre FROM public.noncomedymovie ncm;

CREATE VIEW gav_all_actor AS
    SELECT ca.id, ca.name, ca."birthYear", ca."deathYear"
    FROM public.comedyactor ca UNION
                               SELECT nca.id, nca.name, nca."birthYear", nca."deathYear" FROM public.noncomedyactor nca;

CREATE VIEW gav_all_movie_actor AS
    SELECT ain.id, ain.actor, ain.name FROM public.actedin ain;

CREATE MATERIALIZED VIEW gav_all_movie_mv AS
    SELECT cm.id, cm.title, cm."startYear", 'Comedy' as genre
    FROM public.comedymovie cm UNION
                               SELECT ncm.id, ncm.title, ncm."startYear", Null as genre FROM public.noncomedymovie ncm;

CREATE MATERIALIZED VIEW  gav_all_actor_mv AS
    SELECT ca.id, ca.name, ca."birthYear", ca."deathYear"
    FROM public.comedyactor ca UNION
                               SELECT nca.id, nca.name, nca."birthYear", nca."deathYear" FROM public.noncomedyactor nca;

CREATE MATERIALIZED VIEW gav_all_movie_actor_mv AS
    SELECT ain.id, ain.actor, ain.name FROM public.actedin ain;