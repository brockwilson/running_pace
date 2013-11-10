drop table if exists entries;
create table entries (
       id integer primary key autoincrement,
       date text not null,
       duration integer not null,
       distance real not null
);
