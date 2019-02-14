from customers.Aurora.clinical_test_result.clinical_test_result_mappings import (
    BASE, HIGH, LOW, PROC, STATUS_MAP, UNIT, VALUE)
from lib.master_fake_data_generator import FakeDataGenerator


class AURORAClinicalTestResultFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: int, file_size: int):
        f = self._faker
        r = self._random
        start, end = self.create_start_end_date()
        clinical_test_result = {
            "PAT_ID": f"{r.randint(1,file_size)}",
            "ORDER_PROC_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "LINE": f.random_number(),
            "PAT_ENC_CSN_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "RESULT_TIME": f"{start}T{self.get_time_string()}:000-05:00",
            "LAB_STATUS": f.random_element(list(STATUS_MAP)),
            "PROC_NAME": f.random_element(PROC),
            "BASE_NAME": f.random_element(BASE),
            "COMPONENT_ID": f.random_number(),
            "ORD_VALUE": f.random_element(VALUE),
            "ORD_NUM_VALUE": f"{round(r.uniform(0, 1000), 2)}",
            "REFERENCE_LOW": f.random_element(LOW),
            "REFERENCE_HIGH": f.random_element(HIGH),
            "REFERENCE_UNIT": f.random_element(UNIT),
            "RESULT_IN_RANGE_YN": f.random_element(['Y', 'N']),
            "PROCESS_EXTRACT_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00"
        }
        return clinical_test_result
