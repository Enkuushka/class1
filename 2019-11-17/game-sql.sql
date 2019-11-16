CREATE TABLE teams (
    id integer not null primary key,
    name varchar(255)
);

CREATE TABLE games (
    id integer not null primary key,
    team1_id integer,
    team2_id integer,
    team1_pts integer,
    team2_pts integer,
    game_date date
);