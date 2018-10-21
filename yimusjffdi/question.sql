CREATE TABLE `question` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `question` char(200) DEFAULT NULL,
  `answer` int(200) DEFAULT NULL,
  `correct` boolean DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `question_answer` (`question`, `answer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
