------------------- DATABASE CREATION ---------------------------

create database vending_machine

-------------------------------------------------------------------------------
------------------- DATA TABLES CREATION ------------------------

--- Users ---
create table tblUsers (
iId int identity,
vUserId AS ('VM-' + convert(varchar(3),[iId])) PERSISTED NOT NULL PRIMARY KEY,
vUserName varchar(50) NOT NULL,
vPassword nvarchar(10) NOT NULL CHECK (vPassword not LIKE '%[^A-Z0-9]%'),
vRole varchar(10) DEFAULT 'USER'
);

--- Product Category ---
create table tblProductCategory(
vCategoryCode varchar(5) NOT NULL primary key,
vDescription varchar(20) NOT NULL,
);

--- Product Master ---
create table tblProductMaster(
iID int IDENTITY(1, 1),
vCategoryCode varchar(5) FOREIGN KEY REFERENCES tblProductCategory(vCategoryCode),
vProductId as ([vCategoryCode] + '-' + Convert(varchar(3), iID)) PERSISTED NOT NULL PRIMARY KEY,
vDescription varchar(20) NOT NULL,
dWater decimal(9,2) DEFAULT 0.00,
dMilk decimal(9,2) DEFAULT 0.00,
dCoffee decimal(9,2) DEFAULT 0.00,
dPieces INT DEFAULT 0,
dCost decimal(10,2) DEFAULT 0.00,
);

--- User Orders ---
create table tblUserOrders(
iID INT IDENTITY PRIMARY KEY,
vUserId varchar(6) FOREIGN KEY REFERENCES tblUsers(vUserId),
vProductId varchar(9) FOREIGN KEY REFERENCES tblProductMaster(vProductId),
tOrderDate datetime DEFAULT CURRENT_TIMESTAMP,
);

--- Available Resources ---
create table tblAvailableResources(
iID INT IDENTITY PRIMARY KEY,
iMonth INT NOT NULL,
iWeek INT NOT NULL,
dWater decimal(9,2) DEFAULT 0.00,
dMilk decimal(9,2) DEFAULT 0.00,
dCoffee decimal(9,2) DEFAULT 0.00,
dTotalErnings decimal(10,2) DEFAULT 0.00
);

--- Menu ---
create table tblMenu(
iID INT IDENTITY PRIMARY KEY,
vProductId varchar(9) FOREIGN KEY REFERENCES tblProductMaster(vProductId),
dCost decimal(10,2) DEFAULT 0.00
);


----------------------------------------------------------------------------------------
--- INDEXES OF ABOVE TABLES ---

CREATE UNIQUE INDEX idx_Users
ON tblUsers (vUserId);

CREATE UNIQUE INDEX idx_Category
ON tblProductCategory (vCategoryCode);

CREATE UNIQUE INDEX idx_Product
ON tblProductMaster (vProductId);

CREATE INDEX idx_Orders
ON tblUserOrders (vUserId, vProductId);

CREATE UNIQUE INDEX idx_Resources
ON tblAvailableResources (iMonth, iWeek);

CREATE UNIQUE INDEX idx_Menu
ON tblMenu (iID);
