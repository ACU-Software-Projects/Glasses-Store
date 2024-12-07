-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `mydb`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `mydb` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `mydb`;

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account` (
  `idAccount` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  `Balance` int NOT NULL DEFAULT '0',
  `AccountType` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idAccount`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (1,'mostafa','mostafa@gmail.com','12345678',7240,'USER'),(2,'yousef','yourself@gmail.com','123456778',0,'USER'),(3,'mostafamostafa','mostafa.motafa@gmail.com','12345678',19800,'ADMIN'),(4,'yourself','yourself@gmail.com','12345678',101919,'USER'),(5,'saifsaif','saifsaif@gmail.com','12345678',1300000,'ADMIN');
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `idAdmin` int unsigned NOT NULL AUTO_INCREMENT,
  `Role` varchar(45) DEFAULT NULL,
  `Account_AccountId` int NOT NULL,
  PRIMARY KEY (`idAdmin`),
  KEY `fk_Admin_Account1_idx` (`Account_AccountId`),
  CONSTRAINT `fk_Admin_Account1` FOREIGN KEY (`Account_AccountId`) REFERENCES `account` (`idAccount`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'product manger',1),(2,'product manger',3),(3,'product manger',5);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `idCart` int NOT NULL,
  `User_idUser` int NOT NULL,
  PRIMARY KEY (`idCart`),
  KEY `fk_Cart_User1_idx` (`User_idUser`),
  CONSTRAINT `fk_Cart_User1` FOREIGN KEY (`User_idUser`) REFERENCES `user` (`idUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart_has_product`
--

DROP TABLE IF EXISTS `cart_has_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_has_product` (
  `Cart_idCart` int NOT NULL,
  `Product_idProduct` int NOT NULL,
  PRIMARY KEY (`Cart_idCart`,`Product_idProduct`),
  KEY `fk_Cart_has_Product_Product1_idx` (`Product_idProduct`),
  KEY `fk_Cart_has_Product_Cart1_idx` (`Cart_idCart`),
  CONSTRAINT `fk_Cart_has_Product_Cart1` FOREIGN KEY (`Cart_idCart`) REFERENCES `cart` (`idCart`),
  CONSTRAINT `fk_Cart_has_Product_Product1` FOREIGN KEY (`Product_idProduct`) REFERENCES `product` (`idProduct`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_has_product`
--

LOCK TABLES `cart_has_product` WRITE;
/*!40000 ALTER TABLE `cart_has_product` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart_has_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoice`
--

DROP TABLE IF EXISTS `invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice` (
  `idInvoice` int NOT NULL,
  `IssueDate` date NOT NULL,
  PRIMARY KEY (`idInvoice`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice`
--

LOCK TABLES `invoice` WRITE;
/*!40000 ALTER TABLE `invoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `invoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoice_has_product`
--

DROP TABLE IF EXISTS `invoice_has_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice_has_product` (
  `Invoice_idInvoice` int NOT NULL,
  `Product_idProduct` int NOT NULL,
  PRIMARY KEY (`Invoice_idInvoice`,`Product_idProduct`),
  KEY `fk_Invoice_has_Product_Product1_idx` (`Product_idProduct`),
  KEY `fk_Invoice_has_Product_Invoice1_idx` (`Invoice_idInvoice`),
  CONSTRAINT `fk_Invoice_has_Product_Invoice1` FOREIGN KEY (`Invoice_idInvoice`) REFERENCES `invoice` (`idInvoice`),
  CONSTRAINT `fk_Invoice_has_Product_Product1` FOREIGN KEY (`Product_idProduct`) REFERENCES `product` (`idProduct`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice_has_product`
--

LOCK TABLES `invoice_has_product` WRITE;
/*!40000 ALTER TABLE `invoice_has_product` DISABLE KEYS */;
/*!40000 ALTER TABLE `invoice_has_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoice_has_user`
--

DROP TABLE IF EXISTS `invoice_has_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice_has_user` (
  `Invoice_idInvoice` int NOT NULL,
  `User_idUser` int NOT NULL,
  PRIMARY KEY (`Invoice_idInvoice`,`User_idUser`),
  KEY `fk_Invoice_has_User_User1_idx` (`User_idUser`),
  KEY `fk_Invoice_has_User_Invoice1_idx` (`Invoice_idInvoice`),
  CONSTRAINT `fk_Invoice_has_User_Invoice1` FOREIGN KEY (`Invoice_idInvoice`) REFERENCES `invoice` (`idInvoice`),
  CONSTRAINT `fk_Invoice_has_User_User1` FOREIGN KEY (`User_idUser`) REFERENCES `user` (`idUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice_has_user`
--

LOCK TABLES `invoice_has_user` WRITE;
/*!40000 ALTER TABLE `invoice_has_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `invoice_has_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `idProduct` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `Productcol` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `Productcol1` varchar(45) DEFAULT NULL,
  `Admin_idAdmin` int NOT NULL,
  `ImageSrc` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idProduct`),
  KEY `fk_Product_Admin1_idx` (`Admin_idAdmin`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (10,'mmmmmmm12',1112,NULL,'good product',NULL,3,'saif.jpg'),(11,'mmmmmmm12',1112,NULL,'good product',NULL,3,'saif.jpg'),(12,'anti reflectoion',2222,NULL,'good product',NULL,3,'yourself.png'),(13,'youef bakr3',1111,NULL,'good product',NULL,3,'yousef.jpg'),(14,'mmmmmmm25',2525,NULL,'good product',NULL,3,'yousef.jpg');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `idUser` int NOT NULL AUTO_INCREMENT,
  `Account_AccountId` int NOT NULL,
  PRIMARY KEY (`idUser`),
  UNIQUE KEY `UserId_UNIQUE` (`idUser`),
  KEY `fk_User_Account_idx` (`Account_AccountId`),
  CONSTRAINT `fk_User_Account` FOREIGN KEY (`Account_AccountId`) REFERENCES `account` (`idAccount`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,2),(2,4);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_products`
--

DROP TABLE IF EXISTS `user_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_products` (
  `IdAccount` int NOT NULL,
  `IdProduct` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_products`
--

LOCK TABLES `user_products` WRITE;
/*!40000 ALTER TABLE `user_products` DISABLE KEYS */;
INSERT INTO `user_products` VALUES (4,13),(4,14),(4,12),(4,13),(4,11);
/*!40000 ALTER TABLE `user_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'mydb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-07 15:58:39
