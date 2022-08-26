class LineItem:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Header:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Detail:
    def __init__(self, line_items):
        self.line_items = line_items


class Invoice:
    def __init__(self, header: Header, detail: Detail):
        self.header = header
        self.detail = detail


class InvoiceParser:
    def __init__(self, data_dict):
        self.data_dict = data_dict
        self.invoices = []

    def parse_invoice_data(self):
        # Iterate over all invoice XML headers. Italiano vero XML headers below
        for inv in self.data_dict['Facturi']['Factura']:
            # Parse the Invoice Header info
            header = Header(**inv['Antet'])

            line_items = []
            inv_items = inv['Detalii']['Continut']
            # Parse all line items
            for li in inv_items['Linie']:
                line_item = LineItem(**li)
                line_items.append(line_item)

            detail = Detail(line_items)
            # Create an instance of the Invoice object
            invoice = Invoice(header, detail)
            # Append the Invoice to the list of invoice part of the loaded XML input
            self.invoices.append(invoice)
