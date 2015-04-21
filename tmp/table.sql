drop table if exists t_user;
create table t_user (
    id integer primary key autoincrement,
    name text not null,
    email text not null,
	password text not null,
	regdt text not null
);


drop table if exists t_order;
create table t_order (
    id integer primary key autoincrement,
    title text not null,
    status integer,
    create_user text not null,
	create_dt text not null,
	category text not null,
	type text,
	item text,
	limit_price real,
	limit_weight real,
	kickoff_dt text not null,
	update_dt text not null
);