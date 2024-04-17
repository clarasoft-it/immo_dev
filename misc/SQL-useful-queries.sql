

-- adding a building:

insert  into  building_01 values (gen_random_uuid(), '123 Rue Principale', '123', 'Rue Principale', 'St-Tite', 'Quebec', 'Canada', 'J4Y 4R8', 'Clara', current_timestamp, 'Clara', current_timestamp);

insert  into  building values ('97f67291-c926-4098-bf04-a3890b2d5297', '123 Rue Principale', '123', 'Rue Principale', 'St-Tite', 'Quebec', 'Canada', 'J4Y 4R8', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert  into  building values ('ae66f43d-50db-4ee7-806f-59e220c23e7b', 'Le Chambord', '512', 'Rue du Chateau', 'Laval', 'Quebec', 'Canada', 'T4Y 4P8', 'Clara', current_timestamp, 'Clara', current_timestamp);

-- insert a new unit: the building ID should already exist in the building_01 table
insert into unit_02 values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);

-- insert an owner:
insert into owner_03 values(gen_random_uuid(), 'Olivier', 'Soucie', 'A', 'Clara', current_timestamp, 'Clara', current_timestamp);

-- add an accounting period:

insert into exercice_20 values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '2024', '03', '01', '12', 'Clara', current_timestamp, 'Clara', current_timestamp);

-- getting accounting for a building:

select a.name_01, b.year_20, b.month_start_20, b.day_start_20, b.num_periods_20 from building_01 a join exercice_20 b on a.id_01 = b.building_id_20 where a.name_01 = 'Le Van Horne';

select a.name_01, b.year_20, b.month_start_20, b.day_start_20, b.num_periods_20 from building_01 a join exercice_20 b on a.id_01 = b.building_id_20 where a.id_01 = 'ae66f43d-50db-4ee7-806f-59e220c23e7b';




insert into owner values('ffb16abb-998b-41ef-bd1b-1bab63c86e76', '662f8dec-1127-4c11-af47-082a74206801', 'Frederic', 'Soucie', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into owner values('15159ade-c297-4c68-8b6c-e6b096b84f93', '03164dd3-43bc-4831-8dfc-74a536d5000f', 'Emmanuel', 'Lara', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into owner values('c540509a-428b-48ae-bbd4-6109ee098650', '8df69fd8-6e73-40ff-b3c3-f7de41d4a701', 'Nosheen', 'Sadiq', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into owner values('9a94f3e2-73d7-4e9b-bef0-cc46b903fb01', '98283b86-877a-48eb-afed-f195e530b20c', 'Olivier', 'Soucie', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);


insert into unit values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '1', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into unit values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '2', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into unit values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '3', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into unit values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '4', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into unit values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '5', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into unit values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '6', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);



insert into building_owner values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '1', '9a94f3e2-73d7-4e9b-bef0-cc46b903fb01', current_date, '0001-01-01', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into building_owner values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '1', 'c540509a-428b-48ae-bbd4-6109ee098650', current_date, '0001-01-01', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into building_owner values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '5', '9a94f3e2-73d7-4e9b-bef0-cc46b903fb01', current_date, '0001-01-01', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into building_owner values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '2', '15159ade-c297-4c68-8b6c-e6b096b84f93', current_date, '0001-01-01', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into building_owner values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '3', 'c540509a-428b-48ae-bbd4-6109ee098650', current_date, '0001-01-01', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into building_owner values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '4', '9a94f3e2-73d7-4e9b-bef0-cc46b903fb01', current_date, '0001-01-01', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);
insert into building_owner values('ae66f43d-50db-4ee7-806f-59e220c23e7b', '6', '9a94f3e2-73d7-4e9b-bef0-cc46b903fb01', current_date, '0001-01-01', '1', 'Clara', current_timestamp, 'Clara', current_timestamp);


