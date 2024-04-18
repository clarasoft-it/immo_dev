--------------------------------------------------------------------------------------
--  IMMO
--------------------------------------------------------------------------------------
--
--  To avoid having to provide a user/password everytime one wants to access
--  the database, the latter can be configured to use trust 
--  authentication mode; the host will also only be restricted to localhost.
--
--  Edit the pg_hba.conf file to specify trust authentication; the 
--  location of this file may be retrieved by issuing the following
--  command in psql:
--
--    psql -t -P format=unaligned -c 'SHOW hba_file;'
--
--  The output will be something like:
--
--    /etc/postgresql/16/main/pg_hba.conf
--
--  The pg_hba.conf file has entries like the following:
--
--      # TYPE  DATABASE        USER            ADDRESS                 METHOD
--
--      # "local" is for Unix domain socket connections only
--      local   all             all                                     peer
--      # IPv4 local connections:
--      host    all             all             127.0.0.1/32            scram-sha-256
--      # IPv6 local connections:
--      host    all             all             ::1/128                 scram-sha-256
--
--  It is IMPORTANT that the authentication rules be placed in the proper order.
--  PostgreSQL will examine each line in sequence until it finds one that matches 
--  the conditions under which the connection is requested. It is therefore
--  recommended to put the CFS Repository database connection configuration(s)
--  before lines that specify "all" under the DATABSE column:
--
--      # TYPE  DATABASE        USER            ADDRESS                 METHOD
--
--      #immo --------------------------------------------------------------
--      local   cfsrepo         all                                     trust
--      #local   cfsrepo         all             127.0.0.1/32            trust
--      #local   cfsrepo         all             ::1/128                 trust
--      #-----------------------------------------------------------------------------
--
--      # "local" is for Unix domain socket connections only
--      local   all             all                                     peer
--      # IPv4 local connections:
--      host    all             all             127.0.0.1/32            scram-sha-256
--      # IPv6 local connections:
--      host    all             all             ::1/128                 scram-sha-256
--
--  The above example only allows connections from the system hosting the 
--  CFS Repository, either using local sockets or TCP sockets. 
--
--  Once the file updated, restart the postgresql daemon:
--  
--    sudo systemctl stop postgresql
--    sudo systemctl start postgresql
--
--------------------------------------------------------------------------------------



create database immo LOCALE 'en_CA.UTF-8';

\c immo;

CREATE TABLE BUILDING (
        ID VARCHAR (36) NOT NULL,
        NAME VARCHAR(128) NOT NULL ,
        NO VARCHAR(32) NOT NULL ,
        STREET VARCHAR(128) NOT NULL ,
        CITY VARCHAR(128) NOT NULL ,
        DEPARTMENT VARCHAR(128) NOT NULL ,
        COUNTRY VARCHAR(128) NOT NULL ,
        ZIP VARCHAR(32) NOT NULL ,
        CRTU VARCHAR(64) NOT NULL ,
        CRTD TIMESTAMP NOT NULL ,
        UPDU VARCHAR(64) NOT NULL ,
        UPDD TIMESTAMP NOT NULL,
        PRIMARY KEY (ID));

COMMENT ON TABLE BUILDING IS 'Buildings';

COMMENT ON COLUMN BUILDING.ID IS 'Building ID';
COMMENT ON COLUMN BUILDING.NAME IS 'Building name';
COMMENT ON COLUMN BUILDING.NO IS 'Street number';
COMMENT ON COLUMN BUILDING.STREET IS 'Street name';
COMMENT ON COLUMN BUILDING.CITY IS 'City';
COMMENT ON COLUMN BUILDING.DEPARTMENT IS 'Prov/State/Department';
COMMENT ON COLUMN BUILDING.CITY IS 'City';
COMMENT ON COLUMN BUILDING.COUNTRY IS 'Country';
COMMENT ON COLUMN BUILDING.ZIP IS 'Postal code';
COMMENT ON COLUMN BUILDING.CRTU IS 'Creation User';
COMMENT ON COLUMN BUILDING.CRTD IS 'Creation Stamp';
COMMENT ON COLUMN BUILDING.UPDU IS 'Modification USer';
COMMENT ON COLUMN BUILDING.UPDD IS 'Modification Stamp';

CREATE UNIQUE INDEX BUILDING_I001 ON BUILDING (NAME);
CREATE UNIQUE INDEX BUILDING_I002 ON BUILDING (NO, STREET, CITY, DEPARTMENT, COUNTRY);
CREATE INDEX BUILDING_I003 ON BUILDING (CITY, DEPARTMENT, COUNTRY);
CREATE INDEX BUILDING_I004 ON BUILDING (DEPARTMENT, COUNTRY);
CREATE INDEX BUILDING_I005 ON BUILDING (COUNTRY);
CREATE UNIQUE INDEX BUILDING_I006 ON BUILDING (ID);

CREATE TABLE UNIT (
        BUILDING_ID VARCHAR(36) NOT NULL ,
        NAME VARCHAR(32) NOT NULL , 
        ACTIVE VARCHAR(1) NOT NULL ,
        CRTU VARCHAR(64) NOT NULL ,
        CRTD TIMESTAMP NOT NULL ,
        UPDU VARCHAR(64) NOT NULL ,
        UPDD TIMESTAMP NOT NULL,
        FOREIGN KEY (BUILDING_ID) REFERENCES BUILDING (ID),
        PRIMARY KEY (BUILDING_ID, NAME));

COMMENT ON TABLE UNIT IS 'Units' ;

COMMENT ON COLUMN UNIT.BUILDING_ID IS 'Building ID';
COMMENT ON COLUMN UNIT.NAME IS 'Unit name';
COMMENT ON COLUMN UNIT.ACTIVE IS 'Active T/F';
COMMENT ON COLUMN UNIT.CRTU IS 'Creation User';
COMMENT ON COLUMN UNIT.CRTD IS 'Creation Stamp';
COMMENT ON COLUMN UNIT.UPDU IS 'Modification User';
COMMENT ON COLUMN UNIT.UPDD IS 'Modification Stamp';

CREATE UNIQUE INDEX UNIT_I001 ON UNIT (BUILDING_ID, NAME);

CREATE TABLE OWNER (
        ID VARCHAR(36) NOT NULL ,
        CONTACT_ID VARCHAR(36) NOT NULL ,
        FNAME VARCHAR(64) NOT NULL , 
        LNAME VARCHAR(64) NOT NULL , 
        STATUS VARCHAR(5) NOT NULL , 
        CRTU VARCHAR(64) NOT NULL ,
        CRTD TIMESTAMP NOT NULL ,
        UPDU VARCHAR(64) NOT NULL ,
        UPDD TIMESTAMP NOT NULL,
        PRIMARY KEY (ID));

COMMENT ON TABLE OWNER IS 'Owners' ;

COMMENT ON COLUMN OWNER.ID IS 'Owner ID';
COMMENT ON COLUMN OWNER.CONTACT_ID IS 'Contact ID';
COMMENT ON COLUMN OWNER.FNAME IS 'First name';
COMMENT ON COLUMN OWNER.LNAME IS 'Last name';
COMMENT ON COLUMN OWNER.STATUS IS 'Status';
COMMENT ON COLUMN OWNER.CRTU IS 'Creation User';
COMMENT ON COLUMN OWNER.CRTD IS 'Creation Stamp';
COMMENT ON COLUMN OWNER.UPDU IS 'Modification User';
COMMENT ON COLUMN OWNER.UPDD IS 'Modification Stamp';

CREATE INDEX OWNER_I001 ON OWNER (LNAME, FNAME);
CREATE INDEX OWNER_I002 ON OWNER (STATUS);
CREATE UNIQUE INDEX OWNER_I003 ON OWNER (ID);

CREATE TABLE EXERCICE (
        BUILDING_ID VARCHAR(36) NOT NULL ,
        YEAR VARCHAR(4) NOT NULL , 
        MONTH_START VARCHAR(2) NOT NULL , 
        DAY_START VARCHAR(2) NOT NULL , 
        NUM_PERIODS VARCHAR(2) NOT NULL , 
        CRTU VARCHAR(64) NOT NULL ,
        CRTD TIMESTAMP NOT NULL ,
        UPDU VARCHAR(64) NOT NULL ,
        UPDD TIMESTAMP NOT NULL,
        FOREIGN KEY (BUILDING_ID) REFERENCES BUILDING (ID),
        PRIMARY KEY (BUILDING_ID, YEAR));

COMMENT ON TABLE EXERCICE IS 'Accounting Exercices' ;

COMMENT ON COLUMN EXERCICE.BUILDING_ID IS 'Building ID';
COMMENT ON COLUMN EXERCICE.YEAR IS 'Year';
COMMENT ON COLUMN EXERCICE.MONTH_START IS 'Starting month (01, 02, etc)';
COMMENT ON COLUMN EXERCICE.DAY_START IS 'Starting monthly day (01, 02, etc)';
COMMENT ON COLUMN EXERCICE.NUM_PERIODS IS 'Number of monthly periods';
COMMENT ON COLUMN EXERCICE.CRTU IS 'Creation User';
COMMENT ON COLUMN EXERCICE.CRTD IS 'Creation Stamp';
COMMENT ON COLUMN EXERCICE.UPDU IS 'Modification User';
COMMENT ON COLUMN EXERCICE.UPDD IS 'Modification Stamp';

CREATE UNIQUE INDEX EXERCICE_I001 ON EXERCICE (BUILDING_ID, YEAR);

CREATE TABLE BUILDING_OWNER (
        BUILDING_ID VARCHAR(36) NOT NULL ,
        UNIT_NAME VARCHAR(32) NOT NULL , 
        OWNER_ID VARCHAR(36) NOT NULL , 
        START_DATE DATE NOT NULL ,
        END_DATE DATE NOT NULL ,
        ACTIVE VARCHAR(1) NOT NULL,
        CRTU VARCHAR(64) NOT NULL ,
        CRTD TIMESTAMP NOT NULL ,
        UPDU VARCHAR(64) NOT NULL ,
        UPDD TIMESTAMP NOT NULL,
        FOREIGN KEY (BUILDING_ID, UNIT_NAME) REFERENCES UNIT (BUILDING_ID, NAME),
        FOREIGN KEY (OWNER_ID) REFERENCES OWNER (ID),
        PRIMARY KEY (BUILDING_ID, UNIT_NAME, OWNER_ID));

COMMENT ON TABLE BUILDING_OWNER IS 'Building Owners' ;

COMMENT ON COLUMN BUILDING_OWNER.BUILDING_ID IS 'Building ID';
COMMENT ON COLUMN BUILDING_OWNER.UNIT_NAME IS 'Unit name';
COMMENT ON COLUMN BUILDING_OWNER.OWNER_ID IS 'Owner ID';
COMMENT ON COLUMN BUILDING_OWNER.START_DATE IS 'Date From';
COMMENT ON COLUMN BUILDING_OWNER.END_DATE IS 'Date To';
COMMENT ON COLUMN BUILDING_OWNER.ACTIVE IS 'Status';
COMMENT ON COLUMN BUILDING_OWNER.CRTU IS 'Creation User';
COMMENT ON COLUMN BUILDING_OWNER.CRTD IS 'Creation Stamp';
COMMENT ON COLUMN BUILDING_OWNER.UPDU IS 'Modification User';
COMMENT ON COLUMN BUILDING_OWNER.UPDD IS 'Modification Stamp';

CREATE UNIQUE INDEX BUILDING_OWNER_I001 ON BUILDING_OWNER (BUILDING_ID, UNIT_NAME, OWNER_ID);
