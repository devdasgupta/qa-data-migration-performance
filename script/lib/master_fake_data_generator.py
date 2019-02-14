import json
import os.path
import secrets
from abc import ABC, abstractmethod
from csv import DictWriter
from datetime import datetime

from faker import Faker

from lib.common import FAKER_SEED


class FakeDataGenerator(ABC):
    """
        Abstract  Data Generator class, subclasses needs to implement
        the generate_pipeline_row method specific for each customer.
    """

    def __init__(self, number_records: int = 0):
        self._records_count = number_records if number_records else 1
        self._faker = Faker()
        self._faker.random.seed(FAKER_SEED)
        self._random = secrets.SystemRandom()

    @abstractmethod
    def generate_pipeline_row(row, file_size):
        pass

    def generate_fake_data(self, file_type: str, path: str):
        output_file = self.generate_output_file(path, self._records_count, file_type)
        print(f"Start: {output_file}")
        final_list = []
        for i in range(self._records_count):
            line = self.generate_pipeline_row(i, self._records_count)
            final_list.append(line)

        if file_type == "csv":
            self.output_csv(final_list, output_file)
        else:
            self.output_json(final_list, output_file)
        print(f"Done: {output_file}")

    def generate_output_file(self, path: str, file_length: int, file_type: str) -> str:
        pipeline = path.split('/')[-1]
        file_name = f'{pipeline}_{file_length}.{file_type}'
        output_file = ""
        while not output_file:
            # file = f'cloversub/{path}/input_files/{file_name}'
            file = f'script/input_files/{file_name}'
            if os.path.isfile(file):
                print(f"File '{file}' already exists")
                override = input("Do you want to override file (Y/N)? ")
                if override.lower() in ("n", "no"):
                    file_name = input("Please give another file name: ")
                else:
                    output_file = file
            else:
                output_file = file
        return output_file

    def output_json(self, final_list, output_file):
        with open(output_file, "w") as handle:
            for obj in final_list:
                handle.write(json.dumps(obj))
                handle.write('\n')

    def output_csv(self, final_list, output_file):
        with open(output_file, 'w') as handle:
            writer = DictWriter(handle, fieldnames=final_list[0].keys())
            writer.writeheader()
            writer.writerows(final_list)

    def create_start_end_date(self):
        date = self._faker.date()  # 2017-09-16 format
        end_month = f"{int(date[5:7]) + 1}" if int(date[5:7]) < 12 else "01"
        if len(end_month) == 1:
            end_month = f"0{end_month}"
        end_date = f"{date[:5]}{end_month}{date[7:]}"

        return date, end_date

    def random_or_empty(self, element, empty=''):
        return self._faker.random_element([element, empty])

    def get_current_date(self):
        return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')

    def get_time_string(self):
        return f"{self._random.randint(10,99)}:{self._random.randint(10,99)}:{self._random.randint(10,99)}"
