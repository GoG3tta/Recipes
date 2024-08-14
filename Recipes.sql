-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema recipe_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `recipe_schema` ;

-- -----------------------------------------------------
-- Schema recipe_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `recipe_schema` DEFAULT CHARACTER SET utf8 ;
USE `recipe_schema` ;

-- -----------------------------------------------------
-- Table `recipe_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipe_schema`.`recipe`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipe_schema`.`recipe` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `recipe_name` VARCHAR(255) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `instructions` VARCHAR(255) NOT NULL,
  `date_cooked` DATE NOT NULL,
  `under_30` TINYINT NOT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`, `user_id`),
  INDEX `fk_add_recipe_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_add_recipe_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `recipe_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
