import tkinter as tk
from Classifier import ClassifierA
from tkinter import messagebox


class Start:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x800')
        self.root.resizable(False, False)
        self.root.title('find out the degree of severity')
        self.v = tk.StringVar()
        self.v1 = tk.StringVar()
        self.v2 = tk.StringVar()
        self.v3 = tk.StringVar()
        self.v4 = tk.StringVar()
        self.v5 = tk.StringVar()
        self.res = []
        tk.Label(self.root,
                 text="Do you have fever?",
                 font=10,
                 relief=tk.RIDGE).pack()
        self.r1 = tk.Radiobutton(self.root,
                                 text="no",
                                 variable=self.v,
                                 value="0",
                                 command=lambda: self.v.set("0"),
                                 tristatevalue="x"
                                 )
        self.r1.pack()
        self.r2 = tk.Radiobutton(self.root,
                                 text="between 37 and 38",
                                 variable=self.v,
                                 value="1",
                                 command=lambda: self.v.set("1"),
                                 tristatevalue="x"
                                 )
        self.r2.pack()
        self.r3 = tk.Radiobutton(self.root,
                                 text="more than 38",
                                 variable=self.v,
                                 value="2",
                                 command=lambda: self.v.set("2"),
                                 tristatevalue="x"
                                 )
        self.r3.pack()

        tk.Label(self.root,
                 text="Do you have joint pain?",
                 font=10,
                 relief=tk.RIDGE
                 ).pack()
        tk.Radiobutton(self.root,
                       text="you don’t have",
                       variable=self.v1,
                       value="0",
                       command=lambda: self.v1.set("0"),
                       tristatevalue="x"
                       ).pack()
        tk.Radiobutton(self.root,
                       text="you have",
                       variable=self.v1,
                       value="1",
                       command=lambda: self.v1.set("1"),
                       tristatevalue="x"
                       ).pack()
        tk.Radiobutton(self.root,
                       text="you have a compound fracture",
                       variable=self.v1,
                       value="2",
                       command=lambda: self.v1.set("2"),
                       tristatevalue="x"
                       ).pack()
        tk.Radiobutton(self.root,
                       text="you have a decomposed fracture",
                       variable=self.v1,
                       value="3",
                       command=lambda: self.v1.set("3"),
                       tristatevalue="x"
                       ).pack()

        tk.Label(self.root,
                 text="Do you (or the patient) have an altered state of consciousness?",
                 font=10,
                 relief=tk.RIDGE
                 ).pack()
        tk.Radiobutton(self.root,
                       text="you don’t have",
                       variable=self.v2,
                       value="0",
                       command=lambda: self.v2.set("0"),
                       tristatevalue="x"
                       ).pack()
        tk.Radiobutton(self.root,
                       text="you are in shock",
                       variable=self.v2,
                       value="1",
                       command=lambda: self.v2.set("1"),
                       tristatevalue="x"
                       ).pack()
        tk.Radiobutton(self.root,
                       text="you have an altered state of consciousness",
                       variable=self.v2,
                       value="2",
                       command=lambda: self.v2.set("2"),
                       tristatevalue="x"
                       ).pack()
        tk.Radiobutton(self.root,
                       text="your patient have lost consciousness",
                       variable=self.v2,
                       value="3",
                       command=lambda: self.v2.set("3"),
                       tristatevalue="x"
                       ).pack()
        tk.Label(self.root,
                 text="Do you have intestinal problems?",
                 font=10,
                 relief=tk.RIDGE
                 ).pack()

        tk.Radiobutton(self.root,
                       text="you don’t have",
                       variable=self.v3,
                       value="0",
                       command=lambda: self.v3.set("0"),
                       tristatevalue="x"
                       ).pack()
        tk.Radiobutton(self.root,
                       text="you have diarrhea or abdominal pain",
                       variable=self.v3,
                       value="1",
                       command=lambda: self.v3.set("1"),
                       tristatevalue="x"
                       ).pack()
        tk.Radiobutton(self.root,
                       text="you have strong intestinal cramps",
                       variable=self.v3,
                       value="2",
                       command=lambda: self.v3.set("2"),
                       tristatevalue="x"
                       ).pack()
        tk.Label(self.root,
                 text="Do you have a blood loss?",
                 font=10,
                 relief=tk.RIDGE
                 ).pack()

        tk.Radiobutton(self.root,
                       text="you don’t have",
                       variable=self.v4,
                       value="0",
                       command=lambda: self.v4.set("0"),
                       tristatevalue="x"
                       ).pack()
        tk.Radiobutton(self.root,
                       text="you have a small blood loss",
                       variable=self.v4,
                       value="1",
                       command=lambda: self.v4.set("1"),
                       tristatevalue="x"
                       ).pack()
        tk.Radiobutton(self.root,
                       text="you have an internal haemorrhaging or severe externa",
                       variable=self.v4,
                       value="2",
                       command=lambda: self.v4.set("2"),
                       tristatevalue="x"
                       ).pack()
        tk.Label(self.root,
                 text="Do you have breathing problems? ",
                 font=10,
                 relief=tk.RIDGE
                 ).pack()
        tk.Radiobutton(self.root,
                       text="you don’t have",
                       variable=self.v5,
                       value="0",
                       command=lambda: self.v5.set("0"),
                       tristatevalue="x"
                       ).pack()
        tk.Radiobutton(self.root,
                       text="you have a chronic respiratory insufficiency",
                       variable=self.v5,
                       value="1",
                       command=lambda: self.v5.set("1"),
                       tristatevalue="x"
                       ).pack()
        tk.Radiobutton(self.root,
                       text="you went into acute respiratory distress",
                       variable=self.v5,
                       value="2",
                       command=lambda: self.v5.set("2"),
                       tristatevalue="x"
                       ).pack()

        tk.Button(self.root,
                  text="calculate",
                  command=lambda: self.askuser()).pack()
        tk.Button(self.root,
                  text="test",
                  command=lambda: self.testClassifier()).pack()
        self.consoleArea = tk.Text(self.root, fg="black", wrap=tk.WORD, height=18)
        self.consoleArea.pack()
        self.root.mainloop()

    def askuser(self):
        if ((self.v.get() == "") or (self.v1.get() == "") or (self.v2.get() == "") or (self.v3.get() == "") or (
                self.v4.get() == "") or (self.v5.get() == "")):
            return tk.messagebox.showinfo('ATTENTION!', f"You Don't Have Selected All Options ")
        elif ((self.v.get() == "0") and (self.v1.get() == "0") and (self.v2.get() == "0") and (self.v3.get() == "0") and (
                self.v4.get() == "0") and (self.v5.get() == "0")):
            return tk.messagebox.showinfo('ATTENTION!', f"If your health is great, you don't need to go to the hospital")
        else:
            self.consoleArea.delete("1.0", tk.END)
            choice = self.v.get()
            choice1 = self.v1.get()
            choice2 = self.v2.get()
            choice3 = self.v3.get()
            choice4 = self.v4.get()
            choice5 = self.v5.get()
            self.res = [choice, choice1, choice2, choice3, choice4, choice5]
            userhealth = [self.res]
            classifier = ClassifierA("DataSet.csv")
            self.consoleArea.insert(tk.INSERT, classifier.classify(userhealth))

    def testClassifier(self):
        self.consoleArea.delete("1.0", tk.END)
        classifier = ClassifierA("DataSet.csv")
        resultTest = classifier.cross_validation()+"\n"+classifier.metrix_test()
        self.consoleArea.insert(tk.INSERT, resultTest)
