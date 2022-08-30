from openpyxl.styles import Font, Alignment


def write_to_cell(text: str, cell):
    cell.value = text
    cell.font = Font(name='Times New Roman')
    align_text(cell)


def align_text(cell):
    if cell.row == 11:  # Header row
        cell.alignment = Alignment(horizontal='center')
    elif cell.column > 19 and cell.row > 21:  # Line item numbers
        cell.alignment = Alignment(horizontal='right')
    else:  # Everything else
        cell.alignment = Alignment(horizontal='left')


def merge_cells(row_num, ws):
    col_ranges = (
        f'D{row_num}:E{row_num}',
        f'G{row_num}:T{row_num}',
        f'U{row_num}:V{row_num}',
        f'W{row_num}:Z{row_num}',
        f'AA{row_num}:AB{row_num}',
        f'AC{row_num}:AE{row_num}',
        f'AF{row_num}:AG{row_num}',
    )

    for col_range in col_ranges:
        ws.merge_cells(col_range)
