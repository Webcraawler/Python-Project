import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import Image,ImageTk


class newss:
    def __init__(self):
        #fetch news
        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=4a7feec124124410a972d62e615dd6c1").json()
        #gui
        self.load_gui()
        #show 1st news
        self.load_news(0)


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news(self,index):
        #to go to next news we firt have to clear the screen
        self.clear()

        heading = Label(self.root,text=self.data["articles"][index]["title"],bg="black",fg="white",wraplength=450,justify="center")
        heading.pack(pady=(10,20))
        heading.config(font=("verdana",14))

        try:
            img_url = self.data["articles"][index]["urlToImage"]
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data))
            im1 = im.resize((450,350))
            img = ImageTk.PhotoImage(im1)
            img_label = Label(self.root,image=img)
            img_label.pack()
        except:
            img_url = "https://cdn.vectorstock.com/i/preview-1x/82/99/no-image-available-like-missing-picture-vector-43938299.jpg"
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data))
            im1 = im.resize((450, 350))
            img = ImageTk.PhotoImage(im1)
            img_label = Label(self.root, image=img)
            img_label.pack()


        details = Label(self.root, text=self.data["articles"][index]["description"], bg="black", fg="white", wraplength=450,
                        justify="center")
        details.pack(pady=(5, 20))
        details.config(font=("verdana", 12))


        frame = Frame(self.root,bg="black")
        frame.pack(expand=True,fill=BOTH)

        if index != 0:
            prev = Button(frame,text="Previous",width=10,height=2,command=lambda :self.load_news(index-1))
            prev.pack(side=LEFT,padx=(55,0))
            prev.config(font=("verdana",14))

        Read = Button(frame, text="Read More", width=10, height=2,command=lambda :self.open_link(self.data["articles"][index]["url"]))
        Read.pack(side=LEFT)
        Read.config(font=("verdana", 14))


        if index!=len(self.data["articles"])-1:
            Next = Button(frame, text="Next", width=10, height=2,command=lambda :self.load_news(index+1))
            Next.pack(side=LEFT)
            Next.config(font=("verdana", 14))

        self.root.mainloop()

    def open_link(self,url):
        # webbrowser.get("chrome").open(url)
        webbrowser.open(url)
    def load_gui(self):
        self.root = Tk()
        self.root.title("NewsApp")
        self.root.geometry("500x700")
        self.root.resizable(0,0)
        self.root.config(background="black")



o = newss()