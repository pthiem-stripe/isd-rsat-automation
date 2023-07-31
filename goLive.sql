WITH mavenlink_emails AS (
	SELECT SPLIT(email_user_primary, ',') AS emails_array
	FROM Usertables.tsso_mavenlink_projects mavenlink
),
exploded AS (
	SELECT email
  FROM mavenlink_emails
  CROSS JOIN unnest(emails_array) AS t (email)
)
SELECT exp.email
, firstname, mavenlink.project_id
FROM restricted_sfdc_pii.opportunity_pii opp
JOIN Usertables.tsso_mavenlink_projects mavenlink
	ON opp.id = mavenlink.opportunity_id
JOIN restricted_sfdc_pii.contact_pii contact
	ON opp.accountid = contact.accountid
JOIN exploded exp
	ON exp.email = contact.email
WHERE (opp.implementation_plan = '#jumpstart' OR opp.implementation_plan = 'Implementation Service Desk (ISD)')
  AND mavenlink.project_status IN ('In Progress', 'Completed')
	AND actual_go_live_date between date '2023-04-01' and current_date
  AND deployment_end > date '2023-01-01'
  AND opp.stagename = 'Go Live'