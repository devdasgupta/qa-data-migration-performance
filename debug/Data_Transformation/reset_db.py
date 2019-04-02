from db_activity import Database


if __name__=='__main__':
	pds_db = Database('syapse_apps_pds_dev')
	pds_db.delete_from_table('ps_dependency')
	pds_db.delete_from_table("ont_record", "kb_class NOT IN ('syckb:Medication', 'syckb:ClinicalTrial');")

	del pds_db

	sy_apps = Database('syapse_apps_dev')
	sy_apps.delete_from_table('data_transformation_waitingrelationship')
	sy_apps.delete_from_table('data_transformation_waitingrecord')

	del sy_apps
