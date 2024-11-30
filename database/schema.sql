-- MySQL Workbench Forward Engineering
# show databases;
# use mostafa;
show tables;
SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS, UNIQUE_CHECKS = 0;
SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS = 0;
SET @OLD_SQL_MODE = @@SQL_MODE, SQL_MODE =
        'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb`;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8;
USE `mydb`;

-- -----------------------------------------------------
-- Table `mydb`.`Account`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Account`
(
    `idAccount`   INT         NOT NULL AUTO_INCREMENT,
    `Name`        VARCHAR(45) NOT NULL,
    `Email`       VARCHAR(45) NOT NULL,
    `Password`    VARCHAR(45) NOT NULL,
    `Balance`     INT         NOT NULL DEFAULT 0,
    'AccountType' VARCHAR(45),
    PRIMARY KEY (`idAccount`),
    UNIQUE INDEX `UserId_UNIQUE` (`idAccount` ASC) VISIBLE
)
    ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`User`
(
    `idUser`            INT NOT NULL AUTO_INCREMENT,
    `Account_AccountId` INT NOT NULL,
    PRIMARY KEY (`idUser`),
    UNIQUE INDEX `UserId_UNIQUE` (`idUser` ASC) VISIBLE,
    INDEX `fk_User_Account_idx` (`Account_AccountId` ASC) VISIBLE,
    CONSTRAINT `fk_User_Account`
        FOREIGN KEY (`Account_AccountId`)
            REFERENCES `mydb`.`Account` (`idAccount`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
)
    ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Admin`
(
    `idAdmin`           INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Role`              VARCHAR(45)  NULL,
    `Account_AccountId` INT          NOT NULL,
    PRIMARY KEY (`idAdmin`),
    INDEX `fk_Admin_Account1_idx` (`Account_AccountId` ASC) VISIBLE,
    CONSTRAINT `fk_Admin_Account1`
        FOREIGN KEY (`Account_AccountId`)
            REFERENCES `mydb`.`Account` (`idAccount`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
)
    ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Product`
(
    `idProduct`     INT          NOT NULL,
    `Name`          VARCHAR(45)  NULL,
    `price`         INT          NULL,
    `Productcol`    VARCHAR(45)  NULL,
    `description`   VARCHAR(45)  NULL,
    `Productcol1`   VARCHAR(45)  NULL,
    `Admin_idAdmin` INT UNSIGNED NOT NULL,
    PRIMARY KEY (`idProduct`),
    INDEX `fk_Product_Admin1_idx` (`Admin_idAdmin` ASC) VISIBLE,
    CONSTRAINT `fk_Product_Admin1`
        FOREIGN KEY (`Admin_idAdmin`)
            REFERENCES `mydb`.`Admin` (`idAdmin`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
)
    ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Cart`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cart`
(
    `idCart`      INT NOT NULL,
    `User_idUser` INT NOT NULL,
    PRIMARY KEY (`idCart`),
    INDEX `fk_Cart_User1_idx` (`User_idUser` ASC) VISIBLE,
    CONSTRAINT `fk_Cart_User1`
        FOREIGN KEY (`User_idUser`)
            REFERENCES `mydb`.`User` (`idUser`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
)
    ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Cart_has_Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cart_has_Product`
(
    `Cart_idCart`       INT NOT NULL,
    `Product_idProduct` INT NOT NULL,
    PRIMARY KEY (`Cart_idCart`, `Product_idProduct`),
    INDEX `fk_Cart_has_Product_Product1_idx` (`Product_idProduct` ASC) VISIBLE,
    INDEX `fk_Cart_has_Product_Cart1_idx` (`Cart_idCart` ASC) VISIBLE,
    CONSTRAINT `fk_Cart_has_Product_Cart1`
        FOREIGN KEY (`Cart_idCart`)
            REFERENCES `mydb`.`Cart` (`idCart`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
    CONSTRAINT `fk_Cart_has_Product_Product1`
        FOREIGN KEY (`Product_idProduct`)
            REFERENCES `mydb`.`Product` (`idProduct`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
)
    ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Invoice`
(
    `idInvoice` INT  NOT NULL,
    `IssueDate` DATE NOT NULL,
    PRIMARY KEY (`idInvoice`)
)
    ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Invoice_has_User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Invoice_has_User`
(
    `Invoice_idInvoice` INT NOT NULL,
    `User_idUser`       INT NOT NULL,
    PRIMARY KEY (`Invoice_idInvoice`, `User_idUser`),
    INDEX `fk_Invoice_has_User_User1_idx` (`User_idUser` ASC) VISIBLE,
    INDEX `fk_Invoice_has_User_Invoice1_idx` (`Invoice_idInvoice` ASC) VISIBLE,
    CONSTRAINT `fk_Invoice_has_User_Invoice1`
        FOREIGN KEY (`Invoice_idInvoice`)
            REFERENCES `mydb`.`Invoice` (`idInvoice`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
    CONSTRAINT `fk_Invoice_has_User_User1`
        FOREIGN KEY (`User_idUser`)
            REFERENCES `mydb`.`User` (`idUser`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
)
    ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Invoice_has_Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Invoice_has_Product`
(
    `Invoice_idInvoice` INT NOT NULL,
    `Product_idProduct` INT NOT NULL,
    PRIMARY KEY (`Invoice_idInvoice`, `Product_idProduct`),
    INDEX `fk_Invoice_has_Product_Product1_idx` (`Product_idProduct` ASC) VISIBLE,
    INDEX `fk_Invoice_has_Product_Invoice1_idx` (`Invoice_idInvoice` ASC) VISIBLE,
    CONSTRAINT `fk_Invoice_has_Product_Invoice1`
        FOREIGN KEY (`Invoice_idInvoice`)
            REFERENCES `mydb`.`Invoice` (`idInvoice`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
    CONSTRAINT `fk_Invoice_has_Product_Product1`
        FOREIGN KEY (`Product_idProduct`)
            REFERENCES `mydb`.`Product` (`idProduct`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
)
    ENGINE = InnoDB;


SET SQL_MODE = @OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS = @OLD_UNIQUE_CHECKS;
