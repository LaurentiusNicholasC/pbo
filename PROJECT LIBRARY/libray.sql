-- Active: 1715304964497@@127.0.0.1@3306
DROP DATABASE library_uas_pbo;
CREATE DATABASE library_uas_pbo;
    DEFAULT CHARACTER SET = 'utf8mb4';

use library_uas_pbo;

create table library(
   memberType     varchar(45) not null,
   prnNo          varchar(45) not null,
   id             varchar(45) not null,
   firstName      varchar(45),
   lastName       varchar(45),
   address1       varchar(45),
   address2       varchar(45),
   postID         varchar(45),
   mobilePhone    varchar(45),
   bookID         varchar(45),
   bookTitle      varchar(45),
   author         varchar(45),
   borrowedDate   varchar(45),
   days           varchar(45),
   dueDate        varchar(45),
   lateReturnFund varchar(45),
   overdueDate    varchar(45),
   finalPrice     varchar(45),
   primary key(prnNo)
);