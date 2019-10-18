def input(template_path, test):

    import win32com.client as win32

    wordApp = win32.Dispatch('Word.Application')
    wordApp.Visible = True
    doc = wordApp.Documents.Open(template_path)

    rng=doc.Bookmarks(test).Range

    #need to put in code to add graph after bookmark

