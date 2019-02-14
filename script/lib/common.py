import yaml

CONFIGURATION_FILE = 'cloversub.yaml'
FAKER_SEED = 2018

registry = {
    'chi': {'import_path': 'customers.PMA.CHI', 'format': 'csv'},
    'dh': {'import_path': 'customers.PMA.DH', 'format': 'json'},
    'providence': {'import_path': 'customers.Providence', 'format': 'json'},
    'aurora': {'import_path': 'customers.Aurora', 'format': 'csv'},
}

pipeline_registry = {
    'encounter': "Encounter",
    'patient': "Patient",
    'medication_admin': "MedicationAdmin",
    'medication_order': "MedicationOrder",
    'provider': "Provider",
    'test_order': "TestOrder",
    'tumor_assessment': "CancerAssessment",
    'cancer_assessment': "CancerAssessment",
    'patient_condition': "PatientCondition",
    'clinical_test_result': "ClinicalTestResult",
    'treatment_plan': "TreatmentPlan",
    'protocol': "Protocol",
    'surgery': "Surgery",
    'procedure_order': "ProcedureOrder",
    'performance_status': "PerformanceStatus",
    'imaging': "Imaging",
    'department': "Department",
}


def load_configuration():
    with open(CONFIGURATION_FILE, 'r') as config_file:
        cfg = yaml.load(config_file)
        return cfg
