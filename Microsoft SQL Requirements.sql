use charles_mohlaka;


-- PayslipItemCodes Table
CREATE TABLE PayslipItemCodes (
    PayslipItemCode varchar(4) NOT NULL PRIMARY KEY
);

-- PayslipItemCodes Audit Table
CREATE TABLE PayslipItemCodesAudit (
    PayslipItemCodeAuditID INT IDENTITY(1,1) PRIMARY KEY,
    PayslipItemCode varchar(4),
    UpdatedBy nvarchar(128),
    UpdatedOn datetime
)

-- PayslipItemCodes Audit Trigger
CREATE TRIGGER PayslipItemCodesAuditTrig ON PayslipItemCodes 
FOR INSERT, UPDATE
AS
	declare @payslipitemcode varchar(4);
	declare @updatedby nvarchar(128);
	declare @updatedon datetime;

	select @payslipitemcode=i.PayslipItemCode from inserted i;

	insert into PayslipItemCodesAudit
           (PayslipItemCode,UpdatedBy,UpdatedOn) 
	values(@payslipitemcode,SUSER_SNAME(),getdate());
GO






-- employeeDetails Table
CREATE TABLE employeeDetails (
    EmployerID int NOT NULL,
    EmployeeNumber int NOT NULL,
    EmployeeLastName varchar(255) NOT NULL,
    EmployeeFirstName varchar(255) NOT NULL,
    EmployeeDoB date NOT NULL,
    PayslipItemCode varchar(4) NOT NULL,
    PayslipItemDescription varchar(255) NOT NULL,
    PayslipItemAmount DECIMAL,
    EmployeeTerminated bit NOT NULL
    CONSTRAINT PK_Employee PRIMARY KEY (EmployeeNumber,PayslipItemCode)
);


-- employeeDetails Audit Table
CREATE TABLE employeeDetailsAudit (
    employeeDetailAuditID INT IDENTITY(1,1) PRIMARY KEY,
    EmployerID int,
    EmployeeNumber int,
    EmployeeLastName varchar(255),
    EmployeeFirstName varchar(255),
    EmployeeDoB date,
    PayslipItemCode varchar(4),
    PayslipItemDescription varchar(255),
    PayslipItemAmount DECIMAL,
    EmployeeTerminated bit,
    UpdatedBy nvarchar(128),
    UpdatedOn datetime
)

-- employeeDetails Audit Trigger
CREATE TRIGGER employeeDetailsAuditTrig ON employeeDetails 
FOR INSERT, UPDATE
AS
	declare @employerid int;
    declare @employeenumber int;
    declare @employeelastname varchar(255);
    declare @employeefirstname varchar(255);
    declare @dmployeedob date;
    declare @payslipitemcode varchar(4);
    declare @payslipitemdescription varchar(255);
    declare @payslipitemamount DECIMAL;
    declare @employeeterminated bit;
	declare @updatedby nvarchar(128);
	declare @updatedon datetime;

	select @employerid=i.EmployerID from inserted i;
    select @employeenumber=i.EmployeeNumber from inserted i;
    select @employeelastname=i.EmployeeLastName from inserted i;
    select @employeefirstname=i.EmployeeFirstName from inserted i;
    select @dmployeedob=i.EmployeeDoB from inserted i;
    select @payslipitemcode=i.PayslipItemCode from inserted i;
    select @payslipitemdescription=i.PayslipItemDescription from inserted i;
    select @payslipitemamount=i.PayslipItemAmount from inserted i;
    select @employeeterminated=i.EmployeeTerminated from inserted i;

	insert into employeeDetailsAudit
           (EmployerID,EmployeeNumber,EmployeeLastName,EmployeeFirstName,EmployeeDoB,PayslipItemCode,PayslipItemDescription,PayslipItemAmount,EmployeeTerminated,UpdatedBy,UpdatedOn) 
	values(@employerid,@employeenumber,@employeelastname,@employeefirstname,@dmployeedob,@payslipitemcode,@payslipitemdescription,@payslipitemamount,@employeeterminated,SUSER_SNAME(),getdate());
GO




-- IncomePayslipItems Table
CREATE TABLE IncomePayslipItems (
    IncomePayslipItem varchar(4) NOT NULL PRIMARY KEY,
    FOREIGN KEY(IncomePayslipItem) REFERENCES PayslipItemCodes(PayslipItemCode)
);


-- IncomePayslipItems Audit Table
CREATE TABLE IncomePayslipItemsAudit (
    IncomePayslipItemAuditID INT IDENTITY(1,1) PRIMARY KEY,
    IncomePayslipItem varchar(4),
    UpdatedBy nvarchar(128),
    UpdatedOn datetime
)

-- IncomePayslipItems Audit Trigger
CREATE TRIGGER IncomePayslipItemsAuditTrig ON IncomePayslipItems 
FOR INSERT, UPDATE
AS
	declare @incomepayslipitem varchar(4);
	declare @updatedby nvarchar(128);
	declare @updatedon datetime;

	select @incomepayslipitem=i.IncomePayslipItem from inserted i;

	insert into IncomePayslipItemsAudit
           (IncomePayslipItem,UpdatedBy,UpdatedOn) 
	values(@incomepayslipitem,SUSER_SNAME(),getdate());
GO


-- ExpensePayslipItems Table
CREATE TABLE ExpensePayslipItems (
    ExpensePayslipItem varchar(4) NOT NULL PRIMARY KEY,
    FOREIGN KEY(ExpensePayslipItem) REFERENCES PayslipItemCodes(PayslipItemCode)
);

-- ExpensePayslipItems Audit Table
CREATE TABLE ExpensePayslipItemsAudit (
    ExpensePayslipItemAuditID INT IDENTITY(1,1) PRIMARY KEY,
    ExpensePayslipItem varchar(4),
    UpdatedBy nvarchar(128),
    UpdatedOn datetime
)


-- ExpensePayslipItems Audit Trigger
CREATE TRIGGER ExpensePayslipItemsAuditTrig ON ExpensePayslipItems 
FOR INSERT, UPDATE
AS
	declare @expensepayslipitem varchar(4);
	declare @updatedby nvarchar(128);
	declare @updatedon datetime;

	select @expensepayslipitem=i.ExpensePayslipItem from inserted i;

	insert into ExpensePayslipItemsAudit
           (ExpensePayslipItem,UpdatedBy,UpdatedOn) 
	values(@expensepayslipitem,SUSER_SNAME(),getdate());
GO




-- View listing both incomes and expenses 
CREATE VIEW IncomesVSExpenses AS
	SELECT IncomePayslipItems.IncomePayslipItem, ExpensePayslipItems.ExpensePayslipItem
		FROM IncomePayslipItems, ExpensePayslipItems




-- employeeDetails Table Index
CREATE INDEX IX_EmployeeNumber_PayslipItemCode
ON employeeDetails(EmployeeNumber,PayslipItemCode);