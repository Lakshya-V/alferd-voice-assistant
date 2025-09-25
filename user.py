import customtkinter as ctk
import threading
import main
import sys
from PIL import Image, ImageTk

class TextboxRedirector:
    def __init__(self, textbox):
        self.textbox = textbox

    def write(self, text):
        self.textbox.insert(ctk.END, text)
        self.textbox.see(ctk.END)

    def flush(self):
        pass  # Needed for compatibility

class VoiceAssistantApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.title("ALFERD")
        self.geometry("1220x600") 
        bg_image = Image.open("assets/bgia.png")  
        bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = ctk.CTkLabel(self, image=bg_photo, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.image = bg_photo  
        
        self.start_button = ctk.CTkButton(self, height=35,width=100,  bg_color="transparent",fg_color="darkgreen",hover_color="black", text="WAKE", corner_radius=2, command=self.start_assistant_thread)
        self.start_button.pack(pady=80)

        self.output_textbox = ctk.CTkTextbox(self, width=900, height=200, corner_radius=2, fg_color="white",text_color="black",border_spacing=10)
        self.output_textbox.pack(pady=40)

        self.stop_button = ctk.CTkButton(self, height=35,width=100, bg_color="transparent",fg_color="navyblue",hover_color="black", text="SLEEP", corner_radius=2, command=self.stop_assistant_thread, state="disabled")
        self.stop_button.pack(pady=45)

        self.stop_event = threading.Event()

    def start_assistant_thread(self):
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        self.output_textbox.delete("1.0", ctk.END) 
        self.update_output("Starting voice assistant...\n")

        self.stop_event.clear()  
        self.assistant_thread = threading.Thread(target=self.run_assistant)
        self.assistant_thread.daemon = True
        self.assistant_thread.start()

    def stop_assistant_thread(self):
        self.update_output("Stopping assistant... please wait a few minutes....\n")
        self.stop_event.set() 
        self.stop_button.configure(state="disabled") 

    def update_output(self, text):
        self.output_textbox.insert(ctk.END, f"{text}\n")
        self.output_textbox.see(ctk.END)

    def run_assistant(self):
        old_stdout, old_stderr = sys.stdout, sys.stderr
        sys.stdout = sys.stderr = TextboxRedirector(self.output_textbox)
        try:
            main.final(stop_event=self.stop_event)  
        except Exception as e:
            print(f"Error: {e}")
        finally:
            sys.stdout, sys.stderr = old_stdout, old_stderr
            self.update_output("Assistant has finished. Click the button to start again.\n")
            self.start_button.configure(state="normal")
            self.stop_button.configure(state="disabled")


if __name__ =="__main__" :
    app = VoiceAssistantApp()
    app.mainloop()


