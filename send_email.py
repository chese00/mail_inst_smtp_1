import smtplib
import sys
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from read_template import read_template

HOST = 'HOST'
YOU = 'you@algo'
CC = 'cc@algo'
ME = '<me@algo>'
DIA = sys.argv[1:][0]
if not DIA.isnumeric():
    sys.exit()

def main():
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Día " + str(DIA) + ", inicio jornada"
    msg['From'] = ME
    msg['To'] = YOU
    msg['CC'] = CC
    html = read_template('message.txt')

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)

    # set up the SMTP server
    s = smtplib.SMTP(HOST)
    
    
    s.sendmail(ME, YOU, msg.as_string())
    s.send
    s.quit()

if __name__ == '__main__':
    main()