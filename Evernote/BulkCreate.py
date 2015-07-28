import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient
import sys


def ListNotebooks(note_store):
    notebooks = note_store.listNotebooks()
    print("Found ", len(notebooks), " notebooks:")
    for notebook in notebooks:
        print("  * ", notebook.name)

def CreateNote(title, content, note_store):
    note = Types.Note()
    note.title = title
    note.content = content
    created_note_guid = note_store.createNote(note)
    print('Created Note: %s' % created_note_guid)

if __name__ == '__main__':
    import re
    if len(sys.argv) != 3:
        print('Usage: BulkCreate.py dev_token_file notes_file')
        print('dev_token_file: A text file with the dev_token from https://dev.evernote.com/doc/articles/dev_tokens.php')
        print('ntoes_file: A tsv with 2 columns: title and content')
    print('Read the dev token')
    devtok = open(sys.argv[1],'r').read().strip()
    
    print('The dev token will be used:\n', devtok)
    client = EvernoteClient(token=devtok, sandbox = False)

    user_store = client.get_user_store()
    note_store = client.get_note_store()

    print('Load the notes to be created from %s' % sys.argv[2])
    for line in open(sys.argv[2], 'r'):
        title, content = line.strip().split('\t')
        print(title)
        CreateNote(title, content, note_store)    
