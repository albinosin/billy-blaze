/* 100 ultimos */
select * from double_data order by dt_spin  desc limit 100;
/* Quantidade de vezes que saiu o branco*/
select count(*) from double_data  where fk_int_id_color = 3;
/* Lista brancos */
select * from double_data  where fk_int_id_color = 3;
/* QTd de registros */
select count(*) from double_data;
/* Data que iniciou a coleta e a final */
select min(dt_spin) as min, max(dt_spin) as max from double_data; 

/* Organizado */
select
	dd.id,
	dd.fk_int_id_color,
	dc.char_name as cor,
	dd.number_spin as numero,
	dd.dec_black,
	dd.dec_red,
	dd.dec_white,
	DATE_FORMAT(dd.dt_spin, "%d/%m/%Y %T") as data_hora
from
	double_data dd
inner join double_colors dc
on dc.id = dd.fk_int_id_color 
limit 100;

/* Qtd branca por hora */
select	
	DATE_FORMAT(date(dd.dt_spin), "%d/%m/%Y") as dt,
	HOUR(dd.dt_spin) as hora,
	count(*) as qtd	
from
	double_data dd
where
	dd.fk_int_id_color = 3
group by date(dd.dt_spin), HOUR(dd.dt_spin)
order by date(dd.dt_spin), HOUR(dd.dt_spin);

/* Qtd branco por hora e weekday */
select	
	WEEKDAY(dd.dt_spin) as dia_nro,
	case WEEKDAY(dd.dt_spin)
		when 0 then 'Seg'
		when 1 then 'Ter'
		when 2 then 'Qua'
		when 3 then 'Qui'
		when 4 then 'Sex'
		when 5 then 'Sab'
		when 6 then 'Dom'
	end as dia_texto,
	HOUR(dd.dt_spin) as hora,
	count(*) as qtd	
from
	double_data dd
where
	dd.fk_int_id_color = 3
group by WEEKDAY(dd.dt_spin), HOUR(dd.dt_spin)
order by WEEKDAY(dd.dt_spin), HOUR(dd.dt_spin)

/* Qtd branco weekday*/ 
select	
	WEEKDAY(dd.dt_spin) as dia_nro,
	case WEEKDAY(dd.dt_spin)
		when 0 then 'Seg'
		when 1 then 'Ter'
		when 2 then 'Qua'
		when 3 then 'Qui'
		when 4 then 'Sex'
		when 5 then 'Sab'
		when 6 then 'Dom'
	end as dia_texto,	
	count(*) as qtd	
from
	double_data dd
where
	dd.fk_int_id_color = 3
group by WEEKDAY(dd.dt_spin)
order by WEEKDAY(dd.dt_spin)


/* diferenca tempo entre branco */
select
	TIMEDIFF(ddp.dt_spin, ddp.dt_anterior) as diferenca_tempo
from
	(
	select
		id,
		dd.dt_spin,
		(
		select
			max(dd2.dt_spin)
		from
			double_data dd2
		where
			dd2.dt_spin < dd.dt_spin
			and dd2.fk_int_id_color = 3
		limit 1) as dt_anterior
	from
		double_data dd
	where
		dd.fk_int_id_color = 3) as ddp
where
	ddp.dt_anterior is not null;

/* Media intervalo tempo entre brancos */
select
	sec_to_time(avg(time_to_sec(TIMEDIFF(ddp.dt_spin, ddp.dt_anterior))))
from
	(
	select
		id,
		dd.dt_spin,
		(
		select
			max(dd2.dt_spin)
		from
			double_data dd2
		where
			dd2.dt_spin < dd.dt_spin
			and dd2.fk_int_id_color = 3
		limit 1) as dt_anterior
	from
		double_data dd
	where
		dd.fk_int_id_color = 3) as ddp
where
	ddp.dt_anterior is not null;

/* 49, 80, 86 */

/* saldo por jogada*/
select * 
from
(select
	dd.id,
	dd.fk_int_id_color,
	dc.char_name as cor,
	dd.number_spin as numero,
	dd.dec_black,
	dd.dec_red,
	dd.dec_white,
	DATE_FORMAT(dd.dt_spin, "%d/%m/%Y %T") as data_hora,
	case dec_black
		when -1 then 0
		else dec_red + dec_white 
	end as lucro_bruto,
	case dec_black
		when -1 then 0
		else dec_black * 2
	end as perda_bruta,
	case dec_black
		when -1 then 0
		else (dec_red + dec_white) - (dec_black * 2)
	end as saldo
from
	double_data dd
inner join double_colors dc
on dc.id = dd.fk_int_id_color 
where dd.fk_int_id_color = 1
UNION ALL
select
	dd.id,
	dd.fk_int_id_color,
	dc.char_name as cor,
	dd.number_spin as numero,
	dd.dec_black,
	dd.dec_red,
	dd.dec_white,
	DATE_FORMAT(dd.dt_spin, "%d/%m/%Y %T") as data_hora,
	case dec_black
		when -1 then 0
		else dec_black + dec_white 
	end as lucro_bruto,
	case dec_black
		when -1 then 0
		else dec_red * 2
	end as perda_bruta,
	case dec_black
		when -1 then 0
		else (dec_black + dec_white) - (dec_red * 2)
	end as saldo
from
	double_data dd
inner join double_colors dc
on dc.id = dd.fk_int_id_color 
where dd.fk_int_id_color = 2
UNION ALL
select
	dd.id,
	dd.fk_int_id_color,
	dc.char_name as cor,
	dd.number_spin as numero,
	dd.dec_black,
	dd.dec_red,
	dd.dec_white,
	DATE_FORMAT(dd.dt_spin, "%d/%m/%Y %T") as data_hora,
	case dec_black
		when -1 then 0
		else dec_black + dec_red 
	end as lucro_bruto,
	case dec_black
		when -1 then 0
		else dec_white * 14
	end as perda_bruta,
	case dec_black
		when -1 then 0
		else (dec_black + dec_red) - (dec_white * 14)
	end as saldo
from
	double_data dd
inner join double_colors dc
on dc.id = dd.fk_int_id_color 
where dd.fk_int_id_color = 3) un 
order by un.id


/* Sequencia >= 3 por hora */
select	
	DATE_FORMAT(date(ds.dt_spin), "%d/%m/%Y") as dt,
	HOUR(ds.dt_spin) as hora,
	count(*) as qtd
from
	double_sequence ds
where
	ds.int_count_color >= 3
group by date(ds.dt_spin), HOUR(ds.dt_spin) 
order by date(ds.dt_spin), HOUR(ds.dt_spin);

/* hora e cor */
select	
	DATE_FORMAT(date(ds.dt_spin), "%d/%m/%Y") as dt,
	HOUR(ds.dt_spin) as hora,
	count(*) as qtd,
	ds.fk_int_id_color,
	dc.char_name 
from
	double_sequence ds
inner join double_colors dc 
on dc.id = ds.fk_int_id_color	
where
	ds.int_count_color >= 3
group by date(ds.dt_spin), HOUR(ds.dt_spin) ,ds.fk_int_id_color 
order by date(ds.dt_spin), HOUR(ds.dt_spin);


/* Sequencia por dia da semana e data */
select	
	DATE_FORMAT(date(ds.dt_spin), "%d/%m/%Y") as dt,
	WEEKDAY(ds.dt_spin) as dia_nro,
	case WEEKDAY(ds.dt_spin)
		when 0 then 'Seg'
		when 1 then 'Ter'
		when 2 then 'Qua'
		when 3 then 'Qui'
		when 4 then 'Sex'
		when 5 then 'Sab'
		when 6 then 'Dom'
	end as dia_texto,
	count(*) as qtd	
from
	double_sequence ds
where
	ds.int_count_color >= 3
group by date(ds.dt_spin), WEEKDAY(ds.dt_spin) 
order by date(ds.dt_spin), WEEKDAY(ds.dt_spin);

/* Sequencia por dia da semana, por cor*/
select	
	DATE_FORMAT(date(ds.dt_spin), "%d/%m/%Y") as dt,
	WEEKDAY(ds.dt_spin) as dia_nro,
	case WEEKDAY(ds.dt_spin)
		when 0 then 'Seg'
		when 1 then 'Ter'
		when 2 then 'Qua'
		when 3 then 'Qui'
		when 4 then 'Sex'
		when 5 then 'Sab'
		when 6 then 'Dom'
	end as dia_texto,	
	count(*) as qtd	,
	ds.fk_int_id_color,
	dc.char_name 
from
	double_sequence ds
inner join double_colors dc 
on dc.id = ds.fk_int_id_color
where
	ds.int_count_color >= 3
group by date(ds.dt_spin), WEEKDAY(ds.dt_spin) ,ds.fk_int_id_color 
order by date(ds.dt_spin), WEEKDAY(ds.dt_spin);


/* Sequencia por dia da semana e hora*/
select	
	DATE_FORMAT(date(ds.dt_spin), "%d/%m/%Y") as dt,	
	WEEKDAY(ds.dt_spin) as dia_nro,
	case WEEKDAY(ds.dt_spin)
		when 0 then 'Seg'
		when 1 then 'Ter'
		when 2 then 'Qua'
		when 3 then 'Qui'
		when 4 then 'Sex'
		when 5 then 'Sab'
		when 6 then 'Dom'
	end as dia_texto,
	HOUR(ds.dt_spin) as hra,
	count(*) as qtd	
from
	double_sequence ds
where
	ds.int_count_color >= 3
group by date(ds.dt_spin), WEEKDAY(ds.dt_spin), HOUR(ds.dt_spin) 
order by date(ds.dt_spin), WEEKDAY(ds.dt_spin), HOUR(ds.dt_spin);