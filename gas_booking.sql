-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 14, 2021 at 09:02 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gas_booking`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `book_id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`book_id`, `customer_id`, `date`, `status`) VALUES
(1, 1, '2021-04-03', 'DELIVERED'),
(2, 1, '2021-04-03', 'DELIVERED'),
(3, 8, '2021-04-07', 'DELIVERED'),
(4, 8, '2021-04-09', 'DELIVERED'),
(5, 9, '2021-04-14', 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `date_time` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`complaint_id`, `customer_id`, `complaint`, `reply`, `date_time`) VALUES
(1, 1, 'login error', 'we will consider that', '12-10-2020'),
(2, 1, 'Animi aut molestiae', 'OKAY', '2021-04-02'),
(3, 1, 'efasdfs', 'pending', '2021-04-02'),
(4, 1, 'efasdfs', 'pending', '2021-04-02');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `adhaar_no` varchar(50) DEFAULT NULL,
  `cus_fname` varchar(50) DEFAULT NULL,
  `cus_lname` varchar(50) DEFAULT NULL,
  `cus_hname` varchar(50) DEFAULT NULL,
  `cus_city` varchar(50) DEFAULT NULL,
  `cus_district` varchar(50) DEFAULT NULL,
  `cus_state` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `cus_phno` varchar(50) DEFAULT NULL,
  `c_status` varchar(50) DEFAULT NULL,
  `proof_of_address` varchar(500) DEFAULT NULL,
  `proof_of_identity` varchar(500) DEFAULT NULL,
  `cat_id` int(11) DEFAULT NULL,
  `connection_type` varchar(50) DEFAULT NULL,
  `delivery_charge` varchar(50) DEFAULT NULL,
  `cylin_inhand` varchar(50) DEFAULT NULL,
  `install_status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `username`, `adhaar_no`, `cus_fname`, `cus_lname`, `cus_hname`, `cus_city`, `cus_district`, `cus_state`, `pincode`, `cus_phno`, `c_status`, `proof_of_address`, `proof_of_identity`, `cat_id`, `connection_type`, `delivery_charge`, `cylin_inhand`, `install_status`) VALUES
(1, 'customer', '123456789098', 'sachin', 't', 'mrf', 'mumbai', 'district', 'maharashtra', '673008', '9087654321', 'approved', 'static/images/fb5d8769-a9e8-43ac-bbe6-bdf7b7b2043aScreenshot (1).png', 'static/images/7c689744-bffc-445d-bfb6-9ddd26939927Screenshot (2).png', 1, 'Double Bottle', '12', '2', 'installed'),
(2, 'customer1', '098765432112', 'virat', 'k', 'abc', 'banglore', 'district2', 'karnataka', '983456', '9087654321', 'approved', NULL, NULL, 1, 'Single Bottle', '13', '1', 'pending'),
(7, 'sheela@gmail.com', '151236548956', 'Sheela', 'Thomas', 'ABC', 'Ernakulam', 'Ernakulam', 'Kerala', '688593', '9856234458', 'pending', 'static/images/b1146039-5966-4832-95a1-a9c9c0396ddcdownload (3).jfif', 'static/images/fb9b7233-8bce-42c7-b4d3-48b4bb79f134download (3).jfif', 1, 'Single Bottle', '0', '0', 'installed'),
(8, 'agponnezhath999@gmail.com', '223456789012', 'DSS', 'DESD', 'FDSF', 'Cherthala', 'EDWEF', 'Kerala', '688524', '09495597532', 'approved', 'static/images/8a0cab60-76eb-4d53-8f40-2f7f84c102b7download (3).jfif', 'static/images/290f4f3b-fd98-4a01-b5f3-4e25082b1b14images.jfif', 1, 'Single Bottle', '0', '2', 'installed'),
(9, 'ganga@gmail.com', '789654123654', 'Ganga', 'N', 'poiuy', 'Ernakulam', 'Ernakulam', 'Kerala', '688953', '9874662254', 'approved', 'static/images/60c93797-a089-40a0-9059-4a6c6cc0f71aScreenshot (29).png', 'static/images/f996f284-5522-4e05-a8a3-883bf256213aScreenshot (35).png', 7, '2', '0', '1', 'installed');

-- --------------------------------------------------------

--
-- Table structure for table `cus_service`
--

CREATE TABLE `cus_service` (
  `cus_service_id` int(11) NOT NULL,
  `service_book_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `service_remarks` varchar(50) DEFAULT NULL,
  `service_date` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cus_service`
--

INSERT INTO `cus_service` (`cus_service_id`, `service_book_id`, `staff_id`, `service_remarks`, `service_date`) VALUES
(1, 1, 3, 'connection problem', '2021-04-02 10:37:36'),
(2, 1, 3, 'connection problem', '2021-04-02 10:38:09'),
(3, 2, 3, 'connection problem', '2021-04-03'),
(4, 2, 3, 'connection problem', '2021-04-03'),
(5, 3, 5, 'WILL BE COMPLETED SOON', '2021-04-07');

-- --------------------------------------------------------

--
-- Table structure for table `cylinder_category`
--

CREATE TABLE `cylinder_category` (
  `cat_id` int(11) NOT NULL,
  `cat_weight` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cylinder_category`
--

INSERT INTO `cylinder_category` (`cat_id`, `cat_weight`, `price`) VALUES
(1, '5 KG', '760'),
(7, '14.2 KG', '900'),
(11, '19 KG', '1000'),
(12, '2 KG', '500');

-- --------------------------------------------------------

--
-- Table structure for table `delivery`
--

CREATE TABLE `delivery` (
  `delivery_id` int(11) NOT NULL,
  `book_id` int(11) DEFAULT NULL,
  `vehicle_regno` varchar(50) DEFAULT NULL,
  `delivery_date` varchar(50) DEFAULT NULL,
  `delivery_status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `delivery`
--

INSERT INTO `delivery` (`delivery_id`, `book_id`, `vehicle_regno`, `delivery_date`, `delivery_status`) VALUES
(6, 1, 'kl 11 bs 1891', '2021-04-03', 'vehicle_assigned'),
(7, 2, 'kl 11 bs 1891', '2021-04-07', 'delivered'),
(8, 3, 'KL 12 QQ 1990', '2021-04-08', 'vehicle_assigned'),
(9, 4, 'KL 12 QQ 1990', '2021-04-09', 'vehicle_assigned');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `usertype`) VALUES
('abc@gmail.com', 'Abc@123', 'removed'),
('achu@gmail.com', 'Achu@123', 'staff'),
('admin', 'admin', 'admin'),
('agponnezhath999@gmail.com', 'ZSFDSFq12', 'customer'),
('aleena@gmail.com', 'Aleena@123', 'staff'),
('customer', 'customer', 'customer'),
('ganga@gmail.com', 'Ganga@123', 'customer'),
('Koshi@gmail.com', 'Koshi@123', 'staff'),
('sheela@gmail.com', 'Sheela@123', 'customer');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `pay_id` int(11) NOT NULL,
  `booked_id` int(11) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`pay_id`, `booked_id`, `amount`, `type`, `date`) VALUES
(3, 1, '759', 'booking', '2021-04-02'),
(4, 1, '282', 'service', '2021-04-03'),
(5, 2, '759', 'booking', '2021-04-03'),
(6, 3, '759', 'booking', '2021-04-07'),
(7, 3, '282', 'service', '2021-04-07'),
(8, 4, '759', 'booking', '2021-04-09'),
(9, 5, '900', 'booking', '2021-04-14');

-- --------------------------------------------------------

--
-- Table structure for table `service`
--

CREATE TABLE `service` (
  `service_id` int(11) NOT NULL,
  `service_type` varchar(50) DEFAULT NULL,
  `charge` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `service`
--

INSERT INTO `service` (`service_id`, `service_type`, `charge`) VALUES
(1, 'New Connection and demo', '282'),
(3, 'Special Inspection', '1500'),
(6, 'ABC', '504'),
(7, 'Annual Inspection', '900');

-- --------------------------------------------------------

--
-- Table structure for table `service_booking`
--

CREATE TABLE `service_booking` (
  `service_book_id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  `remarks` varchar(50) DEFAULT NULL,
  `request_date` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `service_booking`
--

INSERT INTO `service_booking` (`service_book_id`, `customer_id`, `service_id`, `remarks`, `request_date`) VALUES
(1, 1, 1, 'paid', '12-10-2021'),
(2, 1, 3, 'accepted', '2021-04-03'),
(3, 8, 1, 'paid', '2021-04-07'),
(4, 8, 1, 'accepted', '2021-04-08'),
(5, 8, 6, 'approved', '2021-04-09'),
(6, 9, 7, 'approved', '2021-04-14');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `staff_fname` varchar(50) DEFAULT NULL,
  `staff_lname` varchar(50) DEFAULT NULL,
  `staff_dob` varchar(50) DEFAULT NULL,
  `staff_hname` varchar(50) DEFAULT NULL,
  `staff_city` varchar(50) DEFAULT NULL,
  `staff_district` varchar(50) DEFAULT NULL,
  `staff_state` varchar(50) DEFAULT NULL,
  `staff_pincode` varchar(50) DEFAULT NULL,
  `staff_phno` varchar(50) DEFAULT NULL,
  `staff_des` varchar(50) DEFAULT NULL,
  `staff_doj` varchar(50) DEFAULT NULL,
  `s_status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staff_id`, `username`, `staff_fname`, `staff_lname`, `staff_dob`, `staff_hname`, `staff_city`, `staff_district`, `staff_state`, `staff_pincode`, `staff_phno`, `staff_des`, `staff_doj`, `s_status`) VALUES
(3, 'ThaneMoran@gmail.com', 'Thane', 'Moran', '1982-05-26', 'Kelsey Odom', 'Alappuzha', 'Alappuzha', 'Kerla', '699583', '9087654355', 'Driver', '2021-03-30 23:57:26', 'expired'),
(5, 'Koshi@gmail.com', 'Koshi', 'P', '2021-04-06', 'poiuy', 'Ernakulam', 'Ernakulam', 'Kerala', '688593', '9685336675', 'Staff', '2021-04-07 10:40:31', 'approved'),
(7, 'abc@gmail.com', 'ABC', 'rty', '1991-02-05', 'poi', 'Ernakulam', 'Ernakulam', 'Kerala', '688555', '9856234562', 'Staff', '2021-04-09 11:07:44', 'expired'),
(8, 'aleena@gmail.com', 'Aleena', 'RTYUI', '1990-02-13', 'POIJKMG', 'Ernakulam', 'Ernakulam', 'Kerala', '688953', '9685996541', 'Driver', '2021-04-13 14:27:16', 'approved'),
(9, 'achu@gmail.com', 'Achu', 'rty', '1993-02-02', 'poi', 'Ernakulam', 'Ernakulam', 'Kerala', '688593', '9856234562', 'Driver', '2021-04-14 13:31:46', 'approved');

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--

CREATE TABLE `stock` (
  `stock_id` int(11) NOT NULL,
  `stock_date` varchar(50) DEFAULT NULL,
  `stock_type` varchar(50) DEFAULT NULL,
  `cat_id` int(11) DEFAULT NULL,
  `no_of_cylin` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stock`
--

INSERT INTO `stock` (`stock_id`, `stock_date`, `stock_type`, `cat_id`, `no_of_cylin`) VALUES
(1, '2021-04-08', 'Full', 1, '1043'),
(2, '2021-04-02', 'Empty', 1, '1030'),
(3, '2021-04-07', 'Full', 7, '1000'),
(4, '2021-04-04', 'Empty', 7, '5'),
(9, '2021-04-07', 'Full', 8, '5'),
(10, '2021-04-07', 'Empty', 8, '2'),
(11, '2021-04-14', 'Full', 11, '50'),
(12, '2021-04-14', 'Empty', 11, '20'),
(13, '2021-04-07', 'Damaged', 11, '0'),
(14, '2021-04-13', 'Damaged', 1, '9'),
(15, '2021-04-02', 'Damaged', 7, '1'),
(16, '2021-04-09', 'Full', 12, '50'),
(17, '2021-04-13', 'Empty', 12, '5'),
(18, '2021-04-09', 'Damaged', 12, '0');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle`
--

CREATE TABLE `vehicle` (
  `vehicle_regno` varchar(50) NOT NULL,
  `vehicle_type` varchar(50) DEFAULT NULL,
  `vehicle_status` varchar(50) DEFAULT NULL,
  `V_Status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicle`
--

INSERT INTO `vehicle` (`vehicle_regno`, `vehicle_type`, `vehicle_status`, `V_Status`) VALUES
('kl 11 bs 1891', 'Ape', 'assigned', 'removed'),
('KL 12 QQ 1990', 'Ape', 'free', 'approved'),
('KL 32 N 5995', 'Ape', 'free', 'approved');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `complaint`
--
ALTER TABLE `complaint`
  ADD PRIMARY KEY (`complaint_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `adhaar_no` (`adhaar_no`);

--
-- Indexes for table `cus_service`
--
ALTER TABLE `cus_service`
  ADD PRIMARY KEY (`cus_service_id`);

--
-- Indexes for table `cylinder_category`
--
ALTER TABLE `cylinder_category`
  ADD PRIMARY KEY (`cat_id`),
  ADD UNIQUE KEY `cat_weight` (`cat_weight`);

--
-- Indexes for table `delivery`
--
ALTER TABLE `delivery`
  ADD PRIMARY KEY (`delivery_id`),
  ADD UNIQUE KEY `book_id` (`book_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`pay_id`);

--
-- Indexes for table `service`
--
ALTER TABLE `service`
  ADD PRIMARY KEY (`service_id`);

--
-- Indexes for table `service_booking`
--
ALTER TABLE `service_booking`
  ADD PRIMARY KEY (`service_book_id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`staff_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`stock_id`);

--
-- Indexes for table `vehicle`
--
ALTER TABLE `vehicle`
  ADD PRIMARY KEY (`vehicle_regno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `complaint`
--
ALTER TABLE `complaint`
  MODIFY `complaint_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `cus_service`
--
ALTER TABLE `cus_service`
  MODIFY `cus_service_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `cylinder_category`
--
ALTER TABLE `cylinder_category`
  MODIFY `cat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `delivery`
--
ALTER TABLE `delivery`
  MODIFY `delivery_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `pay_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `service`
--
ALTER TABLE `service`
  MODIFY `service_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `service_booking`
--
ALTER TABLE `service_booking`
  MODIFY `service_book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `staff_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `stock`
--
ALTER TABLE `stock`
  MODIFY `stock_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
