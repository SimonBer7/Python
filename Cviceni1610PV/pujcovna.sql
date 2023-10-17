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




insert into bydliste(ulice, mesto, psc) values('Studentsk� 25', 'Ostrava P��voz', 70831);
insert into bydliste(ulice, mesto, psc) values('Karvinsk� 4', 'Karvin�-R�j', 73564);
insert into bydliste(ulice, mesto, psc) values('Hornosu�sk� 24', 'Horn� Such�', 73535);
insert into bydliste(ulice, mesto, psc) values('Studentsk� 1', 'Ostrava P��voz', 70831);
insert into bydliste(ulice, mesto, psc) values('Vnit�n� 1151', 'T�rlicko', 73565);

insert into zakaznik(jmeno, prijmeni, bydliste_id) values('Luk�', 'Pavel', 1);
insert into zakaznik(jmeno, prijmeni, bydliste_id) values('Pavel', 'Kvapil', 2);
insert into zakaznik(jmeno, prijmeni, bydliste_id) values('Lev�', 'Pavla', 3);
insert into zakaznik(jmeno, prijmeni, bydliste_id) values('Pavel', 'Luk�', 1);
insert into zakaznik(jmeno, prijmeni, bydliste_id) values('Lev�', 'Pavla', 4);
insert into zakaznik(jmeno, prijmeni, bydliste_id) values('Karel', 'Nov�k', 5);

insert into film(cislo_dvd, nazev) values(21, 'Pir�ti z Karibiku I.');
insert into film(cislo_dvd, nazev) values(5, 'Honza m�lem kr�lem');
insert into film(cislo_dvd, nazev) values(22, 'Pir�ti z Karibiku II.');
insert into film(cislo_dvd, nazev) values(23, 'Pir�ti z Karibiku III.');
insert into film(cislo_dvd, nazev) values(51, 'Popelka');

insert into vypujcka(cislo_vypujcky, zakaznik_id, film_id, datum_vypujceni, datum_vraceni) values(1, 1, 1, '2012-01-05', '2012-01-09');
insert into vypujcka(cislo_vypujcky, zakaznik_id, film_id, datum_vypujceni, datum_vraceni) values(2, 1, 2, '2012-01-05', '2012-01-08');
insert into vypujcka(cislo_vypujcky, zakaznik_id, film_id, datum_vypujceni, datum_vraceni) values(3, 2, 1, '2012-01-10', '2012-01-11');
insert into vypujcka(cislo_vypujcky, zakaznik_id, film_id, datum_vypujceni, datum_vraceni) values(4, 2, 3, '2012-01-10', '2012-01-11');
insert into vypujcka(cislo_vypujcky, zakaznik_id, film_id, datum_vypujceni, datum_vraceni) values(5, 2, 4, '2012-01-10', null);


create view big_select as
SELECT
    v.id AS '��slo z�znamu',
    z.jmeno AS 'Jm�no Z�kazn�ka',
    z.prijmeni AS 'P��jmen� Z�kazn�ka',
    b.ulice AS 'Ulice',
    b.mesto AS 'M�sto',
    b.psc AS 'PS�',
    f.nazev AS 'N�zev Filmu',
    v.datum_vypujceni AS 'Datum V�p�j�ky',
    v.datum_vraceni AS 'Datum Vr�cen�'
FROM vypujcka v
JOIN zakaznik z ON v.zakaznik_id = z.id
JOIN bydliste b ON z.bydliste_id = b.id
JOIN film f ON v.film_id = f.id;

select * from big_select;

