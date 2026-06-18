from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title("3")
root.geometry("700x140")

def agify_lookup(name="john"):
    try:
        response = requests.get(
            "https://api.agify.io",
            params={"name": name},
            timeout=5
        )

        response.raise_for_status()
        data = response.json()

        print("Agify API Response:")
        print(f"Name: {data['name']}")
        print(f"Predicted Age: {data['age']}")
        print(f"Count: {data['count']}")

        return data

    except Exception as e:
        print(f"Agify API Error: {e}")
        return None


def ziplookup():
#    zip.get()
#    ziplabel = Label(root,text = zip.get())
#    ziplabel.grid(row = 1,column=0,columnspan=2)
#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=54ACDFB9-A3AB-4835-A4D2-5DFB9EE6E65B
#https://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=83814&distance=25&API_KEY=54ACDFB9-A3AB-4835-A4D2-5DFB9EE6E65B

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=54ACDFB9-A3AB-4835-A4D2-5DFB9EE6E65B")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good" :
            color = "#0C0"
        
        elif category == "Moderate":
            color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            color = "#FF9900"
        elif category == "Unhealthy":
            color = "#FF0000"
        elif category == "Very Unhealthy":
            color = "#990066"
        elif category == "Hazardous":
            color = "#660000"


        mylabel=Label(root,text=city + " Air Quality " + str(quality) + " " + category,font = ("Helvetica", 20),bg=color)
        mylabel.grid(row=2,column=0,columnspan=2)
        root.configure(background=color)
    except Exception as e:
        api = "Error"

zip = Entry(root)
zip.grid(row=0,column=0)

zipButton = Button (root,text="look up code",command = ziplookup)
zipButton.grid(row=0,column=1)

agify_data = agify_lookup()

root.mainloop()
