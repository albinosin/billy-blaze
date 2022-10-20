create database billy_blaze;

use billy_blaze;

CREATE TABLE billy_blaze.double_colors (
	id INT NOT NULL,
	char_name varchar(100) NOT NULL,
	PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;

CREATE TABLE billy_blaze.`double_data` (
	id INT auto_increment NOT NULL,
	fk_int_id_color INT NOT NULL,
	number_spin INT NOT NULL,
	dec_black DECIMAL(20,2) NULL,
	dec_red DECIMAL(20,2) NULL,
	dec_white DECIMAL(20,2) NULL,
	dt_spin DATETIME NULL,
	PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;



insert into billy_blaze.double_colors values(1, "Black");
insert into billy_blaze.double_colors values(2, "Red");
insert into billy_blaze.double_colors values(3, "White");
insert into billy_blaze.double_colors values(4, "Maintenance");

CREATE TABLE billy_blaze.double_sequence (
	id INT auto_increment NULL,
	fk_int_id_color INT NOT NULL,
	int_count_color INT NOT NULL,
	dt_spin DATETIME NOT NULL,
	CONSTRAINT double_sequence_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;
