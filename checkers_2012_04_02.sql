/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : checkers

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2012-04-02 13:22:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `computed_data`
-- ----------------------------
DROP TABLE IF EXISTS `computed_data`;
CREATE TABLE `computed_data` (
  `id` int(11) NOT NULL DEFAULT '0',
  `Gkn_id` int(11) DEFAULT NULL,
  `m` int(11) DEFAULT NULL,
  `list_of_failures` text,
  `timing_info` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of computed_data
-- ----------------------------

-- ----------------------------
-- Table structure for `grassmannian`
-- ----------------------------
DROP TABLE IF EXISTS `grassmannian`;
CREATE TABLE `grassmannian` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `flagvariety` text,
  `dimension` int(10) unsigned NOT NULL,
  `total_number_problems` int(10) unsigned NOT NULL,
  `number_problems` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of grassmannian
-- ----------------------------
INSERT INTO `grassmannian` VALUES ('1', 'G(2,4)', '4', '7', '[4,1], [3,3], [2,2], [1,1]');
INSERT INTO `grassmannian` VALUES ('2', 'G(2,5)', '6', '0', null);
INSERT INTO `grassmannian` VALUES ('3', 'G(2,6)', '8', '0', null);
INSERT INTO `grassmannian` VALUES ('4', 'G(2,7)', '10', '0', null);
INSERT INTO `grassmannian` VALUES ('5', 'G(2,8)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('6', 'G(2,9)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('7', 'G(2,10)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('8', 'G(2,11)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('9', 'G(2,12)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('10', 'G(2,13)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('11', 'G(2,14)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('12', 'G(3,6)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('13', 'G(3,7)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('14', 'G(3,8)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('15', 'G(3,9)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('16', 'G(3,10)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('17', 'G(3,11)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('18', 'G(3,12)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('19', 'G(3,13)', '0', '0', null);
INSERT INTO `grassmannian` VALUES ('20', 'G(3,14)', '0', '0', null);

-- ----------------------------
-- Table structure for `oracle`
-- ----------------------------
DROP TABLE IF EXISTS `oracle`;
CREATE TABLE `oracle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Gkn_id` int(11) DEFAULT NULL,
  `m` int(11) DEFAULT NULL,
  `False_failures` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of oracle
-- ----------------------------

-- ----------------------------
-- Table structure for `running_computation`
-- ----------------------------
DROP TABLE IF EXISTS `running_computation`;
CREATE TABLE `running_computation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of running_computation
-- ----------------------------

-- ----------------------------
-- Table structure for `state_of_computation`
-- ----------------------------
DROP TABLE IF EXISTS `state_of_computation`;
CREATE TABLE `state_of_computation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Gkn_id` int(11) DEFAULT NULL,
  `current_m` int(11) DEFAULT NULL,
  `current_chunk` int(11) DEFAULT NULL,
  `chunk_table` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of state_of_computation
-- ----------------------------
