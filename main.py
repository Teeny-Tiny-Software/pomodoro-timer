import time
import sys

DEFAULT_WORK_DURATION = 25
DEFAULT_BREAK_DURATION = 5

def pomodoro_timer(work_duration, break_duration):
    while True:
        print("Work time! Focus for {} minutes.".format(work_duration))
        time.sleep(work_duration * 60)
        print("Break time! Relax for {} minutes.".format(break_duration))
        time.sleep(break_duration * 60)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        work_duration = int(sys.argv[1])
        break_duration = int(sys.argv[2])
    else:
        print("Usage: python pomodoro.py [work_duration] [break_duration]")
        print(f"Using default values: {DEFAULT_WORK_DURATION} minutes work, {DEFAULT_BREAK_DURATION} minutes break")
        work_duration = DEFAULT_WORK_DURATION
        break_duration = DEFAULT_BREAK_DURATION

    pomodoro_timer(work_duration, break_duration)
