import csv
import numpy as np
import matplotlib.pyplot as plt


class plot():
    def __init__(self, flag):
        sin = []
        ans = []
        
        with open("sin.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                sin.append(row)
                
        if flag:
            with open("ans.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    ans.append(row)
        
        sin = np.array(sin).T
        
        if flag:
            ans = np.array(ans).T
        
        fig = plt.figure()
        ax1 = fig.add_subplot(211)
        ax1.plot(sin[0], sin[1], label='A=1, f=1')
        ax1.plot(sin[0], sin[2], label='A=2, f=2')
        ax1.plot(sin[0], sin[3], label='A=1, f=3')
        ax1.legend()
        if flag:
            ax2 = fig.add_subplot(212)
            ax2.plot(ans[0], ans[1], label='Answer')
            ax2.legend(loc="lower left")
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    p = plot(False)