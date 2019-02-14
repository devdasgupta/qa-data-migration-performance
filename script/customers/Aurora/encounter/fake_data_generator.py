from customers.Aurora.encounter.encounter_mappings import ENCOUNTER_TYPE, FACILITY, ICD9, ICD10, LINE, STATUS
from lib.master_fake_data_generator import FakeDataGenerator


class AURORAEncounterFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        start, end = self.create_start_end_date()
        upcoming = f.random_element([True, False])
        encounter = {
            "PAT_ID": f"{r.randint(1,file_size)}",
            "ICD9_CODE": f.random_element(ICD9),
            "ICD10_CODE": f.random_element(ICD10),
            "DB_UPDATE_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00",
            "PAT_ENC_CSN_ID": f"{row+1}",
            "ENC_START": f"{start}T{self.get_time_string()}.000-05:00",
            "ENC_END": f"{end}T{self.get_time_string()}.000-05:00" if not upcoming else "",
            "ENC_STATUS": (f.random_element(list(STATUS['Upcoming']))
                           ) if upcoming else f.random_element(list(STATUS['Encounter'])),
            "ENC_TYPE": f.random_element(list(ENCOUNTER_TYPE)),
            "PRIM_ENC_PROV_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "LINE": f.random_element(LINE),
            "FACILITY": f.random_element(FACILITY),
            "DEPARTMENT_ID":  self.random_or_empty(f.random_number(5)),
            "DEPARTMENT_NAME":  self.random_or_empty(f.word().upper())
        }
        return encounter
