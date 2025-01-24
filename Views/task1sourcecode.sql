CREATE VIEW ComedyMovie AS
    SELECT t."id", t."startYear", t.title
    from hw_schema."Genre" g, hw_schema."Title" t, hw_schema."Title_Genre" tg
WHERE g.genre = 'Comedy'
  and t.runtime > 75
  and t.id = tg.title
  and tg.genre = g.id;

CREATE VIEW NonComedyMovie AS
    SELECT t."id", t."startYear", t.title
    from hw_schema."Title" t
WHERE
   t.runtime > 75
  and t.id not in(select t.id from hw_schema."Title" t, hw_schema."Title_Genre" tg WHERE tg.genre = 3 and t.id = tg.title);

CREATE VIEW ComedyActor AS
    SELECT t."id",m.name,m."birthYear",m."deathYear"
    from hw_schema."Title" t, hw_schema."Member" m, hw_schema."Genre" g,
                                                          hw_schema."Title_Genre" tg,hw_schema."Title_Actor" ta
WHERE g.genre = 'Comedy'
  and t.runtime > 75
  and t.id = tg.title
  and tg.genre = g.id
  and ta.actor = m.id
  and t.id = ta.title;


CREATE VIEW NonComedyActor AS
    SELECT t."id",m.name,m."birthYear",m."deathYear"
    from hw_schema."Title" t, hw_schema."Member" m, hw_schema."Title_Actor" ta
WHERE t.runtime > 75
  and ta.actor = m.id
  and ta.title = t.id
  and t.id not in (SELECT t.id from hw_schema."Title" t , hw_schema."Title_Genre" tg
                               WHERE tg.genre = 3
                               and t.id = tg.title);

CREATE  VIEW ActedIn AS
    SELECT t.id, ta.actor, m.name
    from hw_schema."Title" t, hw_schema."Title_Actor" ta, hw_schema."Member" m
WHERE t.id = ta.title and m.id = ta.actor and t.runtime > 75 and t.type = 'movie';
 ----------------------------------------------------------------------------------------------------------------
 ----------------------------------------------------------------------------------------------------------------
 -----------------------------------------------MATERIALIZED VIEWS-----------------------------------------------

CREATE MATERIALIZED VIEW ComedyMovie_mv AS
    SELECT t."id", t."startYear", t.title
    from hw_schema."Genre" g, hw_schema."Title" t, hw_schema."Title_Genre" tg
WHERE g.genre = 'Comedy'
  and t.runtime > 75
  and t.id = tg.title
  and tg.genre = g.id;

CREATE MATERIALIZED VIEW NonComedyMovie_mv AS
    SELECT t."id", t."startYear", t.title
    from hw_schema."Title" t
WHERE
   t.runtime > 75
  and t.id not in(select t.id from hw_schema."Title" t, hw_schema."Title_Genre" tg WHERE tg.genre = 3 and t.id = tg.title);

CREATE MATERIALIZED VIEW ComedyActor_mv AS
    SELECT t."id",m.name,m."birthYear",m."deathYear"
    from hw_schema."Title" t, hw_schema."Member" m, hw_schema."Genre" g,
                                                          hw_schema."Title_Genre" tg,hw_schema."Title_Actor" ta
WHERE g.genre = 'Comedy'
  and t.runtime > 75
  and t.id = tg.title
  and tg.genre = g.id
  and ta.actor = m.id
  and t.id = ta.title;

CREATE MATERIALIZED VIEW NonComedyActor_mv AS
    SELECT t."id",m.name,m."birthYear",m."deathYear"
    from hw_schema."Title" t, hw_schema."Member" m, hw_schema."Title_Actor" ta
WHERE t.runtime > 75
  and ta.actor = m.id
  and ta.title = t.id
  and t.id not in (SELECT t.id from hw_schema."Title" t , hw_schema."Title_Genre" tg
                               WHERE tg.genre = 3
                               and t.id = tg.title);

CREATE  MATERIALIZED VIEW ActedIn_mv AS
    SELECT t.id, ta.actor, m.name
    from hw_schema."Title" t, hw_schema."Title_Actor" ta, hw_schema."Member" m
WHERE t.id = ta.title and m.id = ta.actor and t.runtime > 75 and t.type = 'movie';