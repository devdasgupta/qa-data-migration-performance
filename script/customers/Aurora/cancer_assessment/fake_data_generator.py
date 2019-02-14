from customers.Aurora.cancer_assessment.cancer_assessment_mappings import (
    BODY_SITE, HISTOLOGY, LYMPH, METASTASIS, PRIMARY_TUMOR, STAGE_GROUP)
from lib.master_fake_data_generator import FakeDataGenerator


class AURORACancerAssessmentFakeDataGenerator(FakeDataGenerator):

    def generate_pipeline_row(self, row: str, file_size: str) -> dict:
        f = self._faker
        r = self._random
        classification = f.random_element([('1', 'Clinical'), ('2', 'Pathologic'), ('', '')])
        cancer_assessment = {
            "PAT_ID": f"{r.randint(1,file_size)}",
            "STAGE_ID": f"{row+1}",
            "CONTACT_DATE_REAL": f"{f.random_number(5)}",
            "CLASSIFICATION_C": classification[0],
            "PROBLEM_LIST_ID": f"{r.randint(1,file_size)}",
            "PAT_ENC_CSN_ID": self.random_or_empty(f"{r.randint(1,int(file_size))}"),
            "BODY_SITE_NAME": f.random_element(list(BODY_SITE)),
            "HISTOPATHOLOGIC_TYPE_NAME": f.random_element(HISTOLOGY),
            "STAGING_DATE": self.random_or_empty(f.date()),
            "STAGE_METHOD_NAME": f.random_element(
                ["", 'Rai Staging System', 'AJCC 7th Edition', 'AJCC 6th Edition']),
            "CLASSIFICATION_NAME": classification[1],
            "PRIMARY_TUMOR_NAME": f.random_element(PRIMARY_TUMOR),
            "REGIONAL_LYMPH_NODES_NAME": f.random_element(LYMPH),
            "DISTANT_METASTASIS_NAME": f.random_element(METASTASIS),
            "STAGE_GROUP_NAME": f.random_element(list(STAGE_GROUP)),
            "PROCESS_EXTRACT_DTTM": f"{self.get_current_date()}:{r.randint(100,999)}-05:00",
        }
        return cancer_assessment
