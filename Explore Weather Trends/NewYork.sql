SELECT c.year, c.city, c.avg_temp as city_avg_temp,
	g.avg_temp as global_avg_temp
from city_data c
inner join global_data g on c.year = g.year
where c.city = 'New York'
and c.country = 'United States'
order by c.year
