CREATE DATABASE employeeDB;

use employeeDB;

CREATE TABLE PayslipItemCodes (
    PayslipItemCode varchar(4) NOT NULL PRIMARY KEY
);

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

CREATE TABLE IncomePayslipItems (
    IncomePayslipItem varchar(4) NOT NULL PRIMARY KEY,
    FOREIGN KEY(IncomePayslipItem) REFERENCES PayslipItemCodes(PayslipItemCode)
);

CREATE TABLE ExpensePayslipItems (
    ExpensePayslipItem varchar(4) NOT NULL PRIMARY KEY,
    FOREIGN KEY(ExpensePayslipItem) REFERENCES PayslipItemCodes(PayslipItemCode)
);