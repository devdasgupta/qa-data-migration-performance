from customers.Aurora.encounter.encounter_mappings import ICD9, ICD10
from customers.Aurora.patient_condition.patient_condition_mappings import NAME
from lib.master_fake_data_generator import FakeDataGenerator


class AURORAPatientConditionFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        start, end = self.create_start_end_date()
        diagnosis = {
            "PROBLEM_LIST_ID": f"{row+1}",
            "PAT_ID": f"{r.randint(1,file_size)}",
            "RECORDED_DATE": self.random_or_empty(start),
            "ONSET_DATE": self.random_or_empty(start),
            "RESOLVED_DATE": self.random_or_empty(end),
            "ICD9_CODE": f.random_element(ICD9),
            "ICD10_CODE": f.random_element(ICD10),
            "DX_NAME": f.random_element(NAME),
            "SEVERITY": f.random_element(['', 'High', 'Low', 'Medium']),
            "PROB_STATUS": f.random_element(['Active', 'Resolved']),
            "DB_UPDATE_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00",
        }
        return diagnosis
