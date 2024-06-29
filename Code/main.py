from scrubber import scrape, printListData
from tkinter import *


#zipCode = input("Enter a zip code: ")
#printListData(scrape(zipCode))

'''
def get_data():
    zipCode = zip_entry.get()
    printListData(scrape(zipCode))

root = Tk()

Label(root, text="Enter a zip code:").pack()
zip_entry = Entry(root)
zip_entry.pack()

Button(root, text="Submit", command=get_data).pack()

root.mainloop()
'''
'''
def get_data():
    zipCode = zip_entry.get()
    output_text.delete(1.0, END)  # Clear the text field before inserting new text
    output_text.insert(END, printListData(scrape(zipCode)))

root = Tk()
root.title("Weather Scraper")
root.config(bg="black", cursor="cross", highlightbackground="white", highlightcolor="blue", highlightthickness=2, padx=10, pady=10)

Label(root, text="Enter a zip code:", bg="black", fg="#90ee90").pack()
zip_entry = Entry(root, justify="center")
zip_entry.pack()

Button(root, text="Submit", command=get_data, bg="lightblue", fg="black").pack()

output_text = Text(root, bg="black", fg="#90ee90")  # Create a Text widget with xxx background and xxx text
output_text.pack()

root.mainloop()
'''
'''
def get_data():
    zipCode = zip_entry.get()
    output_text.delete(1.0, END)  # Clear the text field before inserting new text
    output_text.insert(END, printListData(scrape(zipCode)))
'''
def insert_slowly(text_widget, text, delay=12):
    if text:
        text_widget.insert(END, text[0])
        root.after(delay, insert_slowly, text_widget, text[1:], delay)

def get_data():
    zipCode = zip_entry.get()
    output_text.delete(1.0, END)  # Clear the text field before inserting new text
    insert_slowly(output_text, printListData(scrape(zipCode)))

root = Tk()
root.title("Weather Scraper")
root.config(bg="black")





# row 1
Label(root, text="Enter a zip code:", bg="black", fg="#90ee90", justify="center", font=("Fixedsys", 35), borderwidth=7, relief="groove").grid(row=0, column=0, sticky="ew")

# row 2
zip_entry = Entry(root, justify="center", bg="#696969", fg="white", font=("Fixedsys", 20), borderwidth=8, relief="sunken")
zip_entry.grid(row=2,rowspan=3, column=0, sticky="ew")


# row 5

Button(root, text="Submit", command=get_data, bg="#222222", fg="#90ee90", justify="center", font=("Fixedsys", 20)).grid(row=5, column=0, sticky="ew")


# row 6
output_text = Text(root, bg="black", fg="#90ee90", font=("Fixedsys", 20))  # Create a Text widget with black background and light green text
output_text.grid(row=6, column=0, sticky="nsew", columnspan=3, padx=10)  # The "nsew" option makes the Text widget resizable

root.grid_rowconfigure(6, weight=1)  # Makes the row with the Text widget resizable
root.grid_columnconfigure(0, weight=1)  # Makes the column with the Text widget resizable

root.mainloop()