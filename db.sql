-- MariaDB dump 10.19  Distrib 10.6.4-MariaDB, for osx10.16 (arm64)
--
-- Host: localhost    Database: candy_store
-- ------------------------------------------------------
-- Server version	10.6.4-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `candy`
--

DROP TABLE IF EXISTS `candy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `candy` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `description` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `image_url` varchar(500) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `candy_UN` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `candy`
--

LOCK TABLES `candy` WRITE;
/*!40000 ALTER TABLE `candy` DISABLE KEYS */;
INSERT INTO `candy` VALUES (1,'Ferrero Collection Gold','Fine assortied confections','https://images2.minutemediacdn.com/image/fetch/w_2000,h_2000,c_fit/https%3A%2F%2Ffoodsided.com%2Ffiles%2Fimage-exchange%2F2016%2F04%2Fie_38077.jpeg'),(2,'Ferrero Rocher Hearts','Fine hazelnut chocolates','https://target.scene7.com/is/image/Target/GUEST_9f1a3216-8f22-4ddb-bc06-5776205c9918'),(5,'Ferrero Collection Mix','Fine assortied confections','https://i5.walmartimages.com/asr/518b6aec-504d-428f-a3e3-4992993bad14.4c079899839780d5a51815ab8cfd3eb8.jpeg'),(6,'Ferrero Rocher Heart','Hollow milk chocolate','https://i5.walmartimages.com/asr/14b349da-7fc4-4b9a-a7bc-caf0968d0cb8.671d01b2a781da1262b6ddd5d43b7b41.jpeg'),(7,'Elmer\'s Valentine’s Chocolate Puppy','Finest selection','https://i5.walmartimages.ca/images/Enlarge/103/456/41761103456.jpg'),(8,'Lindt LINDOR Amour Gold','Assorted Chocolate Hearts Box','https://i5.walmartimages.ca/images/Enlarge/028/125/999999-37466028125.jpg'),(9,'NESTLÉ TURTLES','Classic Recipe Valentine\'s Heart Gift Box','https://i5.walmartimages.ca/images/Enlarge/799/695/6000196799695.jpg'),(10,'Kinder Surprise Valentine','Assorted Chocolate','https://i5.walmartimages.ca/images/Enlarge/632/069/6000204632069.jpg'),(11,'Lindt LINDOR Amour Red','Assorted Chocolate Hearts Box','https://i5.walmartimages.ca/images/Enlarge/016/337/999999-37466016337.jpg'),(12,'REESE\'S Miniatures ','Peanut Butter Cups Candy','https://i5.walmartimages.ca/images/Enlarge/617/083/6000204617083.jpg');
/*!40000 ALTER TABLE `candy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'candy_store'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-08 22:56:37
