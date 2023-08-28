-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: myproject
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `userid` int NOT NULL,
  `name` varchar(25) DEFAULT NULL,
  `phoneNumber` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Leonard Carroll','809-902-4957'),(2,'Sybill C. Kane','797-156-7733'),(3,'Ryder Stanton','857-833-6279'),(4,'Owen Robbins','102-490-9669'),(5,'Tyrone D. Harvey','364-220-7833'),(6,'Tanek T. Noble','577-561-5445'),(7,'Tanek X. Bridges','817-736-8954'),(8,'Latifah Q. Erickson','500-413-5229'),(9,'Geoffrey Erickson','311-237-5037'),(10,'Galvin Hart','501-807-7965'),(11,'Nolan Cummings','931-805-0046'),(12,'Inga K. Gonzales','736-865-1874'),(13,'Orson Dale','997-968-1425'),(14,'Rahim Mcdowell','554-339-3873'),(15,'Louis Mcguire','725-145-0036'),(16,'Kyra Bell','627-635-5250'),(17,'Kylee U. Hebert','906-664-4111'),(18,'Cora Collins','308-345-2108'),(19,'Mara Murray','794-251-3294'),(20,'Blair N. Weeks','563-321-0004'),(21,'Walter Callahan','568-397-1819'),(22,'Brynne V. Hayes','181-495-6507'),(23,'Hedy U. Wise','499-991-2743'),(24,'Nevada Langley','619-882-8501'),(25,'Sasha Church','853-381-3371'),(26,'Tamekah Cantu','332-466-8999'),(27,'Regan R. Cook','280-150-3915'),(28,'Christian England','385-898-0420'),(29,'Kevyn P. Cox','768-396-9425'),(30,'Leah B. Franklin','853-688-0957'),(31,'Urielle Humphrey','926-331-0012'),(32,'Kendall Lane','661-911-8866'),(33,'Ezra Randolph','922-755-8559'),(34,'Ashton Maddox','523-845-2705'),(35,'Sopoline Spence','614-499-4578'),(36,'Justin Guerrero','516-139-5882'),(37,'Phoebe S. Wynn','264-976-8713'),(38,'Noble R. Flynn','501-240-1875'),(39,'Buffy S. Chandler','859-284-1514'),(40,'Finn Hood','183-267-5415'),(41,'Alea V. Brewer','482-150-4868'),(42,'Elvis M. Watkins','634-901-1779'),(43,'Shafira T. Frank','483-164-3378'),(44,'Beck C. Herman','738-418-4743'),(45,'Minerva V. William','539-390-0106'),(46,'Dahlia Walls','953-437-1177'),(47,'Travis Savage','640-362-9129'),(48,'Illana Gallegos','762-486-9320'),(49,'Sylvia N. Santos','375-164-3524'),(50,'Baxter O. May','346-460-2655'),(51,'Glenna Dalton','913-377-4551'),(52,'Tiger C. Nieves','693-911-2291'),(53,'Mona M. Hurley','238-367-9905'),(54,'Isadora Y. Durham','284-851-0165'),(55,'Ryder Osborn','721-853-4940'),(56,'Blaze B. Aguirre','916-218-1512'),(57,'Summer V. Frazier','879-742-3407'),(58,'Lynn J. Sullivan','340-319-3768'),(59,'Faith M. Wood','908-750-3533'),(60,'Jakeem Velazquez','801-187-8092'),(61,'Adria Fields','755-909-1768'),(62,'Colby Mathews','294-493-0304'),(63,'Graiden O. Graves','217-211-8998'),(64,'Reece U. Case','984-206-6405'),(65,'Calvin A. Wiley','134-482-7453'),(66,'Hanna T. Stevens','896-641-3132'),(67,'Dominic Fleming','833-252-1580'),(68,'Garrett Goodwin','618-577-5738'),(69,'Charissa Dillard','213-729-8239'),(70,'Laurel C. Morales','847-648-1831'),(71,'Cathleen W. Burnett','956-194-4659'),(72,'Genevieve Whitney','919-463-1871'),(73,'Iola Gonzales','593-480-8818'),(74,'Aline Hampton','193-284-2494'),(75,'Lucy Q. Andrews','593-876-6529'),(76,'Athena P. Gray','393-826-7570'),(77,'Violet S. Underwood','425-483-4304'),(78,'Lev Phillips','281-817-4060'),(79,'Deanna Z. Snider','444-315-3902'),(80,'Otto U. Frye','384-258-6411'),(81,'Tatiana Dickson','180-578-2636'),(82,'Cathleen R. Aguilar','577-690-7062'),(83,'Sylvester H. Wiley','914-931-6799'),(84,'Xander G. Thornton','871-337-1836'),(85,'Rooney Hunter','857-195-6423'),(86,'Theodore G. Macias','412-369-2301'),(87,'Britanney Boyer','493-286-6876'),(88,'Wang Harper','923-883-5069'),(89,'Benjamin V. Young','652-797-0120'),(90,'Gray Z. Conner','202-685-6363'),(91,'Amal Mccoy','419-663-7344'),(92,'Kyra G. Reed','990-385-6303'),(93,'Reuben Gilmore','749-575-5329'),(94,'Thomas G. Robles','231-847-0873'),(95,'Kylynn L. Hardin','606-903-9466'),(96,'Regina F. Larsen','338-386-8025'),(97,'Xantha U. Graham','146-582-9214'),(98,'Adara N. Leonard','902-263-9357'),(99,'Ashton V. Hubbard','320-269-9789'),(100,'Robert Lester','579-713-6386');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-30 16:36:33
