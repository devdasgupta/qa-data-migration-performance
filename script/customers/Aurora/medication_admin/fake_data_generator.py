from customers.Aurora.medication_admin.medication_admin_mappings import (
    DISCONT_REASON, DOSE, MAR_ACTION, MAR_DURATION, REASON, SITE, UNIT)
from lib.master_fake_data_generator import FakeDataGenerator


class AURORAMedicationAdminFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        start, end = self.create_start_end_date()
        medication_admin = {
            "PAT_ID": f"{r.randint(1,int(file_size))}",
            "ORDER_MED_ID": f"{r.randint(1,int(file_size))}",
            "LINE": f.random_number(),
            "PAT_ENC_CSN_ID": self.random_or_empty(f"{r.randint(1,int(file_size))}"),
            "MEDICATION_ID": f.random_number(5),
            "SCHEDULED_TIME": self.random_or_empty(f"{start}T{self.get_time_string()}:000-05:00"),
            "TAKEN_TIME": self.random_or_empty(f"{start}T{self.get_time_string()}:000-05:00"),
            "DOSE_VALUE": f.random_element(DOSE),
            "DOSE_UNIT": f.random_element(UNIT),
            "MAR_ACTION": f.random_element(list(MAR_ACTION)),
            "REASON": f.random_element(REASON),
            "SITE": f.random_element(SITE),
            "MAR_DURATION": f.random_element(MAR_DURATION),
            "DURATION": f.random_element(['', 'Hours', 'Minutes', 'Days']),
            "DISCON_TIME": self.random_or_empty(f"{end}T{self.get_time_string()}:000-05:00"),
            "RSN_FOR_DISCON": f.random_element(DISCONT_REASON),
            "PROCESS_EXTRACT_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00",
        }
        return medication_admin
