import pandas as pd #to form the dataframe
import folium #for rendering the map
import tkinter as tk #for GUI

win = tk.Tk()
win.title("Covid Hotspot Detector")
win.geometry("512x550")
win.iconbitmap(r'C:\Users\deepa\Downloads\Icons8-Windows-8-Healthcare-Clinic.ico')
def maha(): #Maharashtra
    cm_df = pd.DataFrame({'city': ['Mumbai', 'Pune', 'Aurangabad', 'Sangli', 'Nagpur','Nashik','Thane','Buldhana','Ahmednagar','Yavatmal'],#hotspot cities
                          'latitude': [19.075983, 18.520430, 19.876165, 16.852398, 21.145800,19.997453,19.197817,20.523737,19.085455,20.389623],#latitudes
                          'longitude': [72.877655, 73.856743, 75.343315, 74.581474, 79.088158,73.789802,72.967810,76.188482,74.735486,78.127160]  #longitudes
                          })
    print(cm_df)
    map_cm_multiple = folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],popup=i.city).add_to(map_cm_multiple) #for on map markers

def delhi(): #Delhi
    cm_df = pd.DataFrame({'city': [' Shahdara', 'New Delhi'],
                          'latitude': [28.671679, 28.626963],
                          'longitude': [77.294197, 77.215396]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)
def UP(): #UttarPradesh
    cm_df = pd.DataFrame({'city': ['Noida', 'Meerut','Gautam Budhh Nagar','Agra','Lucknow','Firozabad','Shamli','Moradabad','Saharanpur','Ghaziabad'],
                          'latitude': [28.5726442, 28.916667,27.42397,27.1752554,26.8381,27.1773663,29.5008816,28.8638424,29.9880774,28.711241],
                          'longitude': [77.3547609, 77.683333,77.09922,78.0098161,78.389912,77.3483826,78.8057783,77.5081299,77.4445372,77.4445372]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)
def Kerala(): #Kerala
    cm_df = pd.DataFrame({'city': ['Kasaragod', 'Kannur','Mallapuram','Ernakulam','Pathanamthitta','Thiruvananthapuram'],
                          'latitude': [12.421713,11.8762254,14.6094453,10.0383947,9.2834044,8.5058909],
                          'longitude': [75.1904498,75.3738043,79.3024381,76.5074145,76.9606628,76.9570481]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)

def Tamil(): #Tamil Nadu
    cm_df = pd.DataFrame({'city': ['Chennai', 'Coimbature','Dindigul','Erode','Vellore','Tuticorin','Madurai','Tiruchirapalli','Thiruvarur','Kanyakumari'],
                          'latitude': [13.0801721,10.9961974,10.3303299,11.3692044,12.7948109,8.7235577,9.9223354,10.7620859,10.7361861,8.079252],
                          'longitude': [80.2838331,77.0055029,78.0673979,77.67662691,79.0006411,78.025154,78.1493658,78.712771,79.6331866,77.5499338]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)

def Telang(): #Telangana
    cm_df = pd.DataFrame({'city': ['Hyderabad','Warangal','Nizamabad','Jogulamba Gadwal','Karimnagar','Nirmal'],
                          'latitude': [17.3887859,17.9806094,26.0553179,16.0999202,18.4346438,19.0915209],
                          'longitude': [78.4610647,79.5982115,82.9931387,77.7341584,79.1322648,78.396609]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)

def raj(): #Rajasthan
    cm_df = pd.DataFrame({'city': ['Bhilwara','Jaipur','Jodhpur','Jaisalmer','Kota','Bikaner'],
                          'latitude': [25.48877352,26.916194,26.2967719,27.0280161,25.1968256,28.0159286],
                          'longitude': [74.6996128,75.820349,73.0351433,70.7785056,76.0008933,73.3171367]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)
def guj(): #Gujarat
    cm_df = pd.DataFrame({'city': ['Ahmedabad','Surat','Vadodara','Rajkot','Bhavnagar'],
                          'latitude': [23.0216238,21.1864607,22.2973142,22.3051991,21.7718836],
                          'longitude': [72.5797068,72.8081281,73.1942567,70.8028335,72.1416449]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)
def mp(): #Madhya Pradesh
    cm_df = pd.DataFrame({'city': ['Bhopal','Indore','Ujjain','Khargone','Hoshangabad'],
                          'latitude': [23.2530923,22.7203616,23.174597,21.8187743,22.6001502],
                          'longitude': [77.3962718,75.8681996,75.7851423,75.6064577,77.9266452]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)
def kar(): #Karnatka
    cm_df = pd.DataFrame({'city': ['Bengaluru','Mysore','Belagavi'],
                          'latitude': [12.9791198,12.3051828,15.8572666],
                          'longitude': [77.5912997,76.6553609,74.5069343]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)
def ap(): #Andhrapradesh
    cm_df = pd.DataFrame({'city': ['Kurnool','Nellore','Vishakhapatnam','Chittoor','Anantapur'],
                          'latitude': [15.8309251,14.4493717,17.68009,13.1601048,14.6546235],
                          'longitude': [78.0425373,79.9873763,83.20161,79.1555506,77.5562598]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)
def wb(): #West Bengal
    cm_df = pd.DataFrame({'city': ['Kolkata','Howrah','Medinipur East'],
                          'latitude': [22.5677459,22.5882216,22.4207025],
                          'longitude': [88.3476023,88.323139,87.3269963]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)
def bihar(): #Bihar
    cm_df = pd.DataFrame({'city': ['Siwan'],
                          'latitude': [26.1310043],
                          'longitude': [84.3912566]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)
def Chandigarh(): #Chandigarh
    cm_df = pd.DataFrame({'city': ['Chandigarh'],
                          'latitude': [30.7194022],
                          'longitude': [76.7646552]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)
def Chhattisgarh (): #Chhattisgarh
    cm_df = pd.DataFrame({'city': ['Korba'],
                          'latitude': [22.5197695],
                          'longitude': [82.6295146]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)
def hr(): #Haryana
    cm_df = pd.DataFrame({'city': ['Gurugram','Palwal','Faridabad'],
                          'latitude': [28.4646148,28.1250257,28.402837],
                          'longitude': [77.0299194,77.358313,77.3085626]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)

def jk(): #Jammu Kashmir
    cm_df = pd.DataFrame({'city': ['Jammu','Udhampur','Srinagar','Bandipora','Baramulla'],
                          'latitude': [32.7185614,33,34.0747444,34.4563234,34.2050056],
                          'longitude': [74.8580917,75.166667,74.8204443,75.1834458,74.3622108]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)

def  od(): #Odisha
    cm_df = pd.DataFrame({'city': ['Khordha'],
                          'latitude': [20.2256472],
                          'longitude': [85.5605947]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)
def pb(): #Punjab
    cm_df = pd.DataFrame({'city': ['Jalandhar','Pathankot','Shaheed Bhagat Singh Nagar'],
                          'latitude': [31.2920107,32.3017104,31.1268889],
                          'longitude': [75.5680577,75.6586425,76.1576848]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)


def  uk(): #Uttarakhand
    cm_df = pd.DataFrame({'city': ['Dehradun'],
                          'latitude': [30.3255646],
                          'longitude': [78.0436813]
                          })
    print(cm_df)
    map_cm_multiple1= folium.Map(location=[18, 80], zoom_start=4)
    for i in cm_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                  popup=i.city).add_to( map_cm_multiple1)



button = tk.Button(win,text = "Maharashtra",command = maha,bg = 'black',fg = 'green') #buttons for respective states
button.pack()
button1 = tk.Button(win,text = "Delhi",command = delhi,bg = 'black',fg = 'green')
button1.pack()
button2 = tk.Button(win,text = "Uttar Pradesh",command = UP,bg = 'black',fg = 'green')
button2.pack()
button3 = tk.Button(win,text = "Kerala",command = Kerala,bg = 'black',fg = 'green')
button3.pack()
button4 = tk.Button(win,text = "Tamil Nadu",command = Tamil,bg = 'black',fg = 'green')
button4.pack()
button5 = tk.Button(win,text = "Telangana",command = Telang,bg = 'black',fg = 'green')
button5.pack()
button6 = tk.Button(win,text = "Rajasthan",command = raj,bg = 'black',fg = 'green')
button6.pack()
button7 = tk.Button(win,text = "Gujarat",command = guj,bg = 'black',fg = 'green')
button7.pack()
button8 = tk.Button(win,text = "Madhya Pradesh",command = mp,bg = 'black',fg = 'green')
button8.pack()
button9 = tk.Button(win,text = "Karnatka",command = kar,bg = 'black',fg = 'green')
button9.pack()
button10= tk.Button(win,text = "Andhra Pradesh",command = ap,bg = 'black',fg = 'green')
button10.pack()
button11= tk.Button(win,text = "West Bengal",command = wb,bg = 'black',fg = 'green')
button11.pack()
button12= tk.Button(win,text = "Bihar",command = bihar,bg = 'black',fg = 'green')
button12.pack()
button13= tk.Button(win,text = "Chandigarh",command =Chandigarh,bg = 'black',fg = 'green')
button13.pack()
button14= tk.Button(win,text = "Chhattisgarh",command =Chhattisgarh,bg = 'black',fg = 'green')
button14.pack()
button15= tk.Button(win,text = "Haryana",command =hr,bg = 'black',fg = 'green')
button15.pack()
button16= tk.Button(win,text = "Jammu and Kashmir",command =jk,bg = 'black',fg = 'green')
button16.pack()
button17= tk.Button(win,text = "Odisha",command =od,bg = 'black',fg = 'green')
button17.pack()
button18= tk.Button(win,text = "Punjab",command =pb,bg = 'black',fg = 'green')
button18.pack()
button19= tk.Button(win,text = "Uttarakhand",command =uk,bg = 'black',fg = 'green')
button19.pack()
button20 = tk.Button(text = "Click and Quit", command = win.destroy,bg = 'red',fg = 'black') #button to close the window
button20.pack()
win.mainloop()