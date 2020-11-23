from alert_box import display_message_mac
from time import sleep
import exercises
import random
from datetime import datetime


class Exercise:
    COUNT = 0
    START_TIME = datetime.now()

    def wormup(self):
        return random.choice(exercises.WORMUP)

    def midtraining(self):
        return random.choice(exercises.MID)

    def end_training(self):
        return random.choice(exercises.END)

    def check_time_for_exercise(self):
        if self.COUNT <= 5:
            return self.wormup()
        elif 5 < self.COUNT <= 15:
            return self.midtraining()
        else:
            return self.end_training()

    def run(self):
        print(f"Starting exercise at {self.START_TIME}")
        while True:
            exercies = self.check_time_for_exercise()
            a = display_message_mac(exercies, "Title here")
            print(a)
            sleep(30*60)
            self.COUNT += 1
            if a == "EXIT":
                print(f"Exercise finished {datetime.now()}")
                print(f"Working time = {datetime.now() - self.START_TIME}")
                break


if __name__ == "__main__":
    e = Exercise()
    e.run()

