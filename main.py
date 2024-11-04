import tkinter as tk


def fahrenheit_to_celsius_kelvin():
    """
    Convert the value for Fahrenheit to Celsius and Kelvin and insert the
    result into lbl_result and lbl_result2 respectively.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    kelvin = celsius + 273.15
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    lbl_result2["text"] = f"{round(kelvin, 2)} K"


def celsius_to_fahrenheit_kelvin():
    """
    Convert the value for Celsius to Fahrenheit and Kelvin and insert the
    result into lbl_result3 and lbl_result4 respectively.
    """
    celsius = ent_temperature2.get()
    fahrenheit = (float(celsius) * (9 / 5)) + 32
    kelvin = float(celsius) + 273.15
    lbl_result3["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"
    lbl_result4["text"] = f"{round(kelvin, 2)} K"


def kelvin_to_celsius_fahrenheit():
    """
    Convert the value for Kelvin to Celsius and Fahrenheit and insert the
    result into lbl_result5 and lbl_result6 respectively.
    """
    kelvin = ent_temperature3.get()
    celsius = float(kelvin) - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    lbl_result5["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    lbl_result6["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"


# Set up the window
window = tk.Tk()
window.title("Temperature Converter")
window.minsize(width=400, height=100)


# fahrenheit --> celsius, kelvin

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")


# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius_kelvin
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
lbl_result2 = tk.Label(master=window, text="K")

# Set up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)
lbl_result2.grid(row=0, column=3, padx=10)


# celsius --> fahrenheit, kelvin

# Create the Celsius entry frame with an Entry
# widget and label in it
frm_entry2 = tk.Frame(master=window)
ent_temperature2 = tk.Entry(master=frm_entry2, width=10)
lbl_temp2 = tk.Label(master=frm_entry2, text="\N{DEGREE CELSIUS}")

# Layout the temperature Entry and Label in frm_entry2
# using the .grid() geometry manager
ent_temperature2.grid(row=1, column=0, sticky="e")
lbl_temp2.grid(row=1, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert2 = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=celsius_to_fahrenheit_kelvin
)
lbl_result3 = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")
lbl_result4 = tk.Label(master=window, text="K")

# Set up the layout using the .grid() geometry manager
frm_entry2.grid(row=1, column=0, padx=10)
btn_convert2.grid(row=1, column=1, pady=10)
lbl_result3.grid(row=1, column=2, padx=10)
lbl_result4.grid(row=1, column=3, padx=10)


# kelvin --> celsius, fahrenheit

# Create the Kelvin entry frame with an Entry
# widget and label in it
frm_entry3 = tk.Frame(master=window)
ent_temperature3 = tk.Entry(master=frm_entry3, width=10)
lbl_temp3 = tk.Label(master=frm_entry3, text=" K")

# Layout the temperature Entry and Label in frm_entry2
# using the .grid() geometry manager
ent_temperature3.grid(row=2, column=0, sticky="e")
lbl_temp3.grid(row=2, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert3 = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=kelvin_to_celsius_fahrenheit
)
lbl_result5 = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
lbl_result6 = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")

# Set up the layout using the .grid() geometry manager
frm_entry3.grid(row=2, column=0, padx=10)
btn_convert3.grid(row=2, column=1, pady=10)
lbl_result5.grid(row=2, column=2, padx=10)
lbl_result6.grid(row=2, column=3, padx=10)


# Run the application
window.mainloop()
