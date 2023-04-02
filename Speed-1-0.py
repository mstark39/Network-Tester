import speedtest
import tkinter as tk


class InternetSpeedTracker:
    def __init__(self, interval):
        self.interval = interval
        self.speedtester = speedtest.Speedtest()
        self.speedtester.get_best_server()
        self.root = tk.Tk()
        self.root.title("Internet Speed Tracker")
        self.speed_label = tk.Label(text="Testing internet speed...", font=("Arial", 24))
        self.speed_label.pack(pady=20)
        self.refresh_button = tk.Button(text="Refresh", command=self.check_speed)
        self.refresh_button.pack(pady=10)
        self.interval_label = tk.Label(text=f"Test interval: {self.interval/1000} seconds", font=("Arial", 14))
        self.interval_label.pack(pady=10)
        self.one_minute_button = tk.Button(text="1 minute", command=lambda: self.set_interval(60*1000))
        self.one_minute_button.pack(pady=5)
        self.five_minute_button = tk.Button(text="5 minutes", command=lambda: self.set_interval(5*60*1000))
        self.five_minute_button.pack(pady=5)
        self.ten_minute_button = tk.Button(text="10 minutes", command=lambda: self.set_interval(10*60*1000))
        self.ten_minute_button.pack(pady=5)
        self.stop_button = tk.Button(text="Stop", command=self.stop)
        self.stop_button.pack(pady=5)
        self.root.after(self.interval, self.check_speed)
        self.root.mainloop()

    def check_speed(self):
        download_speed = round(self.speedtester.download() / 1_000_000, 2)
        if download_speed >= 5:
            self.speed_label.configure(text=f"Download speed: {download_speed} Mbps", fg="green")
        elif download_speed < 5:
            self.speed_label.configure(text=f"Download speed: {download_speed} Mbps", fg="yellow")
        else:
            self.speed_label.configure(text="No internet connection", fg="red")
        if download_speed >= 5:
            self.interval_label.configure(text=f"Test interval: {self.interval/1000} seconds", fg="black")
            self.root.after(10*60*1000, lambda: self.set_interval(10*60*1000))
        else:
            self.interval_label.configure(text=f"Test interval: {self.interval/1000} seconds", fg="red")
            self.root.after(60*1000, self.check_speed)

    def set_interval(self, interval):
        self.interval = interval
        self.interval_label.configure(text=f"Test interval: {self.interval/1000} seconds")
        self.root.after(self.interval, self.check_speed)

    def stop(self):
        if self.stop_button.cget("text") == "Stop":
            self.stop_button.configure(text="Start")
            self.root.after_cancel(self.root.after_id)
        else:
            self.stop_button.configure(text="Stop")
            self.root.after(self.interval, self.check_speed)


tracker = InternetSpeedTracker(60000)
