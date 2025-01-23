create index title_runtime_index
    on "Title" (runtime);

create index "title_startYear_endYear_index"
    on "Title" ("startYear", "endYear");

create index title_title_index
    on "Title" (title);

create index genre_index
    on "Genre" (genre);

create index "member_birthYear_deathYear_index"
    on "Member" ("birthYear", "deathYear");

create index member_name_index
    on "Member" (name)
    
create index character_index
    on "Character" (character)

create index actor_title_character_actorindex
    on "Actor_Title_Character" (actor);

create index actor_title_character_title_index
    on "Actor_Title_Character" (title);

create index "Actor_Title_Character_character_index"
    on "Actor_Title_Character" (character);
    
create index title_actor_actor_index
    on "Title_Actor" (actor);

create index "Title_Actor_title_index"
    on "Title_Actor" (title);
    
create index "Title_Genre_genre_index"
    on "Title_Genre" (genre);

create index "Title_Genre_title_index"
    on "Title_Genre" (title);
    
create index "Title_Producer_producer_index"
    on "Title_Producer" (producer);

create index "Title_Producer_title_index"
    on "Title_Producer" (title);
    
