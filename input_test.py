import win32com.client as win32

wordApp = win32.Dispatch('Word.Application')
wordApp.Visible = True
doc = wordApp.Documents.Open("C:\\Users\\LS Site Laptop\\Documents\\Python\\Tests_Generator_v1\\input_test.docx")

rng=doc.Bookmarks("title").Range
doc.Tables.Add(rng,NumRows=2,NumColumns=2)

