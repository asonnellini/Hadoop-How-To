CREATE TABLE IF NOT EXISTS Sonne_drivers_orc(driverId int, name string, ssn integer, location string, certified string, wageplan string) COMMENT 'Data about drivers from a public database' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS ORC;