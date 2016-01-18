from datetime import datetime, timedelta

import evernote.edam.type.ttypes as EnTypes
from evernote.api.client import EvernoteClient

notebook_dct = {'!nbox': 'cd9cb2e4-452e-4900-b494-dba98dfcbc1e',
                'Cabinet': '2ce80038-4c1f-4588-8a8b-2e93034521fb',
                'Connections': 'a6f78bbf-bbd8-43dc-ad36-7501d2c083f9',
                'J-Tour': 'e19eb69d-6a49-47b8-b516-127e48c801ac',
                'Memories': '8f5e65d6-0dd6-443c-bf35-e0be151a1711',
                'Personal': '923944ba-3d61-4db9-86c7-17bf060e79a7'}


def convert_time(local_dt):
    delta = (local_dt - datetime.utcfromtimestamp(0)).total_seconds()
    # dirty hack to solve the local time to utc problem... work for pst
    delta += + 3600*12
    return int(delta * 1000)


class MyBook():
    def __init__(self, dev_tok_file='dev_token.txt'):
        devtok = open(dev_tok_file, 'r').read().strip()
        self.token = devtok
        self.client = EvernoteClient(token=devtok, sandbox=False)
        self.user_store = self.client.get_user_store()
        self.note_store = self.client.get_note_store()
        pass

    def create_note(self, title, content, created=None, notebook_name=None):
        note = EnTypes.Note()
        note.title = title
        note.content = content
        if created:
            note.created = convert_time(created)
        if notebook_name:
            note.notebookGuid = notebook_dct[notebook_name]
        created_note_guid = self.note_store.createNote(note)
        print('Created Note: %s' % created_note_guid)
