select
    fire_incidents."Battalion" as "Battalion",
    count(*) as "Incidents Per Battalion"
from public.Fire_Incidents
group by
    1
order by
    2 desc
