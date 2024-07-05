import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.total_income = 0
        self.total_expense = 0
        self.income_cats = {}
        self.expense_cats = {}
        self.financial_data = []
        self.chart = None
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.income_label = Label(self, text="Income:")
        self.income_label.pack()
        self.income = Entry(self)
        self.income.pack()
        self.income_cat_label = Label(self, text="Income Category:")
        self.income_cat_label.pack()
        self.income_cat = Entry(self)
        self.income_cat.pack()
        self.expense_label = Label(self, text="Expense:")
        self.expense_label.pack()
        self.expense = Entry(self)
        self.expense.pack()
        self.expense_cat_label = Label(self, text="Expense Category:")
        self.expense_cat_label.pack()
        self.expense_cat = Entry(self)
        self.expense_cat.pack()
        self.total_income_label = Label(self, text="Total Income: " + str(self.total_income))
        self.total_income_label.pack()
        self.total_expense_label = Label(self, text="Total Expense: " + str(self.total_expense))
        self.total_expense_label.pack()
        self.submit_button = Button(self, text="SUBMIT", fg="blue", command=self.add_financial_data)
        self.submit_button.pack()
        self.plot_line_button = Button(self, text="Plot Line Chart", fg="green", command=self.plot_line_chart)
        self.plot_line_button.pack()
        self.plot_pie_income_button = Button(self, text="Plot Income Pie Chart", fg="green",
                                             command=self.plot_pie_income_chart)
        self.plot_pie_income_button.pack()
        self.plot_pie_expense_button = Button(self, text="Plot Expense Pie Chart", fg="green",
                                              command=self.plot_pie_expense_chart)
        self.plot_pie_expense_button.pack()
        self.quit_button = Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit_button.pack()

    def add_financial_data(self):
        try:
            income = int(self.income.get())
            if not isinstance(income, int):
                raise ValueError

            expense = int(self.expense.get())
            if not isinstance(expense, int):
                raise ValueError

            income_cat = self.income_cat.get()
            if not isinstance(income_cat, str):
                raise ValueError

            expense_cat = self.expense_cat.get()
            if not isinstance(expense_cat, str):
                raise ValueError

            self.total_income += income
            self.total_expense += expense
            self.income_cats[income_cat] = self.income_cats.get(income_cat, 0) + income
            self.expense_cats[expense_cat] = self.expense_cats.get(expense_cat, 0) + expense
            self.financial_data.append((self.total_income, self.total_expense))
            self.total_income_label.config(text="Total Income: " + str(self.total_income))
            self.total_expense_label.config(text="Total Expense: " + str(self.total_expense))
            self.income.delete(0, END)
            self.expense.delete(0, END)
            self.income_cat.delete(0, END)
            self.expense_cat.delete(0, END)
        except ValueError:
            print("Please enter proper type of values: int for income and expense, str for income and expense category")

    def plot_line_chart(self):
        self.clear_chart()
        fig = plt.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot([income for income, expense in self.financial_data], label='Income')
        ax.plot([expense for income, expense in self.financial_data], label='Expense')
        ax.legend()
        ax.set_title("Income and Expense Chart")
        ax.set_xlabel('Time')
        ax.set_ylabel('Amount')
        self.chart = FigureCanvasTkAgg(fig, self)
        self.chart.get_tk_widget().pack()

    def plot_pie_income_chart(self):
        self.plot_pie_chart(self.income_cats, "Income Categories")

    def plot_pie_expense_chart(self):
        self.plot_pie_chart(self.expense_cats, "Expense Categories")

    def plot_pie_chart(self, data, title):
        self.clear_chart()
        fig = plt.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.pie(list(data.values()), labels=list(data.keys()), autopct='%1.1f%%')
        ax.set_title(title)
        self.chart = FigureCanvasTkAgg(fig, self)
        self.chart.get_tk_widget().pack()

    def clear_chart(self):
        if self.chart:
            widget = self.chart.get_tk_widget()
            widget.pack_forget()
            widget.destroy()


if __name__ == "__main__":
    root = Tk()
    root.geometry("500x600")
    app = Application(master=root)
    app.mainloop()