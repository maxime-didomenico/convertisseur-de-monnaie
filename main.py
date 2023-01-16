from tkinter import *
from tkinter import ttk
import requests
import csv

mainapp = Tk()
currency = ["eur","usd","jpy"] 

def extract_result(str):
    i = 0
    long = len(str)
    while i < long:
        if str[i] == 'u' and str[i + 1] == 'l' and str[i + 2] == 't':
            value = [str[i + 6],str[i + 7],str[i + 8],str[i + 9],str[i + 10],str[i + 11]]
            real_value = "".join(value)
            real_value = float(real_value)
            i = long
        else:
            i+=1
    return(real_value)

def convert():
    amount = EntryAmount.get()
    first_currency = FirstCurrency.get()
    second_currency = SecondCurrency.get()

    url_one = "https://api.apilayer.com/fixer/convert?to="
    url_sec = "&from="
    url_third = "&amount="

    string = [url_one,first_currency,url_sec,second_currency,url_third,amount]
    url = "".join(string)

    payload = {}
    headers= {"apikey": "bmab1LCggAyWjyhNmGRIpURZLjAnPJVS"}

    response = requests.request("GET", url, headers=headers, data = payload)

    #status_code = response.status_code
    result = response.text
    last_result = extract_result(result)
    print(last_result)
    LabelResult.configure(text=last_result)
    
    with open('history.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_currency', 'second_currency', 'amount', 'change']

        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        thewriter.writeheader()
        thewriter.writerow({'first_currency' : first_currency, 'second_currency' : second_currency, 'amount' : amount, 'change' : last_result})



mainapp.title("Currency Conversion")
mainapp.geometry("800x600")
mainapp.resizable(width=False, height=False)

frame = LabelFrame(mainapp,text='Currency Converter',bg='#f0f0f0',font=(20))
frame.pack(expand=True, fill=BOTH)


LabelAmount = Label(frame, text="Amount to convert : ",bg="#f0f0f0")
LabelAmount.pack()

EntryAmount = Entry(frame, bd =5)
EntryAmount.pack()


LabelSecondCurrency = Label(frame, text="First Currency : ",bg="#f0f0f0")
LabelSecondCurrency.pack()

SecondCurrency = ttk.Combobox(frame, values=currency)
SecondCurrency.pack()


LabelFirstCurrency = Label(frame, text="Second Currency : ",bg="#f0f0f0")
LabelFirstCurrency.pack()

FirstCurrency = ttk.Combobox(frame, values=currency)
FirstCurrency.pack()

Button = Button(frame, text="Convert", command=convert)
Button.pack()

LabelResult = Label(frame, text="",bg="#f0f0f0")
LabelResult.pack()


mainapp.mainloop()