from cloversub import DataAcquisition
from customers.Aurora.provider.provider_mappings import property_key_map, provider_type_map
from lib.transformers import check_integer, map_property_keys


class Provider(DataAcquisition):

    def process_row(self, row, file_name: str) -> dict:
        row = map_property_keys(property_key_map, row)

        # message should be rejected if there is no client_id
        if not row['client_id'] or not row['extract_date']:
            print("At least one required field missing (client_id or extract_date)")
            return {}

        # check if npi has value and is int
        row = check_integer(row, 'npi', 'Provider')

        row["provider_type"] = provider_type_map.get(row["provider_type"], "")
        row['affiliations'] = ['Aurora Health Care']
        row['client_id'] = f"Provider:{row['client_id']}"
        row["extract_date"] = row["extract_date"][:19] + row["extract_date"][23:]

        row['meta'] = {
            'extract_date': row.pop("extract_date"),
            'source': f"{file_name}.csv",
            'source_format': "EDW",
            'cloverleaf_id': ''
        }

        return {
            "model": "careprovider",
            "fields": row,
        }
