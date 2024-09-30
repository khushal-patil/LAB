-- MySQL dump 10.13  Distrib 5.7.42, for Linux (x86_64)
--
-- Host: localhost    Database: khushal_assign3
-- ------------------------------------------------------
-- Server version	5.7.42-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Account`
--

DROP TABLE IF EXISTS `Account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Account` (
  `Acc_no` int(11) NOT NULL,
  `branch_name` varchar(25) DEFAULT NULL,
  `balance` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`Acc_no`),
  KEY `branch_name` (`branch_name`),
  CONSTRAINT `Account_ibfk_1` FOREIGN KEY (`branch_name`) REFERENCES `Branch` (`branch_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Account`
--

LOCK TABLES `Account` WRITE;
/*!40000 ALTER TABLE `Account` DISABLE KEYS */;
INSERT INTO `Account` VALUES (1011,'Akurdi-Branch','50000'),(1012,'Akurdi-Branch','40000'),(1013,'Akurdi-Branch','30000'),(1014,'Akurdi-Branch','60000'),(1015,'Akurdi-Branch','52000'),(2011,'Nigdi-Branch','70000'),(2012,'Nigdi-Branch','52000'),(2013,'Nigdi-Branch','10000'),(2014,'Nigdi-Branch','11000'),(2015,'Nigdi-Branch','25000');
/*!40000 ALTER TABLE `Account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Borrower`
--

DROP TABLE IF EXISTS `Borrower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Borrower` (
  `cust_name` varchar(50) DEFAULT NULL,
  `loan_no` int(11) DEFAULT NULL,
  UNIQUE KEY `index2` (`loan_no`),
  KEY `loan_no` (`loan_no`),
  KEY `cust_name` (`cust_name`),
  CONSTRAINT `Borrower_ibfk_1` FOREIGN KEY (`loan_no`) REFERENCES `Loan` (`loan_no`),
  CONSTRAINT `Borrower_ibfk_2` FOREIGN KEY (`cust_name`) REFERENCES `Customer` (`cust_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Borrower`
--

LOCK TABLES `Borrower` WRITE;
/*!40000 ALTER TABLE `Borrower` DISABLE KEYS */;
INSERT INTO `Borrower` VALUES ('Khushal Patil',7001),('Aryan Patil',7004),('Sarthak Yere',7002),('Tejas Danane',8001),('Yash Patil',8003),('Aayush Jadhav',9001),('Dnyanesh Deore',9002),('Sumit Shelar',9004),('Nayan Bhadane',9005),('Pranav Patil',9003);
/*!40000 ALTER TABLE `Borrower` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Branch`
--

DROP TABLE IF EXISTS `Branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Branch` (
  `branch_name` varchar(25) NOT NULL,
  `branch_city` varchar(25) DEFAULT NULL,
  `assets` int(11) DEFAULT NULL,
  PRIMARY KEY (`branch_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Branch`
--

LOCK TABLES `Branch` WRITE;
/*!40000 ALTER TABLE `Branch` DISABLE KEYS */;
INSERT INTO `Branch` VALUES ('Akurdi-Branch','PCMC',100000000),('Nigdi-Branch','PCMC',300000000),('Pune-Station','Pune',700000000),('Yerwada-Branch','Pune',500000000);
/*!40000 ALTER TABLE `Branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Companies`
--

DROP TABLE IF EXISTS `Companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Companies` (
  `comp_id` varchar(10) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `cost` int(50) DEFAULT NULL,
  `year` int(10) DEFAULT NULL,
  PRIMARY KEY (`comp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Companies`
--

LOCK TABLES `Companies` WRITE;
/*!40000 ALTER TABLE `Companies` DISABLE KEYS */;
INSERT INTO `Companies` VALUES ('C001','ONGC',2000,2010),('C002','HPCL',2500,2012),('C005','IOCL',1000,2014),('C006','BHEL',3000,2015);
/*!40000 ALTER TABLE `Companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customer` (
  `cust_name` varchar(50) NOT NULL,
  `cust_street` varchar(50) DEFAULT NULL,
  `cust_city` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`cust_name`),
  KEY `index1` (`cust_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES ('Aayush Jadhav','ABC Road','Dhule'),('Abhishek Patil','LG Road','PCMC'),('Anuj Jadhav','Satara Road','PCMC'),('Aryan Patil','Katraj Road','Pune'),('Chaitnya Mitkari','Nagar Road','Pune'),('Dnyanesh Deore','MI Road','Pune'),('Gaurav Pawar','Station Road','Pune'),('Khushal Patil','MG Road','Pune'),('Nayan Bhadane','XYZ Road','Dhule'),('Pradyumna Sawkar','Tata Garden','Pune'),('Pranav Patil','ABC Road','Jalgaon'),('Prathmesh Dive','Kartaj Road','Pune'),('Rahul Patil','Karad Road','PCMC'),('Sarthak Yere','Dhayari Road','Pune'),('Sumit Shelar','PQR Road','Dhule'),('Tejas Danane','Samarth Road','Pune'),('Yash Patil','Khandoba Road','PCMC');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Depositer`
--

DROP TABLE IF EXISTS `Depositer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Depositer` (
  `cust_name` varchar(50) DEFAULT NULL,
  `Acc_no` int(11) DEFAULT NULL,
  KEY `Acc_no` (`Acc_no`),
  KEY `cust_name` (`cust_name`),
  CONSTRAINT `Depositer_ibfk_1` FOREIGN KEY (`Acc_no`) REFERENCES `Account` (`Acc_no`),
  CONSTRAINT `Depositer_ibfk_2` FOREIGN KEY (`cust_name`) REFERENCES `Customer` (`cust_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Depositer`
--

LOCK TABLES `Depositer` WRITE;
/*!40000 ALTER TABLE `Depositer` DISABLE KEYS */;
INSERT INTO `Depositer` VALUES ('Anuj Jadhav',1011),('Aryan Patil',1013),('Khushal Patil',1015),('Gaurav Pawar',2011),('Yash Patil',2013);
/*!40000 ALTER TABLE `Depositer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Loan`
--

DROP TABLE IF EXISTS `Loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Loan` (
  `loan_no` int(11) NOT NULL,
  `branch_name` varchar(25) DEFAULT NULL,
  `amount` double(7,2) DEFAULT NULL,
  PRIMARY KEY (`loan_no`),
  KEY `branch_name` (`branch_name`),
  CONSTRAINT `Loan_ibfk_1` FOREIGN KEY (`branch_name`) REFERENCES `Branch` (`branch_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Loan`
--

LOCK TABLES `Loan` WRITE;
/*!40000 ALTER TABLE `Loan` DISABLE KEYS */;
INSERT INTO `Loan` VALUES (7001,'Akurdi-Branch',15000.00),(7002,'Akurdi-Branch',1320.00),(7004,'Akurdi-Branch',6000.00),(8001,'Nigdi-Branch',77000.00),(8003,'Nigdi-Branch',50000.00),(9001,'Pune-Station',89000.00),(9002,'Pune-Station',49000.00),(9003,'Pune-Station',59000.00),(9004,'Pune-Station',62000.00),(9005,'Pune-Station',62400.00);
/*!40000 ALTER TABLE `Loan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Orders` (
  `comp_id` varchar(10) DEFAULT NULL,
  `domain` varchar(20) DEFAULT NULL,
  `quantity` int(20) DEFAULT NULL,
  KEY `comp_id` (`comp_id`),
  CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`comp_id`) REFERENCES `Companies` (`comp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--

LOCK TABLES `Orders` WRITE;
/*!40000 ALTER TABLE `Orders` DISABLE KEYS */;
INSERT INTO `Orders` VALUES ('C001','Oil',109),('C002','Gas',121),('C005','Telecom',115);
/*!40000 ALTER TABLE `Orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `View1`
--

DROP TABLE IF EXISTS `View1`;
/*!50001 DROP VIEW IF EXISTS `View1`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `View1` AS SELECT 
 1 AS `cust_name`,
 1 AS `loan_no`,
 1 AS `amount`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `View2`
--

DROP TABLE IF EXISTS `View2`;
/*!50001 DROP VIEW IF EXISTS `View2`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `View2` AS SELECT 
 1 AS `branch_name`,
 1 AS `branch_city`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `View3`
--

DROP TABLE IF EXISTS `View3`;
/*!50001 DROP VIEW IF EXISTS `View3`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `View3` AS SELECT 
 1 AS `cust_name`,
 1 AS `Acc_no`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `View1`
--

/*!50001 DROP VIEW IF EXISTS `View1`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `View1` AS select `Borrower`.`cust_name` AS `cust_name`,`Borrower`.`loan_no` AS `loan_no`,`Loan`.`amount` AS `amount` from (`Borrower` join `Loan` on((`Borrower`.`loan_no` = `Loan`.`loan_no`))) where (`Loan`.`branch_name` = 'Pune-Station') order by `Borrower`.`cust_name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `View2`
--

/*!50001 DROP VIEW IF EXISTS `View2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `View2` AS select `Branch`.`branch_name` AS `branch_name`,`Branch`.`branch_city` AS `branch_city` from `Branch` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `View3`
--

/*!50001 DROP VIEW IF EXISTS `View3`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `View3` AS select `Borrower`.`cust_name` AS `cust_name`,`Depositer`.`Acc_no` AS `Acc_no` from (`Borrower` join `Depositer`) where (`Borrower`.`cust_name` = `Depositer`.`cust_name`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-07 13:20:14
