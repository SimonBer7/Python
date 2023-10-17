create database pujcovna;
use pujcovna;


create table bydliste(
	id int primary key identity(1,1),
	ulice varchar(80) not null,
	mesto varchar(50) not null,
	psc int not null
);


create table zakaznik(
	id int primary key identity(1,1),
	jmeno varchar(30) not null,
	prijmeni varchar(30) not null,
	bydliste_id int foreign key references bydliste(id)
);

create table film(
	id int primary key identity(1,1),
	cislo_dvd int not null check(cislo_dvd > 0),
	nazev varchar(100) not null
);

create table vypujcka(
	id int primary key identity(1,1),
	cislo_vypujcky int not null check(cislo_vypujcky > 0),
	zakaznik_id int foreign key references zakaznik(id),
	film_id int foreign key references film(id),
	datum_vypujceni date,
	datum_vraceni date 
);




insert into bydliste(ulice, mesto, psc) values('Studentská 25', 'Ostrava Pøívoz', 70831);
insert into bydliste(ulice, mesto, psc) values('Karvinská 4', 'Karviná-Ráj', 73564);
insert into bydliste(ulice, mesto, psc) values('Hornosušská 24', 'Horní Suchá', 73535);
insert into bydliste(ulice, mesto, psc) values('Studentská 1', 'Ostrava Pøívoz', 70831);
insert into bydliste(ulice, mesto, psc) values('Vnitøní 1151', 'Tìrlicko', 73565);

insert into zakaznik(jmeno, prijmeni, bydliste_id) values('Lukáš', 'Pavel', 1);
insert into zakaznik(jmeno, prijmeni, bydliste_id) values('Pavel', 'Kvapil', 2);
insert into zakaznik(jmeno, prijmeni, bydliste_id) values('Levá', 'Pavla', 3);
insert into zakaznik(jmeno, prijmeni, bydliste_id) values('Pavel', 'Lukáš', 1);
insert into zakaznik(jmeno, prijmeni, bydliste_id) values('Levá', 'Pavla', 4);
insert into zakaznik(jmeno, prijmeni, bydliste_id) values('Karel', 'Novák', 5);

insert into film(cislo_dvd, nazev) values(21, 'Piráti z Karibiku I.');
insert into film(cislo_dvd, nazev) values(5, 'Honza málem králem');
insert into film(cislo_dvd, nazev) values(22, 'Piráti z Karibiku II.');
insert into film(cislo_dvd, nazev) values(23, 'Piráti z Karibiku III.');
insert into film(cislo_dvd, nazev) values(51, 'Popelka');

insert into vypujcka(cislo_vypujcky, zakaznik_id, film_id, datum_vypujceni, datum_vraceni) values(1, 1, 1, '2012-01-05', '2012-01-09');
insert into vypujcka(cislo_vypujcky, zakaznik_id, film_id, datum_vypujceni, datum_vraceni) values(2, 1, 2, '2012-01-05', '2012-01-08');
insert into vypujcka(cislo_vypujcky, zakaznik_id, film_id, datum_vypujceni, datum_vraceni) values(3, 2, 1, '2012-01-10', '2012-01-11');
insert into vypujcka(cislo_vypujcky, zakaznik_id, film_id, datum_vypujceni, datum_vraceni) values(4, 2, 3, '2012-01-10', '2012-01-11');
insert into vypujcka(cislo_vypujcky, zakaznik_id, film_id, datum_vypujceni, datum_vraceni) values(5, 2, 4, '2012-01-10', null);


create view big_select as
SELECT
    v.id AS 'Èíslo záznamu',
    z.jmeno AS 'Jméno Zákazníka',
    z.prijmeni AS 'Pøíjmení Zákazníka',
    b.ulice AS 'Ulice',
    b.mesto AS 'Mìsto',
    b.psc AS 'PSÈ',
    f.nazev AS 'Název Filmu',
    v.datum_vypujceni AS 'Datum Výpùjèky',
    v.datum_vraceni AS 'Datum Vrácení'
FROM vypujcka v
JOIN zakaznik z ON v.zakaznik_id = z.id
JOIN bydliste b ON z.bydliste_id = b.id
JOIN film f ON v.film_id = f.id;

select * from big_select;

