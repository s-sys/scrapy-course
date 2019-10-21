CREATE TABLE steamdb(
   source_url           VARCHAR(500) NOT NULL PRIMARY KEY,
   publisher            VARCHAR(500),
   name                 VARCHAR(500),
   rating               VARCHAR(500),
   store_url            VARCHAR(500),
   supported_systems    VARCHAR(500),
   in_game              VARCHAR(500),
   day_player_peak      VARCHAR(500),
   all_time_player_peak VARCHAR(500),
   developer            VARCHAR(500)
);
