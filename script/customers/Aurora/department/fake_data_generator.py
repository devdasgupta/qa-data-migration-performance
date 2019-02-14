from customers.Aurora.department.department_mappings import NAME, SPECIALTY
from lib.master_fake_data_generator import FakeDataGenerator


class AURORADepartmentFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        department = {
            "PROCESS_EXTRACT_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00",
            "DEPARTMENT_ID": f"{row+1}",
            "DEPARTMENT_NAME": f.random_element(NAME),
            "SPECIALTY": f.random_element(SPECIALTY)
        }
        return department
