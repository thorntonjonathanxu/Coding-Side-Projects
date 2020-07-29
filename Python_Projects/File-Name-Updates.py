import os
from datetime import datetime

for filename in os.listdir('C:\\Users\\thorntonj1\\Downloads\\Bank Statements'):

    #Current date format'%B %d, %y' needs to be '%y-%m-%d - Acct 4461 Statement.pdf'
    # print(filename[:-4])
    dt_str = filename[:-4]
    foo = datetime.strptime(dt_str,'%B %d, %Y')
    dst = str(foo.date()) + ' - Acct 0074 Statement.pdf'
    src = 'C:\\Users\\thorntonj1\\Downloads\\Bank Statements\\' + filename
    os.rename(src, dst)
    print("Completed")