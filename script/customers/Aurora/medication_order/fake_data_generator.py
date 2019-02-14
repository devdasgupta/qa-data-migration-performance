from customers.Aurora.medication_order.medication_order_mappings import (
    DISCRETE_DOSE, DOSE_UNIT, FREQUENCY, QUANTITY, REFILLS, RX_MEDS, STATUS)
from lib.master_fake_data_generator import FakeDataGenerator


class AURORAMedicationOrderFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: int) -> dict:
        f = self._faker
        r = self._random
        start, end = self.create_start_end_date()
        rx, med = f.random_element(RX_MEDS)
        medication_order = {
            "PAT_ID": f"{r.randint(1,file_size)}",
            "DB_UPDATE_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00",
            "ORDER_MED_ID": f"{row+1}",
            "PAT_ENC_CSN_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "RXNORM_CODE": rx,
            "MEDICATION_ID": f.random_number(5),
            "ORDER_INST": f"{start}T{self.get_time_string()}:000-05:00",
            "ORDER_START_TIME": f"{start}T{self.get_time_string()}:000-05:00",
            "ORDER_END_TIME": self.random_or_empty(f"{end}T{self.get_time_string()}:000-05:00"),
            "AUTHRZING_PROV_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "DESCRIPTION": med,
            "TREATMENT_PLAN_ID": self.random_or_empty(f"{r.randint(1,file_size)}"),
            "FREQ_NAME": f.random_element(FREQUENCY),
            "MED_ROUTE": self.random_or_empty(f.word()),
            "HV_DISCRETE_DOSE": f.random_element(DISCRETE_DOSE),
            "DOSE_UNIT": f.random_element(DOSE_UNIT),
            "ORDER_STATUS": f.random_element(list(STATUS)),
            "ORDER_MODE": f.random_element(['', 'Inpatient', 'Outpatient']),
            "PRN_YN": f.random_element(['', 'Y', 'N']),
            "SIG": self.random_or_empty(f.sentence()),
            "QUANTITY": f.random_element(QUANTITY),
            "DOSAGE": '',
            "REFILLS": f.random_element(REFILLS),
            "DISP_AS_WRITTEN_YN": '',
            "DISCON_REASON": self.random_or_empty(f.sentence())
        }
        return medication_order
