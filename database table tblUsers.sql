--create database vending_machine

--- Creating a table for users ---
create table tblUsers (
iId int identity(1, 1) Not Null,
iUserId AS ('VM-' + right(('000' + convert(varchar(3),[iId])),3)) PERSISTED NOT NULL ,
vUserName varchar(50) not null,
vPassword nvarchar(8) not null
)

--- Adding check constraint for special characters for vPassword column in tblUsers table ---
alter table tblUsers 
add constraint ck_only_Special_Characters 
check (vPassword not LIKE '%[^A-Z0-9]%') 

--- Inserting Data into the tblUsers table ---
insert into tblUsers values('Vaibhav','Creed96'), ('Sahil','Sahils20'), ('Seema','SeemaSur')

select * from tblUsers

alter table tblUsers
add constraint PK_tblUsers_iUserId primary key (iUserId)

alter table tblUsers
add vRole varchar(10) default 'USER'

