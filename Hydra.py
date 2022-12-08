import threading
import tkinter

try:
    from winsound import MB_ICONASTERISK, MessageBeep
except ImportError:
    # Define winsound.MessageBeep() as a dummy function
    def MessageBeep(*args, **kwargs):
        pass
    MB_ICONASTERISK = 0


class Hydra:

    def play_sound(self):
        # MessageBeep(MB_ICONASTERISK)
        threading.Thread(target=MessageBeep, args=(MB_ICONASTERISK,)).start()

    def create_window(self):
        # Create a window with title and message, if closed it will call the function close_window
        self.window = tkinter.Tk()
        self.window.title("Hydra")
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)
        # self.window.geometry("300x100")
        # self.window.resizable(False, False)
        self.window.configure(background="black")
        self.label = tkinter.Label(
            self.window, text="Cut off one head, two more shall take its place!", bg="black", fg="white", font="none 16 bold")
        self.label.pack()
        self.window.mainloop()

    def __init__(self):
        self.create_window()

    def close_window(self):
        # Close the window
        self.window.destroy()
        # Play a sound
        self.play_sound()
        # Create two new threads and call the function call_hydra
        hydra_thread_1 = threading.Thread(target=self.call_hydra)
        hydra_thread_2 = threading.Thread(target=self.call_hydra)
        # Start the threads
        hydra_thread_1.start()
        hydra_thread_2.start()
        # If threads end, they will be called
        hydra_thread_1.join()
        hydra_thread_2.join()

    def call_hydra(self):
        # Create a new Hydra object
        hydra = self.__class__()
        return hydra


if __name__ == "__main__":
    # Create a new Hydra object
    hydra = Hydra()
