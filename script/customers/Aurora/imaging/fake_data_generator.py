from customers.Aurora.imaging.imaging_mappings import CODE, NAME, STATUS, TYPE_MAP
from lib.master_fake_data_generator import FakeDataGenerator


class AURORAImagingFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        start, end = self.create_start_end_date()
        imaging = {
            "PAT_ID": f"{r.randint(1,file_size)}",
            "ORDERING_CSN_ID": f.random_number(),
            "PERFORMING_CSN_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "ORDER_ID": f"{row+1}",
            "STUDY_STATUS": f.random_element(STATUS),
            "PROC_CAT_NAME": f.random_element(list(TYPE_MAP)),
            "PERFORMING_DEP_ID": f.random_number(),
            "PERFORMING_PROV_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "PROC_CODE": f.random_element(CODE),
            "PROC_NAME": f.random_element(NAME),
            "BEGIN_EXAM_DTTM": self.random_or_empty(f"{start}T{self.get_time_string()}:000-05:00"),
            "END_EXAM_DTTM": self.random_or_empty(f"{end}T{self.get_time_string()}:000-05:00"),
            "PROCESS_EXTRACT_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00",
        }
        return imaging
