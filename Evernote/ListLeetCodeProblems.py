import re

def GrabProblemList(html_file, dump_file):
    print('Read the LeetCode problem list html file: %s' % html_file)
    html = open(html_file, 'r').read()

    problems = re.compile(r'<a href="(https://leetcode.com/problems/.*)/">(.*)</a>').findall(html)
    nums = re.compile(r'<td>(\d+)</td>').findall(html)
    if len(problems) != len(nums):
        print('Number of problems does not match. Parsing Aborted')
        print('Number of Prolbems = %d ' % len(problems))
        print('Number of Problems = %d ' % len(nums))
        return
       
    fout = open(dump_file, 'w')
    for i in range(len(problems)):
        fout.write('\t'.join([nums[i], problems[i][0], problems[i][1]]))
        fout.write('\n')
    fout.close()
    print('%d problems found. Result dump to %s' % (len(problems), dump_file))


def PrepareNotes(dump_file, evernote_file):
    fout = open(evernote_file, 'w')
    for line in open(dump_file, 'r').readlines():
        idx, url, name = line.strip().split('\t')
        title = str.format('LeetCode {0:0>3}: {1}', idx, name)
        print(title)
        content = '<?xml version="1.0" encoding="UTF-8"?>'
        content += '<!DOCTYPE en-note SYSTEM ' \
               '"http://xml.evernote.com/pub/enml2.dtd">'
        content += str.format('<en-note><h2>Problem</h2><a href="{0}">{1}</a>', url, name)
        content += '<br/>'*10
        content += '<h2><b>Solution</b></h2>'
        content += '<ul><li></li></ul>'
        content += '</en-note>'
        fout.write('%s\t%s\n' % (title, content))
    fout.close()

if __name__ == '__main__':
    html_file = r'leetcode.html'
    dump_file = r'problem_list.tsv'
    evernote_file = r'notes.txt'

    GrabProblemList(html_file, dump_file)
    PrepareNotes(dump_file, evernote_file)
    
