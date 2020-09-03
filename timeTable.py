import datetime 
import calendar
import webbrowser

day = calendar.day_name[datetime.date.today().weekday()]
# print(day)

time = datetime.datetime.now()
time = time.strftime("%H:%M:%S")
# print(time)

dateToday = datetime.datetime.now()
dateToday = dateToday.strftime("%Y-%m-%d")
# print(dateToday)

if dateToday >= '2020-07-28' and dateToday <= '2020-08-28':
  print('Fractal 1-2 in progress')
if dateToday >= '2020-09-03' and dateToday <= '2020-10-06':
  print('Fractal 3-4 in progress')
if dateToday >= '2020-10-01' and dateToday <= '2020-11-20':
  print('Fractal 5-6 in progress')


####################################################################################################################################


# Monday
if day == 'Monday':

  # Computer Networks
  if time >= '08:25:00' and time <= '09:50:00':
    print('Computer Networks')
    webbrowser.open('https://iitbhilai.webex.com/meet/b203', new=2)

  # check for fractal 5-6
  if dateToday >= '2020-10-01' and dateToday <= '2020-11-20':

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

  # check for fractal 1-2
  if dateToday >= '2020-07-28' and dateToday <= '2020-08-28':

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

  # check for fractal 1-2
  if dateToday >= '2020-07-28' and dateToday <= '2020-08-28':

    # Materials Chemistry 3 Tutorial
    if time >= '09:55:00' and time <= '11:20:00':
      print('Materials Chemistry 3 Tutorial')
      webbrowser.open('https://iitbhilai.webex.com/meet/b204', new=2)

  # Computer Networks
  if time >= '11:25:00' and time <= '12:50:00':
    print('Computer Networks')
    webbrowser.open('https://iitbhilai.webex.com/meet/b203', new=2)
  
  # check for fractal 5-6
  if dateToday >= '2020-10-01' and dateToday <= '2020-11-20':

    # Concepts of Personality Psychology
    if time >= '15:55:00' and time <= '17:20:00':
      print('Concepts of Personality Psychology')
      webbrowser.open('https://iitbhilai.webex.com/meet/b204', new=2)


# Thursday
if day == 'Thursday':
  
  # check for fractal 5-6
  if dateToday >= '2020-10-01' and dateToday <= '2020-11-20':

    # Contemporary Indian Cinema: Beyond Bollywood
    if time >= '09:55:00' and time <= '11:20:00':
      print('Contemporary Indian Cinema: Beyond Bollywood')
      webbrowser.open('https://iitbhilai.webex.com/meet/b202', new=2)

  # check for fractal 1-2
  if dateToday >= '2020-07-28' and dateToday <= '2020-08-28':

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

  # check for fractal 5-6
  if dateToday >= '2020-10-01' and dateToday <= '2020-11-20':

    # Concepts of Personality Psychology
    if time >= '15:55:00' and time <= '17:20:00':
      print('Concepts of Personality Psychology')
      webbrowser.open('https://iitbhilai.webex.com/meet/b204', new=2)


####################################################################################################################################