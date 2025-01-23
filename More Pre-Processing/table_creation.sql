create table hw_schema."Title"
(
    id              integer not null
        constraint "Title_pk"
            primary key,
    "avgRating"     numeric,
    "numVotes"      integer,
    type            varchar,
    title           varchar,
    "originalTitle" varchar,
    "startYear"     integer,
    "endYear"       integer,
    runtime         integer
)



create table hw_schema."Genre"
(
    id    integer not null
        constraint "Genre_pk"
            primary key,
    genre varchar
);


create table hw_schema."Title_Actor"
(
    actor integer not null
        constraint member_actor_fk_id
            references "Member",
    title integer not null
        constraint title_actor_fk_id
            references "Title",
    constraint "Title_Actor_pk"
        primary key (title, actor)
);


create table hw_schema."Member"
(
    id          integer not null
        constraint "Member_pk"
            primary key,
    name        varchar,
    "birthYear" integer,
    "deathYear" integer
);


create table hw_schema."Title_Writer"
(
    writer integer
        constraint title_writer_fk_member
            references "Member",
    title  integer
        constraint title_writer_fk_title
            references "Title"
);


create table hw_schema."Title_Director"
(
    director integer not null
        constraint title_director_fk_director
            references "Member",
    title    integer not null
        constraint title_director_fk_title
            references "Title",
    constraint "Title_Director_pk"
        primary key (title, director)
);


create table hw_schema"Title_Producer"
(
    producer integer not null
        constraint title_producer_fk_producer
            references "Member",
    title    integer not null
        constraint title_producer_fk_title
            references "Title",
    constraint "Title_Producer_pk"
        primary key (producer, title)
);


create table hw_schema."Actor_Title_Character"
(
    actor     integer not null,
    title     integer not null,
    character integer not null
        constraint "Actor_Title_Character_Character_id_fk"
            references "Character",
    constraint "Actor_Title_Character_pk"
        primary key (actor, title, character),
    constraint "Actor_Title_Character_Title_Actor_actor_title_fk"
        foreign key (actor, title) references "Title_Actor" (actor, title)
);

