import tkinter
import threading


class Hydra:

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
        # Create two new threads and call the function call_hydra
        hydra_thread_1 = threading.Thread(target=call_hydra)
        hydra_thread_2 = threading.Thread(target=call_hydra)
        # Start the threads
        hydra_thread_1.start()
        hydra_thread_2.start()
        # If threads end, they will be called
        hydra_thread_1.join()
        hydra_thread_2.join()


def call_hydra():
    # Create a new Hydra object
    hydra = Hydra()


def call_hydra_thread():
    # Create a new thread and call the function call_hydra
    hydra_thread = threading.Thread(target=call_hydra)
    # Start the thread
    hydra_thread.start()
    # If thread ends, it will be called
    hydra_thread.join()
    # Open another window
    # call_hydra_thread()


if __name__ == "__main__":
    call_hydra_thread()
