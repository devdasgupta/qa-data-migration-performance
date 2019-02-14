from customers.Aurora.patient.patient_mappings import ETHNICITY, LANGUAGES, RACE
from lib.master_fake_data_generator import FakeDataGenerator


class AURORAPatientFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        deceased = f.random_element([True, False])
        patient_line = {
            "PAT_ID": f"{row+1}",
            "MRN": f"{f.random_number(10)}",
            "BIRTH_DATE": f.date(),
            "PATIENT_STATUS": 'Deceased' if deceased else 'Alive',
            "DEATH_DATE": (f"{f.date()}T{self.get_time_string()}:{r.randint(100,999)}-05:00"
                           )if deceased else "",
            "PAT_LAST_NAME": f.last_name(),
            "PAT_FIRST_NAME": f.first_name(),
            "PAT_MIDDLE_NAME": f.first_name(),
            "PAT_TITLE": f.random_element([
                '', 'Ms.', 'Rev.', 'Sr.', 'Fr.', 'Mrs.', 'Mr.', 'Dr.', 'Miss']),
            "PAT_NAME_SUFFIX": f.random_element(['', 'Jr.', 'Sr.', 'IV', 'II', 'III']),
            "SEX": f.random_element(["Unknown", "Female", "Male"]),
            "ADD_LINE_1": self.random_or_empty(f.street_address()),
            "ADD_LINE_2": self.random_or_empty("APT 123"),
            "CITY": self.random_or_empty(f.city()),
            "STATE": self.random_or_empty(f.state()),
            "ZIP": self.random_or_empty(f.postalcode()),
            "COUNTRY": self.random_or_empty("UNITED STATES"),
            "CONTACT_PHONE": f.phone_number(),
            "PRIMARY_ONC": self.random_or_empty(f"{r.randint(1,int(file_size))}"),
            "IS_ACTIVE": f.random_element(['Y', 'N']),
            "PATIENT_RACE": f.random_element(list(RACE)),
            "ETHNIC_GROUP": f.random_element(list(ETHNICITY)),
            "LANGUAGE": f.random_element(list(LANGUAGES)),
            "EMAIL_ADDRESS": f.email(),
            "DB_UPDATE_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00"

        }
        return patient_line
