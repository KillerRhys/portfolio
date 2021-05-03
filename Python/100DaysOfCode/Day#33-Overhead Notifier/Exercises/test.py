import requests

# API Tut
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# data = response.json()
#
# longitude = data['iss_position']['longitude']
# latitude =  data['iss_position']['latitude']
# pos = (longitude, latitude)
# print(pos)


# # Kanye Quote Machine XD
# from tkinter import *
# quote = ""
#
#
# def get_quote():
#     global quote
#     dumbass = requests.get(url="https://api.kanye.rest")
#     dumbass.raise_for_status()
#     dummy = dumbass.json()
#     quote = dummy['quote']
#     canvas.itemconfig(quote_text, text=quote)
#     window.update()
#
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text=f"{quote}", width=250, font=("Arial", 20, "bold"), fill="white", tags='shit')
# canvas.grid(row=0, column=0)
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
#
# window.mainloop()

# Sunrise/Set API
parameters = {
    'lat': 39.554920,
    'lng': -84.304610,
    'formatted': 0,
}
sol = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
sol.raise_for_status()
data = sol.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise, sunset)