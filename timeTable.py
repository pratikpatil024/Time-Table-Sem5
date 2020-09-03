import datetime 
import calendar
import webbrowser

day = calendar.day_name[datetime.date.today().weekday()]
print(day)

time = datetime.datetime.now()
time = time.strftime("%H:%M:%S")
print(time)

# print(datetime.date.today())

# if datetime.date.today() >= '2020-10-1' and datetime.date.today() <= '2020-11-20':
#   print(1)


# Monday
if day == 'Monday':

  # Computer Networks
  if time >= '08:25:00' and time <= '09:50:00':
    print('Computer Networks')
    webbrowser.open('https://iitbhilai.webex.com/meet/b203', new=2)

  # if datetime.date.today() >= '2020-10-12' and datetime.date.today() <= '2020-11-20':
    
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

  # Materials Chemistry 3
  if time >= '08:25:00' and time <= '09:50:00':
    print('Materials Chemistry 3')
    webbrowser.open('https://iitbhilai.webex.com/meet/b204', new=2)

  # Principles of Programming Languages
  if time >= '09:55:00' and time <= '11:20:00':
    print('Principles of Programming Languages')
    webbrowser.open('https://vcdot.cdot.in/vmeet/vis-3ph-hlx', new=2)

  # Data Analytics and Visualization
  if time >= '15:55:00' and time <= '17:20:00':
    print('Data Analytics and Visualization')
    webbrowser.open('https://iitbhilai.webex.com/meet/b203', new=2)


# Wednesday
if day == 'Wednesday':

  # Graph Theory and Applications
  if time >= '08:25:00' and time <= '09:50:00':
    print('Graph Theory and Applications')
    webbrowser.open('https://meet.google.com/jpb-whwn-vjj', new=2)

  # Materials Chemistry 3 Tutorial
  if time >= '09:55:00' and time <= '11:20:00':
    print('Materials Chemistry 3 Tutorial')
    webbrowser.open('https://iitbhilai.webex.com/meet/b204', new=2)

  # Computer Networks
  if time >= '11:25:00' and time <= '12:50:00':
    print('Computer Networks')
    webbrowser.open('https://iitbhilai.webex.com/meet/b203', new=2)
  
  # Concepts of Personality Psychology
  if time >= '15:55:00' and time <= '17:20:00':
    print('Concepts of Personality Psychology')
    webbrowser.open('https://iitbhilai.webex.com/meet/b204', new=2)


# Thursday
if day == 'Thursday':
  
  # Contemporary Indian Cinema: Beyond Bollywood
  if time >= '09:55:00' and time <= '11:20:00':
    print('Contemporary Indian Cinema: Beyond Bollywood')
    webbrowser.open('https://iitbhilai.webex.com/meet/b202', new=2)

  # Materials Chemistry 3
  if time >= '11:25:00' and time <= '12:50:00':
    print('Materials Chemistry 3')
    webbrowser.open('https://iitbhilai.webex.com/meet/b204', new=2)


# Friday
if day == 'Friday':

  # Principles of Programming Languages
  if time >= '08:25:00' and time <= '09:50:00':
    print('Principles of Programming Languages')
    webbrowser.open('https://vcdot.cdot.in/vmeet/vis-3ph-hlx', new=2)

  # Graph Theory and Applications
  if time >= '11:25:00' and time <= '12:50:00':
    print('Graph Theory and Applications')
    webbrowser.open('https://meet.google.com/jpb-whwn-vjj', new=2)

  # Concepts of Personality Psychology
  if time >= '15:55:00' and time <= '17:20:00':
    print('Concepts of Personality Psychology')
    webbrowser.open('https://iitbhilai.webex.com/meet/b204', new=2)