SELECT
v.*
from visits_main v
left join accounts a on v.account_id = a.id