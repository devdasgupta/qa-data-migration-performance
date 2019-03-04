"""
    The below code is modified and incorporated from the existing CLoversub utilty used for fake data creation
"""

import importlib

import lib.common as common


class TestDataSetup:
    def __init__(self, customer, pipeline):
        self.customer = customer
        self.pipeline = pipeline

    def data_generator(self, number_records):
        customer = self.customer
        pipeline = self.pipeline
        customer_registered = common.registry.get(self.customer, None)

        if not customer_registered:
            print(f'ERROR: Could not find customer configuration for {customer}')
            exit()

        try:
            imported_module = importlib.import_module(
                ".fake_data_generator", package=f"{customer_registered['import_path']}.{pipeline}")
            pipeline_class = f"{customer.upper()}{common.pipeline_registry.get(pipeline)}FakeDataGenerator"
            converter_object = getattr(imported_module, pipeline_class)
        except ModuleNotFoundError as e:
            print(f"ERROR: Could not find customer {customer} configuration for the pipeline '{pipeline}'")
            print(e)
            exit()

        if converter_object:
            data_converter = converter_object(number_records)
            file_format = customer_registered['format']
            file_path = f"{customer_registered['import_path'].replace('.', '/')}/{pipeline}"
            data_converter.generate_fake_data(file_format, file_path)
        else:
            print(f'Could not find data generator for {customer}, {pipeline}')

        return f"{file_path}.{file_format}"


if __name__ == '__main__':
    main()