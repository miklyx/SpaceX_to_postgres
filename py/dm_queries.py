DM_MISSIONS = """CREATE TABLE DM_MISSIONS_PUBLICATIONS AS
	select l.mission_name, m.name as mision_class,
	case when h.article is not null then 1 else 0 end +
	case when h.reddit is not null then 1 else 0 end +
	case when h.wikipedia  is not null then 1 else 0 end as publications_count
	from launches l 
	left join missions m on l.mis_id = m.id
	left join histories h on h.flight_id = l.id"""

DM_ROCKETS = """CREATE TABLE DM_ROCKETS_PUBLICATIONS AS
select r.name as rocket_name,
sum(case when h.article is not null then 1 else 0 end +
case when h.reddit is not null then 1 else 0 end +
case when h.wikipedia  is not null then 1 else 0 end) as publications_count
from rockets r
left join launches l on l.rocket_id = r.id
left join histories h on h.flight_id = l.id
group by r.name
"""

DM_LAUNCHES = """CREATE TABLE DM_LAUNCHES_PUBLICATIONS AS
select l.launch_year, l.launch_date_local,
sum(case when h.article is not null then 1 else 0 end +
case when h.reddit is not null then 1 else 0 end +
case when h.wikipedia  is not null then 1 else 0 end) as publications
from launches l
left join histories h on h.flight_id = l.id
group by l.launch_year, l.launch_date_local
"""
