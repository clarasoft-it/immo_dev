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



create database immo_dev LOCALE 'en_CA.UTF-8';

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
        QUOTE_SHARE NUMERIC(3,4) NOT NULL DEFAULT 0.0000,
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
COMMENT ON COLUMN UNIT.QUOTE_SHARE IS 'Quote Share';
COMMENT ON COLUMN UNIT.CRTU IS 'Creation User';
COMMENT ON COLUMN UNIT.CRTD IS 'Creation Stamp';
COMMENT ON COLUMN UNIT.UPDU IS 'Modification User';
COMMENT ON COLUMN UNIT.UPDD IS 'Modification Stamp';

CREATE UNIQUE INDEX UNIT_I001 ON UNIT (BUILDING_ID, NAME);

CREATE TABLE CONTACT (
        ID VARCHAR(36) NOT NULL,
        FNAME VARCHAR(64) NOT NULL,
        MNAME VARCHAR(64) NOT NULL,
        LNAME VARCHAR(64) NOT NULL,
        STATUS VARCHAR(5) NOT NULL , 
        CRTU VARCHAR(64) NOT NULL ,
        CRTD TIMESTAMP NOT NULL ,
        UPDU VARCHAR(64) NOT NULL ,
        UPDD TIMESTAMP NOT NULL,
        PRIMARY KEY (ID));

COMMENT ON TABLE CONTACT IS 'Contacts' ;

COMMENT ON COLUMN CONTACT.ID IS 'Contact ID';
COMMENT ON COLUMN CONTACT.FNAME IS 'First name';
COMMENT ON COLUMN CONTACT.MNAME IS 'Middle name';
COMMENT ON COLUMN CONTACT.LNAME IS 'Last name';
COMMENT ON COLUMN CONTACT.STATUS IS 'Activity status';
COMMENT ON COLUMN CONTACT.CRTU IS 'Creation User';
COMMENT ON COLUMN CONTACT.CRTD IS 'Creation Stamp';
COMMENT ON COLUMN CONTACT.UPDU IS 'Modification User';
COMMENT ON COLUMN CONTACT.UPDD IS 'Modification Stamp';

CREATE INDEX CONTACT_I001 ON CONTACT (ID);
CREATE INDEX CONTACT_I002 ON CONTACT (LNAME, FNAME, MNAME, STATUS);

CREATE TABLE ADDRESS (
        CONTACT_ID VARCHAR(36) NOT NULL,
        STATUS VARCHAR(5) NOT NULL , 
        ADDRESS1 VARCHAR(128) NOT NULL ,
        ADDRESS2 VARCHAR(128) NOT NULL ,
        CITY VARCHAR(128) NOT NULL ,
        DEPARTMENT VARCHAR(128) NOT NULL ,
        COUNTRY VARCHAR(128) NOT NULL ,
        ZIP VARCHAR(32) NOT NULL ,
        PHONE1 VARCHAR(32) NOT NULL ,
        PHONE2 VARCHAR(32) NOT NULL ,
        FAX VARCHAR(32) NOT NULL ,
        EMAIL VARCHAR(128) NOT NULL ,
        CRTU VARCHAR(64) NOT NULL ,
        CRTD TIMESTAMP NOT NULL ,
        UPDU VARCHAR(64) NOT NULL ,
        UPDD TIMESTAMP NOT NULL, 
        FOREIGN KEY (CONTACT_ID) REFERENCES CONTACT(ID));

COMMENT ON COLUMN ADDRESS.CONTACT_ID IS 'Contact ID';
COMMENT ON COLUMN ADDRESS.STATUS IS 'Activity Status';
COMMENT ON COLUMN ADDRESS.ADDRESS1 IS 'Address 1';
COMMENT ON COLUMN ADDRESS.ADDRESS2 IS 'Address 2';
COMMENT ON COLUMN ADDRESS.CITY IS 'City';
COMMENT ON COLUMN ADDRESS.DEPARTMENT IS 'Prov/State/Department';
COMMENT ON COLUMN ADDRESS.COUNTRY IS 'Country';
COMMENT ON COLUMN ADDRESS.ZIP IS 'Postal code';
COMMENT ON COLUMN ADDRESS.PHONE1 IS 'Phone 1';
COMMENT ON COLUMN ADDRESS.PHONE2 IS 'Phone 2';
COMMENT ON COLUMN ADDRESS.FAX IS 'Fax';
COMMENT ON COLUMN ADDRESS.EMAIL IS 'Email';
COMMENT ON COLUMN ADDRESS.CRTU IS 'Creation User';
COMMENT ON COLUMN ADDRESS.CRTD IS 'Creation Stamp';
COMMENT ON COLUMN ADDRESS.UPDU IS 'Modification User';
COMMENT ON COLUMN ADDRESS.UPDD IS 'Modification Stamp';

CREATE INDEX ADDRESS_I001 ON ADDRESS (COUNTRY, DEPARTMENT, CITY, STATUS);
CREATE INDEX ADDRESS_I002 ON ADDRESS (ZIP);

CREATE TABLE OWNER (
        CONTACT_ID VARCHAR(36) REFERENCES CONTACT(ID) NOT NULL ,
        STATUS VARCHAR(5) NOT NULL , 
        CRTU VARCHAR(64) NOT NULL ,
        CRTD TIMESTAMP NOT NULL ,
        UPDU VARCHAR(64) NOT NULL ,
        UPDD TIMESTAMP NOT NULL,
        FOREIGN KEY (CONTACT_ID) REFERENCES CONTACT(ID) );

COMMENT ON TABLE OWNER IS 'Owners' ;

COMMENT ON COLUMN OWNER.CONTACT_ID IS 'Owner ID';
COMMENT ON COLUMN OWNER.STATUS IS 'Status';
COMMENT ON COLUMN OWNER.CRTU IS 'Creation User';
COMMENT ON COLUMN OWNER.CRTD IS 'Creation Stamp';
COMMENT ON COLUMN OWNER.UPDU IS 'Modification User';
COMMENT ON COLUMN OWNER.UPDD IS 'Modification Stamp';

CREATE INDEX OWNER_I001 ON OWNER (CONTACT_ID, STATUS, CRTD);

CREATE TABLE ADMINISTRATOR (
        CONTACT_ID VARCHAR(36) REFERENCES CONTACT(ID) NOT NULL ,
        STATUS VARCHAR(5) NOT NULL , 
        CRTU VARCHAR(64) NOT NULL ,
        CRTD TIMESTAMP NOT NULL ,
        UPDU VARCHAR(64) NOT NULL ,
        UPDD TIMESTAMP NOT NULL,
        FOREIGN KEY (CONTACT_ID) REFERENCES CONTACT(ID) );

COMMENT ON TABLE ADMINISTRATOR IS 'Building administrators' ;

COMMENT ON COLUMN ADMINISTRATOR.CONTACT_ID IS 'Administrator ID';
COMMENT ON COLUMN ADMINISTRATOR.STATUS IS 'Status';
COMMENT ON COLUMN ADMINISTRATOR.CRTU IS 'Creation User';
COMMENT ON COLUMN ADMINISTRATOR.CRTD IS 'Creation Stamp';
COMMENT ON COLUMN ADMINISTRATOR.UPDU IS 'Modification User';
COMMENT ON COLUMN ADMINISTRATOR.UPDD IS 'Modification Stamp';

CREATE INDEX ADMINISTRATOR_I001 ON ADMINISTRATOR (CONTACT_ID, STATUS, CRTD);

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
        OWNER_ID VARCHAR(36) NOT NULL, 
        START_DATE DATE NOT NULL ,
        END_DATE DATE NOT NULL ,
        ACTIVE VARCHAR(1) NOT NULL,
        CRTU VARCHAR(64) NOT NULL ,
        CRTD TIMESTAMP NOT NULL ,
        UPDU VARCHAR(64) NOT NULL ,
        UPDD TIMESTAMP NOT NULL,
        FOREIGN KEY (BUILDING_ID, UNIT_NAME) REFERENCES UNIT (BUILDING_ID, NAME),
        FOREIGN KEY ());

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

CREATE INDEX BUILDING_OWNER_I001 ON BUILDING_OWNER (BUILDING_ID, UNIT_NAME, OWNER_ID, STATUS, CRTD);

CREATE TABLE LANGUAGE (
        ID VARCHAR(36) NOT NULL ,
        DESC_L VARCHAR(64) NOT NULL , 
        CRTU VARCHAR(64) NOT NULL ,
        CRTD TIMESTAMP NOT NULL ,
        UPDU VARCHAR(64) NOT NULL ,
        UPDD TIMESTAMP NOT NULL,
        PRIMARY KEY (ID));

COMMENT ON TABLE LANGUAGE IS 'Languages' ;

COMMENT ON COLUMN LANGUAGE.ID IS 'Language ID';
COMMENT ON COLUMN LANGUAGE.DESC_L IS 'Long description';
COMMENT ON COLUMN LANGUAGE.CRTU IS 'Creation User';
COMMENT ON COLUMN LANGUAGE.CRTD IS 'Creation Stamp';
COMMENT ON COLUMN LANGUAGE.UPDU IS 'Modification User';
COMMENT ON COLUMN LANGUAGE.UPDD IS 'Modification Stamp';

CREATE UNIQUE INDEX LANGUAGE_I001 ON LANGUAGE (ID);


CREATE TABLE APPLICATION (
        ID VARCHAR(32) NOT NULL ,
        DESC_S VARCHAR(32) NOT NULL , 
        DESC_L VARCHAR(64) NOT NULL , 
        CRTU VARCHAR(64) NOT NULL ,
        CRTD TIMESTAMP NOT NULL ,
        UPDU VARCHAR(64) NOT NULL ,
        UPDD TIMESTAMP NOT NULL,
        PRIMARY KEY (ID));

COMMENT ON TABLE APPLICATION IS 'Applications' ;

COMMENT ON COLUMN APPLICATION.ID IS 'Applciation ID';
COMMENT ON COLUMN APPLICATION.DESC_S IS 'Short description';
COMMENT ON COLUMN APPLICATION.DESC_L IS 'Long description';
COMMENT ON COLUMN APPLICATION.CRTU IS 'Creation User';
COMMENT ON COLUMN APPLICATION.CRTD IS 'Creation Stamp';
COMMENT ON COLUMN APPLICATION.UPDU IS 'Modification User';
COMMENT ON COLUMN APPLICATION.UPDD IS 'Modification Stamp';

CREATE UNIQUE INDEX APPLICATION_I001 ON APPLICATION (ID);


CREATE TABLE CAPTION (
        ID VARCHAR(36) NOT NULL ,
        APP_ID VARCHAR(36) NOT NULL ,
        LANG_ID VARCHAR(36) NOT NULL ,
        CAPTION VARCHAR(255) NOT NULL , 
        CRTU VARCHAR(64) NOT NULL ,
        CRTD TIMESTAMP NOT NULL ,
        UPDU VARCHAR(64) NOT NULL ,
        UPDD TIMESTAMP NOT NULL,
        FOREIGN KEY (LANG_ID) REFERENCES LANGUAGE (ID),
        FOREIGN KEY (APP_ID) REFERENCES APPLICATION (ID),
        PRIMARY KEY (APP_ID, LANG_ID, ID));

COMMENT ON TABLE CAPTION IS 'Languages' ;
COMMENT ON COLUMN CAPTION.ID IS 'Caption ID';
COMMENT ON COLUMN CAPTION.APP_ID IS 'Application ID';
COMMENT ON COLUMN CAPTION.LANG_ID IS 'Language ID';
COMMENT ON COLUMN CAPTION.CAPTION IS 'Caption';
COMMENT ON COLUMN CAPTION.CRTU IS 'Creation User';
COMMENT ON COLUMN CAPTION.CRTD IS 'Creation Stamp';
COMMENT ON COLUMN CAPTION.UPDU IS 'Modification User';
COMMENT ON COLUMN CAPTION.UPDD IS 'Modification Stamp';

CREATE UNIQUE INDEX CAPTION_I001 ON CAPTION (APP_ID, LANG_ID, ID);
CREATE UNIQUE INDEX CAPTION_I002 ON CAPTION (ID, APP_ID, LANG_ID);
CREATE UNIQUE INDEX CAPTION_I003 ON CAPTION (LANG_ID, APP_ID, ID);
