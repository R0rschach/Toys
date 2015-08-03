from datetime import datetime, timedelta
import sys
import mybook

def create_daily_journal(date, content = ''):
    """
    Create a daily journal of given date. 
    Creation time will be equal to the date. 

    @date: datetime object
    @content: string, when empty, load from local template
    @return:  (title, content, created_time)
    """
    title = date.strftime('%Y.%m.%d')
    if not content:
        content = open('template.daily_journal.html','r').read()
    return (title, content, date) 

def create_weekly_summary(date, content = ''):
    """
    Create a weekly summary journal of given date. 
    Creation time will be equal to the date. 

    @date: datetime object
    @content: string, when empty, load from local template
    @return:  (title, content, created_time)
    """
    title = date.strftime('%Y.%m.%d Weekly Summary')
    if not content:
        content = open('template.weekly_summary.html','r').read()
    return (title, content, date)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Generate journals template for next 7 days')
        mybook = mybook.MyBook()

        dt = datetime.today()
        dt = datetime(dt.year, dt.month, dt.day)
        end = dt + timedelta(days=7)
        while dt <= end:
            print('Create Daily Journal: %s' % dt.strftime('%Y-%m-%d'))
            title, content, created = create_daily_journal(dt)
            mybook.create_note(title, content, created=created)
            if dt.weekday() == 6:
                print('Create Weely Summary: %s' % dt.strftime('%Y-%m-%d'))
                title, content, created = create_weekly_summary(dt+timedelta(seconds=1))
                mybook.create_note(title, content, created=created)
            dt += timedelta(days=1)
