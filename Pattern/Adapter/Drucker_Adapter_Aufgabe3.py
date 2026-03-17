class AlterDrucker:
    def print_text(self, text):
        return f"Drucke Text: {text}"


class Dokument:
    def __init__(self, inhalt):
        self.inhalt = inhalt


class DruckerAdapter:
    def __init__(self, alter_drucker):
        self.alter_drucker = alter_drucker

    def print_document(self, doc_object):
        return self.alter_drucker.print_text(doc_object.inhalt)


alter_drucker = AlterDrucker()
adapter3 = DruckerAdapter(alter_drucker)

dokument1 = Dokument("Hallo, das ist ein Testdokument.")
print(adapter3.print_document(dokument1))