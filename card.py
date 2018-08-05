class Card:

    def __init__(self, marvel_token, project_pk, offset_comment):
        self.marvel_token = marvel_token
        self.project_pk = project_pk
        self.offset_comment = offset_comment
        self.comment_cursors = {}
        self.old_modifiedAt_project = 0  # globalna spremenljivka za cekiranje na marvel strani
        self.old_modifiedAt_screen = None  # globalna spremenljivka za cekiranje na marvel strani
        self.screen_list = []

    def change_marvel_token(self, marvel_token):
        self.marvel_token = marvel_token

    def change_project_pk(self, project_pk):
        self.project_pk = project_pk

    def change_offset_comment(self, offset_comment):
        self.offset_comment = offset_comment

    def change_old_modifiedAt_screen(self, old_modifiedAt_screen):
        self.old_modifiedAt_screen = old_modifiedAt_screen

    def has_required_data(self):
        if self.marvel_token is not None and self.project_pk is not None:
            return True
        else:
            return False
