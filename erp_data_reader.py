import os
from pathlib import Path
import xmltodict
from models.erp_models import InvoiceParser

# Config path to directories
project_directory = Path(os.path.dirname(os.path.abspath(__file__)))
input_directory = Path(project_directory / 'input')

for file in input_directory.iterdir():
    if file.suffix == '.xml':
        # Open read the XML file into a dictionary
        with open(file) as fd:
            xml_doc = xmltodict.parse(fd.read())

        # Create an instance of the InvoiceParser object with the dictionary data
        invoice_parser = InvoiceParser(xml_doc)

        # Try to parse the XML file into an Invoice object(s)
        try:
            invoice_parser.parse_invoice_data()
        except Exception as ex:
            raise ValueError('Error parsing the data!')
