CREATE TABLE teams (
    id integer not null primary key AUTO_INCREMENT,
    name varchar(255)
);

CREATE TABLE games (
    id integer not null primary key AUTO_INCREMENT,
    team1_id integer,
    team2_id integer,
    team1_pts integer,
    team2_pts integer,
    game_date date
);


ALTER TABLE `teams` CHANGE `id` `id` INT(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE `games` CHANGE `id` `id` INT(11) NOT NULL AUTO_INCREMENT;