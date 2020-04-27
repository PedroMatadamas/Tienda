#Create the DB
CREATE DATABASE IF NOT EXISTS store_db;

#Select the database to work with
use store_db;

#Create the kernel tables: zips, client and products
CREATE TABLE IF NOT EXISTS zips(
	zip varchar(6) not null,
    z_city varchar(35) not null,
    z_state varchar(35) not null,
    primary key(zip)
)engine = InnoDB;

create table if not exists clients(
	id_client int not null auto_increment,
    c_fname varchar(35) not null,
    c_sname1 varchar(35) not null,
    c_sname2 varchar(35),
    c_street varchar(35) not null,
    c_noext varchar(7) not null,
    c_noint varchar(7),
    c_col varchar(50),
    c_zip varchar(6),
    c_email varchar(20),
    c_phone varchar(13),
    primary key(id_client),
    constraint fkzip_clients foreign key(c_zip)
		references zips(zip)
        on delete set null
        on update cascade
)engine = InnoDB;

create table if not exists products(
	id_product int not null auto_increment,
    p_name varchar(35) not null,
    p_brand varchar(35) not null,
    p_descrip varchar(250),
    p_price float not null,
    primary key(id_product)
)engine = InnoDB;


#Create the dependent tables: order and order details
create table if not exists orders(
	id_order int not null auto_increment,
    id_client int,
    o_status enum('PROCESSING', 'ACEPTED', 'SENT', 'RECEIVED') not null,
    o_date date not null, #Since MYSQL deals directly with dates
    o_total float not null,
    primary key(id_order),
    constraint fkclient_orders foreign key(id_client)
		references clients(id_client)
        on delete cascade
        on update cascade
)engine = InnoDB;


create table if not exists order_details(
	id_order int not null,
    id_product int not null,
    od_amount int not null,
    od_total float not null,
    primary key(id_order, id_product),
    constraint fkorder_ods foreign key(id_order)
		references orders(id_order)
        on delete cascade
        on update cascade,
	constraint fkproduct_ods foreign key(id_product)
		references products(id_product)
        on delete cascade
        on update cascade
)engine = InnoDB;
