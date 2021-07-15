import docx
document = docx.Document()
par = document.add_paragraph('Lolem Ipsum')
par_above = par.insert_paragraph_before('Some text at the beginning')
table = document.add_table(rows = 6, cols = 2)
cell = table.cell(0, 0)
cell.text = 'видеть'
row = table.rows[1]
row.cells[0].text = 'думать'
row.cells[1].text = 'thinc'
document.save('document.docx')