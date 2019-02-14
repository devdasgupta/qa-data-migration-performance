from customers.Aurora.protocol.protocol_mappings import NAME, RXNORM
from lib.master_fake_data_generator import FakeDataGenerator


class AURORAProtocolFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        protocol = {
            "PROTOCOL_ID": f"{row+1}",
            "DISPLAY_NAME": f.random_element(NAME),
            "MED_ID": f"{f.random_number(5)}",
            "PRL_STATUS": f.random_element([
                '', 'RETIRED', 'RELEASED', 'RELEASED FOR TESTING', 'UNRELEASED']),
            "PROCESS_EXTRACT_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00",
            "CONTACT_DATE_REAL": f"{f.random_number(5)}",
            "PROC_ID": f"{f.random_number(5)}",
            "RXNORM_CODE": f.random_element(RXNORM)
        }
        return protocol
