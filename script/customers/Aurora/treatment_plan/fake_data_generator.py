from lib.master_fake_data_generator import FakeDataGenerator


class AURORATreatmentPlanFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        start, end = self.create_start_end_date()
        treatment_plan = {
            "PAT_ID": f"{r.randint(1,file_size)}",
            "TREATMENT_PLAN_ID": f"{row+1}",
            "PROTOCOL_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "PLAN_START_DATE": f"{start}T{self.get_time_string()}:000-05:00",
            "PLAN_DISCON_DATETIME": self.random_or_empty(
                f"{end}T{self.get_time_string()}:000-05:00"),
            "DISPLAY_NAME": f.word().upper(),
            "CREATED_ON_TM": f"{start}T{self.get_time_string()}.000-05:00",
            "TPL_PROVIDER_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "PLAN_DISCON_REASON_NAME": f.word().upper(),
            "TREATMENT_GOAL_NAME": f.word().upper(),
            "PROCESS_EXTRACT_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00",
            "PROTOCOL_CONTACT_DATE_REAL": f"{f.random_number(5)}"
        }
        return treatment_plan
