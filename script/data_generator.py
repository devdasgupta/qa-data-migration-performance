import argparse
import importlib

import lib.common as common


def process_args():
    parser = argparse.ArgumentParser(description='Fake Data generator for Interop')
    parser.add_argument('customer', help='customer name')
    parser.add_argument('pipeline', help='record type')
    parser.add_argument(
        '--count', type=int, help='number of records to create (default 1)')
    arguments = parser.parse_args()
    return arguments


def main():
    """Create fake data for a specific customer's pipeline"""
    # arguments = process_args()
    # customer = arguments.customer.lower()
    # pipeline = arguments.pipeline.lower()
    # number_records = arguments.count
    customer = 'aurora'
    pipeline = 'patient'
    number_records = 2

    customer_registered = common.registry.get(customer, None)
    print(customer_registered)
    if not customer_registered:
        print(f'ERROR: Could not find customer configuration for {customer}')
        exit()

    # importlib.import_module("fake_data_generator",package=)
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


if __name__ == "__main__":
    main()
