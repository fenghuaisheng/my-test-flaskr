drop table if exists users;
create table users (
  id integer primary key autoincrement,
  name text not null,
  email text not null,
  password text not null
);

drop table if exists posts;
create table posts (
  id integer primary key autoincrement,
  userid integer,
  title text not null,
  content text not null,
  foreign key(userid) references users(id)
);
