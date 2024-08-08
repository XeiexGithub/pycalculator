# Display a microsoft calculator type layout
# Use libaries such as tkinter to make a gui
# Simple math operations should be possible

import customtkinter as ctk

calculation_string = ""

ctk.set_appearance_mode("System")

calculator = ctk.CTk()

calculator.title("Dhyan's calculator")
calculator.geometry("300x290")

def clear_screen():
    textbox.delete(1.0, "end")
    calculation_string = ""

def add_to_calculator(number):
    global calculation_string
    if number == "=":
        textbox.delete(1.0, "end")
        eval_calculation()
    else:
        calculation_string += str(number)
        textbox.insert(ctk.INSERT,number)

def eval_calculation():
    try:
        result = str(eval(calculation_string))
        textbox.insert(ctk.INSERT,result)
        calculation_string = ""
    except:
        textbox.insert(ctk.INSERT,"ERROR")

textbox = ctk.CTkTextbox(calculator, width = 300, height = 75)
textbox.grid(row=0, columnspan=5, padx=0, pady=1)

bn_7 = ctk.CTkButton(calculator, text="7", command=lambda: add_to_calculator(7), width = 65, height = 40)
bn_7.grid(row=1, column=1, padx=0, pady=1)
bn_8 = ctk.CTkButton(calculator, text="8", command=lambda: add_to_calculator(8), width = 65, height = 40)
bn_8.grid(row=1, column=2, padx=0, pady=1)
bn_9 = ctk.CTkButton(calculator, text="9", command=lambda: add_to_calculator(9), width = 65, height = 40)
bn_9.grid(row=1, column=3, padx=0, pady=1)
bn_4 = ctk.CTkButton(calculator, text="4", command=lambda: add_to_calculator(4), width = 65, height = 40)
bn_4.grid(row=2, column=1, padx=0, pady=1)
bn_5 = ctk.CTkButton(calculator, text="5", command=lambda: add_to_calculator(5), width = 65, height = 40)
bn_5.grid(row=2, column=2, padx=0, pady=1)
bn_6 = ctk.CTkButton(calculator, text="6", command=lambda: add_to_calculator(6), width = 65, height = 40)
bn_6.grid(row=2, column=3, padx=0, pady=1)
bn_1 = ctk.CTkButton(calculator, text="1", command=lambda: add_to_calculator(1), width = 65, height = 40)
bn_1.grid(row=3, column=1, padx=0, pady=1)
bn_2 = ctk.CTkButton(calculator, text="2", command=lambda: add_to_calculator(2), width = 65, height = 40)
bn_2.grid(row=3, column=2, padx=0, pady=1)
bn_3 = ctk.CTkButton(calculator, text="3", command=lambda: add_to_calculator(3), width = 65, height = 40)
bn_3.grid(row=3, column=3, padx=0, pady=1)
bn_0 = ctk.CTkButton(calculator, text="0", command=lambda: add_to_calculator(0), width = 65, height = 40)
bn_0.grid(row=4, column=2, padx=0, pady=1)
bn_plus = ctk.CTkButton(calculator, text="+", command=lambda: add_to_calculator("+"), width = 65, height = 40)
bn_plus.grid(row=1, column=4, padx=0, pady=1)
bn_minus = ctk.CTkButton(calculator, text="-", command=lambda: add_to_calculator("-"), width = 65, height = 40)
bn_minus.grid(row=2, column=4, padx=0, pady=1)
bn_multiply = ctk.CTkButton(calculator, text="*", command=lambda: add_to_calculator("*"), width = 65, height = 40)
bn_multiply.grid(row=3, column=4, padx=0, pady=1)
bn_divide = ctk.CTkButton(calculator, text="/", command=lambda: add_to_calculator("/"), width = 65, height = 40)
bn_divide.grid(row=4, column=4, padx=0, pady=1)
bn_para1 = ctk.CTkButton(calculator, text="(", command=lambda: add_to_calculator("("), width = 65, height = 40)
bn_para1.grid(row=4, column=1, padx=0, pady=1)
bn_para2 = ctk.CTkButton(calculator, text=")", command=lambda: add_to_calculator(")"), width = 65, height = 40)
bn_para2.grid(row=4, column=3, padx=0, pady=1)
bn_equals = ctk.CTkButton(calculator, text="=", command=lambda: add_to_calculator("="), width = 65, height = 40)
bn_equals.grid(row=5, column=1, padx=0, pady=1)
bn_clear = ctk.CTkButton(calculator, text="CE", command=lambda: clear_screen(), width = 65, height = 40)
bn_clear.grid(row=5, column=3, padx=0, pady=1)

calculator.mainloop()