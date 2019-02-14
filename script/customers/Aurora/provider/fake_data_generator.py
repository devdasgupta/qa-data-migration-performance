from customers.Aurora.provider.provider_mappings import CREDENTIALS, provider_type_map
from lib.master_fake_data_generator import FakeDataGenerator


class AURORAProviderFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        provider_line = {
            "PROV_ID": f"{row + 1}",
            "PROV_NAME": f.name(),
            "CREDENTIALS": f.random_element(CREDENTIALS),
            "NPI": self.random_or_empty(f.random_number(10)),
            "PROV_TYPE": f.random_element(list(provider_type_map)),
            "PROCESS_EXTRACT_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00"
        }
        return provider_line
