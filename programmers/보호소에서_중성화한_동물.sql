select ins.animal_id, ins.animal_type, ins.name
from animal_ins as ins
join animal_outs as outs
on ins.animal_id = outs.animal_id and ins.sex_upon_intake != outs.sex_upon_outcome
where ins.sex_upon_intake like 'Intact%'
order by ins.animal_id