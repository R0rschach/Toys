from datetime import datetime, timedelta

import evernote.edam.type.ttypes as EnTypes
from evernote.api.client import EvernoteClient


def convert_time(local_dt):
    delta = (local_dt - datetime.utcfromtimestamp(0)).total_seconds()
    return int(delta * 1000)


class MyBook():
    def __init__(self, dev_tok_file='dev_token.txt'):
        devtok = open(dev_tok_file, 'r').read().strip()
        self.token = devtok
        self.client = EvernoteClient(token=devtok, sandbox=False)
        self.user_store = self.client.get_user_store()
        self.note_store = self.client.get_note_store()
        pass

    def create_note(self, title, content, created=None):
        note = EnTypes.Note()
        note.title = title
        note.content = content
        if created:
            note.created = convert_time(created)
        created_note_guid = self.note_store.createNote(note)
        print('Created Note: %s' % created_note_guid)
