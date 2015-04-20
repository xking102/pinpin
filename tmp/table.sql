drop table if exists t_user;
create table t_user (
    id integer primary key autoincrement,
    name text not null,
    email text not null,
	password text not null
);