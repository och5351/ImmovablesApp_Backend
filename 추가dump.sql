
--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `email` varchar(50) NOT NULL,
  `uid` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('changkeereum@gmail.com','103842694532689299916','강창기'),('elien940318@gmail.com','104354213223830137811','CG Kang');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;



--
-- Table structure for table `likelist`
--

DROP TABLE IF EXISTS `likelist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `likelist` (
  `num` int(11) NOT NULL AUTO_INCREMENT COMMENT '키',
  `email` varchar(50) NOT NULL COMMENT '회원정보',
  `board_idx` int(11) NOT NULL COMMENT '게시글번호',
  `type` tinyint(4) NOT NULL COMMENT '거래정보',
  PRIMARY KEY (`num`),
  KEY `FK_likelist_email_user_email` (`email`),
  KEY `FK_likelist_type_boardtype_num` (`type`),
  CONSTRAINT `FK_likelist_email_user_email` FOREIGN KEY (`email`) REFERENCES `user` (`email`),
  CONSTRAINT `FK_likelist_type_boardtype_num` FOREIGN KEY (`type`) REFERENCES `boardtype` (`num`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='좋아요리스트';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likelist`
--

LOCK TABLES `likelist` WRITE;
/*!40000 ALTER TABLE `likelist` DISABLE KEYS */;
INSERT INTO `likelist` VALUES (1,'changkeereum@gmail.com',5,1),(2,'elien940318@gmail.com',5,1),(3,'changkeereum@gmail.com',1,2);
/*!40000 ALTER TABLE `likelist` ENABLE KEYS */;
UNLOCK TABLES;



--
-- Table structure for table `recentlist`
--

DROP TABLE IF EXISTS `recentlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recentlist` (
  `num` int(11) NOT NULL AUTO_INCREMENT COMMENT '키',
  `email` varchar(50) NOT NULL COMMENT '회원정보',
  `board_idx` int(11) NOT NULL COMMENT '게시글번호',
  `type` tinyint(4) NOT NULL COMMENT '거래정보',
  PRIMARY KEY (`num`),
  KEY `FK_recentlist_email_user_email` (`email`),
  KEY `FK_recentlist_type_boardtype_num` (`type`),
  CONSTRAINT `FK_recentlist_email_user_email` FOREIGN KEY (`email`) REFERENCES `user` (`email`),
  CONSTRAINT `FK_recentlist_type_boardtype_num` FOREIGN KEY (`type`) REFERENCES `boardtype` (`num`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='최근리스트';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recentlist`
--

LOCK TABLES `recentlist` WRITE;
/*!40000 ALTER TABLE `recentlist` DISABLE KEYS */;
INSERT INTO `recentlist` VALUES (2,'changkeereum@gmail.com',5,1),(3,'changkeereum@gmail.com',2,1),(4,'elien940318@gmail.com',5,1);
/*!40000 ALTER TABLE `recentlist` ENABLE KEYS */;
UNLOCK TABLES;
