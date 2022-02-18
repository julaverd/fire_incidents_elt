select
    fire_incidents."neighborhood_district" as "Disctrict",
    count(*) as "Incidents Per District"
from public."Fire_Incidents" as fire_incidents
group by
    1
order by
    2 desc
