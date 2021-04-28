-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 28, 2021 at 05:38 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_mahasiswa`
--

CREATE TABLE `data_mahasiswa` (
  `nama` varchar(255) NOT NULL,
  `nim` int(100) NOT NULL,
  `alamat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data_mahasiswa`
--

INSERT INTO `data_mahasiswa` (`nama`, `nim`, `alamat`) VALUES
('Angga Jiyan Fajar', 1230001, 'Sidoarjo, Jawa Timur'),
('Muhammad Tegar', 1230002, 'Surabaya, Jawa Timur'),
('Budi Yanto Nugroho', 1230003, 'Gresik, Jawa Timur'),
('Fajar Chandra', 1230005, 'Semarang, Jawa Timur'),
('Rudy Mulyanto', 1230006, 'Semarang, Jawa Timur'),
('Rayhan Rizal', 1230007, 'Malang, Jawa Timur'),
('Faris Syaifulloh', 1230008, 'Bogor, Jawa Barat'),
('Rizqy Khoirul', 1230009, 'Sidoarjo, Jawa Timur'),
('Rizky Ramadhan', 1230009, 'Kediri, Jawa Timur');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
