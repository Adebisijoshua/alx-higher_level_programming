-- script that creates the secondrable in the hash table
CREATE table IF NOT EXISTS second_table (`id` INT,
`name` VARCHAR(256),
`score` INT);
INSERT INTO `second_table` (`id`, `name`, `score`)
VALUES
       (1, 'Joshua', 10),
       (2, 'JUdah', 3),
       (3, 'Zin', 14),
       (4, 'George', 8)
