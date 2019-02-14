from customers.Aurora.procedure_order.procedure_order_mappings import STATUS, TYPE_MAP
from lib.master_fake_data_generator import FakeDataGenerator


class AURORAProcedureOrderFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        procedure_order = {
            "PAT_ID": f"{r.randint(1,file_size)}",
            "DB_UPDATE_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00",
            "PAT_ENC_CSN_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "AUTHRZING_PROV_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "ORDER_PROC_ID": f"{row+1}",
            "BILLING_PROV_ID": self.random_or_empty(f.random_number()),
            "INS_CVG_ACCT": self.random_or_empty(f.random_number()),
            "PROC_NAME": f.random_element(list(TYPE_MAP)),
            "ORDER_TIME": f"{f.date()}T{self.get_time_string()}:000-05:00",
            "ORDER_STATUS": f.random_element(list(STATUS))
        }
        return procedure_order
