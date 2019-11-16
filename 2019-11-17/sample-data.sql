-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 16, 2019 at 07:52 PM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `class_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `id` int(11) NOT NULL,
  `name` varchar(64) DEFAULT NULL,
  `birth` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `name`, `birth`) VALUES
(1, 'Aaaaa', '2009-04-10'),
(2, 'Bbbbb', '1980-08-08');

-- --------------------------------------------------------

--
-- Table structure for table `edu`
--

DROP TABLE IF EXISTS `edu`;
CREATE TABLE IF NOT EXISTS `edu` (
  `id` int(11) NOT NULL,
  `begin` int(11) DEFAULT NULL,
  `end` int(11) DEFAULT NULL,
  `name` mediumtext,
  `customer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `phone`
--

DROP TABLE IF EXISTS `phone`;
CREATE TABLE IF NOT EXISTS `phone` (
  `id` int(11) NOT NULL,
  `type` varchar(64) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `phone`
--

INSERT INTO `phone` (`id`, `type`, `number`, `customer_id`) VALUES
(1, 'ger', 3232, 1),
(2, 'gar', 88888, 1);

-- --------------------------------------------------------

--
-- Table structure for table `relative`
--

DROP TABLE IF EXISTS `relative`;
CREATE TABLE IF NOT EXISTS `relative` (
  `id` int(11) NOT NULL,
  `customer_id_1` int(11) DEFAULT NULL,
  `customer_id_2` int(11) DEFAULT NULL,
  `type` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `relative`
--

INSERT INTO `relative` (`id`, `customer_id_1`, `customer_id_2`, `type`) VALUES
(1, 1, 2, 'huuhed'),
(2, 2, 1, 'aav');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
