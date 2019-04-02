from customers.Aurora.test_order.test_order_mappings import LAB_NAME, PROC_NAME, STATUS
from lib.master_fake_data_generator import FakeDataGenerator


class AURORATestOrderFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        start, end = self.create_start_end_date()
        test_order = {
            "ORDER_PROC_ID": f"{row+1}",
            "PAT_ID": f"{r.randint(1,file_size)}",
            "PAT_ENC_CSN_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "AUTHRZING_PROV_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "PRIMARY_DEPT_ID": self.random_or_empty(f.random_number()),
            "BILLING_PROV_ID": self.random_or_empty(f.random_number()),
            "INS_CVG_ACCT": self.random_or_empty(f.random_number()),
            "LAB_NAME": f.random_element(LAB_NAME),
            "PROC_NAME": f.random_element(PROC_NAME),
            "ORDER_TIME": f"{start}T{self.get_time_string()}:000-05:00",
            "LAB_STATUS": f.random_element(list(STATUS)),
            "DB_UPDATE_DTTM":  f"{self.get_current_date()}:{r.randint(100,999)}-05:00",
        }
        return test_order
