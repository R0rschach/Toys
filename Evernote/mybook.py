import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as EnTypes

from evernote.api.client import EvernoteClient
import sys
import time
from datetime import datetime, timedelta

def convert_time(local_dt):
    delta = (datetime.utcfromtimestamp(local_dt.timestamp()) - datetime(1970, 1, 1))
    stamp = delta / timedelta(milliseconds = 1)
    return int(stamp)

class MyBook():
    def __init__(self, dev_tok_file = 'dev_token.txt'):
        devtok = open(dev_tok_file,'r').read().strip()

        self.client = EvernoteClient(token = devtok, sandbox = False)
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







