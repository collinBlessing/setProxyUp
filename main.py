from customtkinter import *

class SetProxy(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('500x300')
        self.title("Set npm proxy")
        self.create_widgets()

    def create_widgets(self):

        self.proxy_frame = CTkFrame(self, width=100, height=50)
        self.proxy_frame.pack()

        self.https_proxy_frame = CTkFrame(self, width=100, height=50)
        self.https_proxy_frame.pack()

        # title [proxy]
        self.proxy_title = CTkLabel(self.proxy_frame, text="proxy")
        self.proxy_title.pack(side="left" ,pady=20)

        # title [https-proxy]
        self.proxy_title = CTkLabel(self.https_proxy_frame, text="https-proxy")
        self.proxy_title.pack(side="left" ,pady=20)

        # entry [proxy]
        self.entry_proxy = CTkEntry(self.proxy_frame, width=200)
        self.entry_proxy.pack(side="left" , pady=20, padx=20)

        # entry [https-proxy]
        self.entry_proxy = CTkEntry(self.https_proxy_frame, width=200)
        self.entry_proxy.pack(side="left" , pady=20, padx=20)

        self.button_apply = CTkButton(self, text="Apply", command=self.apply_proxy)
        self.button_apply.pack(pady=20, padx=20)
    
    def apply_proxy(self):
        proxy_value = self.entry_proxy.get()
        print(f"Applying npm proxy to: {proxy_value}")

app = SetProxy()
app.mainloop()
