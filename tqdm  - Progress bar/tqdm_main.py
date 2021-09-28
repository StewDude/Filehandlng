from tqdm import tqdm
import argh
import time

def show_bar(whole_time = 1000, slice_time = 0.01):
    for i in tqdm(range(whole_time)):
        time.sleep(slice_time)

if __name__ == "__main__":
    argh.dispatch_command(show_bar)