CREATE SCHEMA IF NOT EXISTS usbank_bankings_core;

CREATE TABLE usbank_bankings_core.ACCOUNTS
(
	ID UUID NOT NULL,FNAME VARCHAR(20),LNAME VARCHAR(10),
	MOBILE VARCHAR(12),ADDRESS_ID INT NOT NULL,EMAIL VARCHAR(15)

);

select * from usbank_bankings_core.accounts;