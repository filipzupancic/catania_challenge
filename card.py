class Card:

    def __init__(self, marvel_token, project_pk, offset_comment):
        self.marvel_token = marvel_token
        self.project_pk = project_pk
        self.offset_comment = offset_comment
        self.comment_cursors = {}
        self.old_modifiedAt = None  # globalna spremenljivka za cekiranje na marvel strani

    def change_marvel_token(self, marvel_token):
        self.marvel_token = marvel_token

    def change_project_pk(self, project_pk):
        self.project_pk = project_pk

    def change_offset_comment(self, offset_comment):
        self.offset_comment = offset_comment

    def change_old_modifiedAt(self, old_modifiedAt):
        self.old_modifiedAt = old_modifiedAt

    def has_required_data(self):
        if self.marvel_token is not None and self.project_pk is not None:
            return True
        else:
            return False
