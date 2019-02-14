from customers.Aurora.performance_status.performance_status_mappings import PERF_VAL
from lib.master_fake_data_generator import FakeDataGenerator


class AURORAPerformanceStatusFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        start, end = self.create_start_end_date()
        performance_status = {
            "PAT_ID": f"{r.randint(1,file_size)}",
            "DB_UPDATE_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00",
            "HLV_ID": f"{row+1}",
            "ENC_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "STATUS": "Final",
            "PERF_STAT_DTTM": f"{start}T{self.get_time_string}:000-05:00",
            "PERF_STATUS_TYPE": 'ONCOLOGY - PERFORMANCE STATUS',
            "PERF_VAL": f.random_element(PERF_VAL)
        }
        return performance_status
