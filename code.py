import docx, random
document = docx.Document('table.docx')
tables = document.tables
for table in tables:
    shaffeled_rows = list()
    empty_rows = list()
    for row in table.rows:
        row_text_list = list()
        for cell in row.cells:
            row_text_list.append(cell.text)
        if  all(row_text_list):
            shaffeled_rows.append(row)   
        else:
            empty_rows.append(row)
    random.shuffle(shaffeled_rows)
    words_for_cells = list()
    for row in shaffeled_rows:
        for cell in row.cells:
            words_for_cells.append(cell.text)
    for row in table.rows:
        for cell in row.cells:
            try:
                cell.text = words_for_cells.pop()
            except:
                pass





document.save('table_shuffeled.docx')