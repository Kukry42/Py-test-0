import docx, random
document = docx.Document('table.docx')
tables = document.tables
for table in tables:
    shaffeled_rows = list()
    for row in table.rows:
        shaffeled_rows.append(row)
    random.shuffle(shaffeled_rows)
    new_table = document.add_table(len(table.rows), len(table.columns))
    words_for_cells = list()
    for row in shaffeled_rows:
        for cell in row.cells:
            words_for_cells.append(cell.text)
    for row in new_table.rows:
        for cell in row.cells:
            cell.text = words_for_cells.pop()





document.save('table_shuffeled.docx')