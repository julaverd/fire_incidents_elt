select
    fire_incidents."Battalion" as "Battalion",
    count(*) as "Incidents Per Battalion"
from public."Fire_Incidents" as fire_incidents
group by
    1
order by
    2 desc
