create table tblProductCategory(
vCategoryCode varchar(5) not null primary key,
vDescription varchar(20) not null,
)

create table tblProductMaster(
vCategoryCode varchar(5) FOREIGN KEY REFERENCES tblProductCategory(vCategoryCode),
vProductId as right((convert(varchar(3),[vCategoryCode])+ '000'),3) PERSISTED NOT NULL,
vDescription varchar(20) not null,
dWater decimal(3,3) not null,
dMilk decimal(3,3) not null,
dCoffee decimal(3,3) not null,
dPieces INT not null,
dCost decimal(3,2) not null,
)

alter table tblProductMaster
add constraint PK_tblProductMaster_vProductId primary key (vProductId)

ALTER TABLE tblProductMaster
ADD CONSTRAINT DF_tblProductMaster_dPieces DEFAULT 0 FOR dPieces;

ALTER TABLE tblProductMaster ALTER COLUMN dPieces INT;

create table tblUsersOrder(
iUserId varchar(6) FOREIGN KEY REFERENCES tblUsers(iUserId),
vProductId varchar(5) FOREIGN KEY REFERENCES tblProductMaster(vProductId),
tOrderTime time(7) not null,
)

create table tblAvailableResources(
dWater decimal(3,2) not null,
dMilk decimal(3,2) not null,
dCoffee decimal(3,2) not null,
dTotalErnings decimal(3,2) not null
)

create table tblMenu(
vProductId varchar(5)  FOREIGN KEY REFERENCES tblProductMaster(vProductId),
vDescription varchar(20) not null,
dCost decimal(3,2) not null
)

SELECT * FROM tblProductCategory