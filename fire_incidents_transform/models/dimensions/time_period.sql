select
    fire_incidents."ID" as "Incident ID",
    fire_incidents."Incident Date" as "Incident Occurrence",
    date(fire_incidents."Incident Date") as "Incident Date",
    extract(year from date(fire_incidents."Incident Date")) as "Incident Year",
    extract(month from date(fire_incidents."Incident Date")) as "Incident Month",
    extract(day from date(fire_incidents."Incident Date")) as "Incident Day"
from public."Fire_Incidents" as fire_incidents
order by
    1,
    4,
    5,
    6