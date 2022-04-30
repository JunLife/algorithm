select hour(datetime) as hour, count(*) as count
from animal_outs
group by hour(datetime)
having 9 <= hour and hour <= 19
order by hour