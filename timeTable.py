import datetime 
import calendar
import webbrowser

day = calendar.day_name[datetime.date.today().weekday()]
print(day)

time = datetime.datetime.now()
time = time.strftime("%H:%M:%S")
print(time)


# Monday
if day == 'Monday':

  # Computer Networks
  if time >= '08:25:00' and time <= '09:50:00':
    print('Computer Networks')
    webbrowser.open('https://iitbhilai.webex.com/meet/b203', new=2)

  # Contemporary Indian Cinema: Beyond Bollywood
  if time >= '11:25:00' and time <= '12:50:00':
    print('Contemporary Indian Cinema: Beyond Bollywood')
    webbrowser.open('https://iitbhilai.webex.com/meet/b202', new=2)

  # Data Analytics and Visualization
  if time >= '14:25:00' and time <= '15:50:00':
    print('Data Analytics and Visualization')
    webbrowser.open('https://iitbhilai.webex.com/meet/b203', new=2)


# Tuesday
if day == 'Tuesday':
webbrowser.open('', new=2)
webbrowser.open('', new=2)

# Wednesday
if day == 'Wednesday':
  webbrowser.open('', new=2)
  webbrowser.open('', new=2)
  webbrowser.open('', new=2)

# Thursday
if day == 'Thursday':

  # for 5-6 fractal
  # if time >= '09:55:00' and time <= '11:20:00' :
  #   webbrowser.open('https://iitbhilai.webex.com/meet/b202', new=2)

# Friday
if day == 'Friday':
  webbrowser.open('', new=2)
  webbrowser.open('', new=2)
  webbrowser.open('', new=2)