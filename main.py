from customtkinter import *

class SetProxy(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('500x300')
        self.title("Set npm proxy")

        # set default properties
        self.proxy_string = "proxy=http://"
        self.https_proxy_string = "https-proxy=http://"

        self.default_port = StringVar(value="8080")

        # define file title
        self.file_title = '.npmrc'

        # fetch previous proxy
        self.previous_proxy_url = self.fetch_previous_proxy()

        # run create widgets function
        self.create_widgets()




    def create_widgets(self):

        self.proxy_frame = CTkFrame(self, width=100, height=50)
        self.proxy_frame.pack()

        self.https_proxy_frame = CTkFrame(self, width=100, height=50)
        self.https_proxy_frame.pack()

        # title [proxy url title]
        self.proxy_url_title = CTkLabel(self.proxy_frame, text="url")
        self.proxy_url_title.pack(side="left" ,pady=20)

        # title [proxy port title]
        self.proxy_port_title = CTkLabel(self.https_proxy_frame, text="port")
        self.proxy_port_title.pack(side="left" ,pady=20)

        # entry [proxy url entry]
        self.proxy_url = CTkEntry(self.proxy_frame, width=200, textvariable=StringVar(value=self.previous_proxy_url ))
        self.proxy_url.pack(side="left" , pady=20, padx=20)

        # entry [proxy port entry]
        self.proxy_port = CTkEntry(self.https_proxy_frame, width=200, textvariable=self.default_port)
        self.proxy_port.pack(side="left" , pady=20, padx=20)

        self.button_apply = CTkButton(self, text="Apply",fg_color="green", command=self.apply_proxy)
        self.button_apply.pack(pady=20, padx=20)

        self.button_disable = CTkButton(self, text="disable",fg_color="red", command=self.disable_proxy)
        self.button_disable.pack(pady=20, padx=20)
    
    def apply_proxy(self):
        val_proxy_url = self.proxy_url.get()
        proxy_port = self.proxy_port.get()
        try:
            with open(self.file_title, 'r+') as npm_proxy_file:
                self.new_proxy = f"{self.proxy_string}{val_proxy_url}:{proxy_port}"
                self.new_port = f"{self.https_proxy_string}{val_proxy_url}:{proxy_port}"

                content = f"{self.new_proxy}\n{self.new_port}"

                print(content)

                npm_proxy_file.seek(0)
                npm_proxy_file.write(content)

        except FileNotFoundError:
            print("No previous proxy URL")


    def disable_proxy(self):
        val_proxy_url = self.proxy_url.get()
        proxy_port = self.proxy_port.get()
        try:
            with open(self.file_title, 'r+') as npm_proxy_file:
                self.new_proxy = f"#{self.proxy_string}{val_proxy_url}:{proxy_port}"
                self.new_port = f"#{self.https_proxy_string}{val_proxy_url}:{proxy_port}"

                content = f"{self.new_proxy}\n{self.new_port}"

                print(content)

                npm_proxy_file.seek(0)
                npm_proxy_file.write(content)

        except FileNotFoundError:
            print("No previous proxy URL")

    def fetch_previous_proxy(self):
        """Fetches the previous proxy from the specified file.
        Args:
            file_path (str, optional): The path to the .npmrc file. Defaults to ".npmrc".

        Returns:
            str: The previous proxy URL or an empty string if not found.
        """
        try:
            with open(self.file_title, 'r') as npm_proxy_file:
                previous_port_url = npm_proxy_file.readlines(1)[0].split('//')[1].split(':')[0]
                return previous_port_url
        except FileNotFoundError:
            print("No previous proxy URL")


app = SetProxy()
app.mainloop()
