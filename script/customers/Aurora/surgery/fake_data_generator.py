from customers.Aurora.surgery.surgery_mappings import PROC_NM
from lib.master_fake_data_generator import FakeDataGenerator


class AURORASurgeryFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        start, end = self.create_start_end_date()
        surgery = {
            "PAT_ID": f"{r.randint(1,file_size)}",
            "SURGERY_ID": f"{row+1}",
            "PAT_ENC_CSN_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "PROCEDURE_ID": f.random_number(),
            "PANEL": f.random_element(['1', '3', '2', '5', '4']),
            "PANEL_PRIMARY_PHYSICIAN_ID":  self.random_or_empty(f"{r.randint(1,file_size)}"),
            "PERFORMED_YN": f.random_element(['Y', 'N']),
            "PROCEDURE_NM": f.random_element(PROC_NM),
            "PATIENT_IN_ROOM_DTTM": self.random_or_empty(
                f"{start}T{self.get_time_string()}:000-05:00"),
            "PATIENT_OUT_ROOM_DTTM": self.random_or_empty(
                f"{end}T{self.get_time_string()}:000-05:00"),
            "PROCESS_EXTRACT_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00",
        }
        return surgery
