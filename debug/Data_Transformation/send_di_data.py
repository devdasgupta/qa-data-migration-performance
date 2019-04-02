from graphite_activity import Graphite
from db_activity import Database
import config as c

LIVE_TABLES = [
        "careprovider",
        "clinicaltestresult",
        "coverage",
        "department",
        "diagnosis",
        "encounter",
        "imaging",
        "imagingstudy",
        "medication",
        "medicationadmin",
        "medicationorder",
        #"order",
        "pathologyreport",
        "order_staging",
        "patient",
        "patientcondition",
        "performancestatus",
        "protocol",
        "providerrole",
        "radiation",
        "surgery",
        "testrequest",
        "treatmentplan",
        "tumorassessment",
        "tumorstaging"
        ]

STAGE_TABLES = [
        "careprovider_staging",
        "clinicaltestresult_staging",
        "coverage_staging",
        "department_staging",
        "imagingstudy_staging",
        "encounter_staging",
        "diagnosis_staging",
        "imaging_staging",
        "medication_staging",
        "medicationadmin_staging",
        "medicationorder_staging",
        "pathologyreport_staging",
        "patient_staging",
        "patientcondition_staging",
        "performancestatus_staging",
        "protocol_staging",
        "providerrole_staging",
        "radiation_staging",
        "surgery_staging",
        "testrequest_staging",
        "treatmentplan_staging",
        "tumorassessment_staging",
        "tumorstaging_staging"
        ]


def send_records(path, db, table_list):

    graph = Graphite(c.GRAPHITE_ENDPOINT, 2003)

    for table in table_list:
        count = db.count_records(table)
        graph.send_message(path, table, count)

    del graph


if __name__ == '__main__':
    di_db = Database('syapse_di_dev')

    send_records('Data_Ingestion.syapse_di.Live', di_db, LIVE_TABLES)
    send_records('Data_Ingestion.syapse_di.Stage', di_db, STAGE_TABLES)

    del di_db
