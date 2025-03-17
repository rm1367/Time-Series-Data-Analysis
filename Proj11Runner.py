import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

class Runner:
    def __init__(self, args):

        self.file_name = args[0]
        self.index_col = args[1]
        self.start_date = args[2]
        self.end_date = args [3]
        self.start_col = args[4]
        self.end_col = args[5]

    def run(self):

        data = pd.read_csv(self.file_name, index_col = self.index_col)

        data2 = data.loc[self.start_date:self.end_date]

        data3 = data2.loc[:,self.start_col:self.end_col]

        data4=data3.transpose()

        fig, (ax1) = plt.subplots(1,1,facecolor='0.75',linewidth=3,edgecolor='Black')

        data4.plot(ax=ax1, grid =True)
        ax1.set_xlabel('Category')
        ax1.set_ylabel('Value')
        ax1.set_title('Stock Prices')

        fig.suptitle(f"args = ['{self.file_name}','{self.index_col}','{self.start_date}','{self.end_date}','{self.start_col}','{self.end_col}']\n"
                     '\n'
                     'I certify that this program is my own work\n'
                     'and is not the work of others. I agree\n'
                     'not to share my solution with others.\n'
                     'Ryan Maldonado', horizontalalignment='center')


        plt.tight_layout()
        fig.savefig("Proj11.jpg")
        plt.show()







    
