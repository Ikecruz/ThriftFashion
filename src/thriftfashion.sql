-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 14, 2022 at 01:17 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `thriftfashion`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `email` varchar(80) NOT NULL,
  `username` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL,
  `join_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `email`, `username`, `password`, `join_date`) VALUES
(1, 'onyiboixy@gmail.com', 'admin', '$5$rounds=535000$GfnvcjP3t1e95pcF$TXeJM442ap8GeFnPn9ujor48wOtWNmtbj4lGP3dfYt1', '2022-08-13 06:18:04');

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('e0b14078a0c2');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `id` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `price` decimal(10,0) NOT NULL,
  `quantity` decimal(10,0) NOT NULL,
  `date_added` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`id`, `product_id`, `user_id`, `price`, `quantity`, `date_added`) VALUES
(1, 1, 1, '30', '1', '2022-08-14 10:32:31');

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`) VALUES
(1, 'Hats'),
(2, 'Shoes'),
(3, 'TShirt');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `email` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `number` varchar(45) NOT NULL,
  `message` varchar(100) NOT NULL,
  `date_added` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `total` decimal(10,0) NOT NULL,
  `quantity` decimal(10,0) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `date_added` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `price` decimal(10,0) DEFAULT NULL,
  `img_url` varchar(80) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `qty` int(11) NOT NULL,
  `date_added` datetime NOT NULL,
  `description` varchar(60) NOT NULL,
  `gender` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `price`, `img_url`, `category_id`, `qty`, `date_added`, `description`, `gender`) VALUES
(1, 'The North Face Sun Stash bucket hat in navy/ blue', '30', '2022-08-14v873640mt7fazbjk5l0iwc76o5vfzf.png', 1, 19, '2022-08-14 06:38:11', 'Founded by a pair of hiking enthusiasts, outdoor clothing an', 'Women'),
(2, 'The North Face Cypress bucket hat in black', '20', '2022-08-14uf1x71bxqvrfxzcjszzdb4d99ftien.png', 1, 30, '2022-08-14 06:40:31', 'Smooth woven fabric\r\nUses The North Face FlashDry technology', 'Women'),
(3, 'ASOS 4505 bucket hat', '20', '2022-08-142s18fpkcefoa1nrblfjuerut39zjzu.png', 1, 50, '2022-08-14 06:42:22', 'Whether you’re gaining, training or exploring the great outd', 'Women'),
(4, 'Nike utility graphic logo boyfriend t-shirt in cel', '32', '2022-08-14ssyv1z56d0feuo955t8x15lmh3bcu4.png', 3, 20, '2022-08-14 07:03:44', 'Key players in everything activewear-related, it doesn’t get', 'Women'),
(5, 'Nike Essential mini swoosh boyfriend t-shirt in ma', '30', '2022-08-14i8u8i6x64jzqcp2dq5dwimy7lhn1ti.png', 3, 30, '2022-08-14 07:06:03', 'Key players in everything activewear-related, it doesn’t get', 'Women'),
(6, 'Nike unisex retro collegiate t-shirt in navy', '20', '2022-08-14hs8wh6nqw52n0fyqwyr3g4kr6m4reb.png', 3, 30, '2022-08-14 07:08:44', 'Key players in everything activewear-related, it doesn’t get', 'Women'),
(7, 'ASOS DESIGN oversized t-shirt in black cotton blen', '30', '2022-08-14ktn89esk16pd1totxdksh2e3usj1tr.png', 3, 40, '2022-08-14 12:14:36', 'ASOS DESIGN oversized t-shirt in black cotton blend with Chi', 'Men'),
(8, ' Carhartt WIP backley 7 panel cap', '37', '2022-08-14j0xa8qq796r0iohjyj8ag2qbrokrld.png', 1, 100, '2022-08-14 12:16:09', 'The youngest child of the Carhartt family, Carhartt WIP laun', 'Men');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(80) NOT NULL,
  `name` varchar(80) NOT NULL,
  `number` varchar(80) NOT NULL,
  `username` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL,
  `token` varchar(80) NOT NULL,
  `email_verified` tinyint(1) NOT NULL,
  `join_date` datetime DEFAULT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `name`, `number`, `username`, `password`, `token`, `email_verified`, `join_date`, `status`) VALUES
(1, 'dracoglocky@gmail.com', 'Draco Glocl', '+2348164482268', 'DOTE', '$5$rounds=535000$TE2I0gOVobItrbRK$D16FGByDpUMDIAtLaL6edNkaRscvka.fw6PiGlYwxt3', '547496', 1, '2022-08-14 10:23:06', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_id` (`product_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cart`
--
ALTER TABLE `cart`
  ADD CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  ADD CONSTRAINT `cart_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
