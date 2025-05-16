import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Initialize variables
        self.current_input = ""
        self.result = 0
        self.operation = None
        
        # Create display
        self.display_var = tk.StringVar()
        self.display = tk.Entry(root, textvariable=self.display_var, font=('Arial', 20), 
                               bd=10, insertwidth=2, width=14, borderwidth=4, 
                               justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Create buttons
        self.create_buttons()
        
    def create_buttons(self):
        # Button layout
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        # Create and position buttons
        for i, text in enumerate(button_texts):
            row = i // 4 + 1
            col = i % 4
            if text == '=':
                btn = tk.Button(self.root, text=text, padx=20, pady=20,
                              command=self.calculate_result, bg='light blue')
            elif text == 'C':
                btn = tk.Button(self.root, text=text, padx=20, pady=20,
                              command=self.clear_display, bg='light coral')
            else:
                btn = tk.Button(self.root, text=text, padx=20, pady=20,
                              command=lambda t=text: self.button_click(t))
            btn.grid(row=row, column=col, sticky='nsew')
            
        # Configure row/column weights
        for i in range(1, 5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value):
        if value in '+-*/':
            if self.current_input:
                self.operation = value
                self.result = float(self.current_input)
                self.current_input = ""
                self.display_var.set(self.result)
        else:
            self.current_input += str(value)
            self.display_var.set(self.current_input)
    
    def calculate_result(self):
        if self.operation and self.current_input:
            try:
                num2 = float(self.current_input)
                if self.operation == '+':
                    self.result += num2
                elif self.operation == '-':
                    self.result -= num2
                elif self.operation == '*':
                    self.result *= num2
                elif self.operation == '/':
                    if num2 == 0:
                        messagebox.showerror("Error", "Cannot divide by zero!")
                        self.clear_display()
                        return
                    self.result /= num2
                
                self.display_var.set(self.result)
                self.current_input = str(self.result)
                self.operation = None
            except ValueError:
                messagebox.showerror("Error", "Invalid input!")
                self.clear_display()
    
    def clear_display(self):
        self.current_input = ""
        self.result = 0
        self.operation = None
        self.display_var.set("")
    
    def run(self):
        self.root.mainloop()

# Main function to run the app
def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    app.run()

if __name__ == "__main__":
    main()