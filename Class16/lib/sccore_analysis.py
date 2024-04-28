import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from numpy import *
import pandas as pd
import pickle as pkl


def plot_scores(styled_logs,title=None,normalize=True):
    plt.figure(figsize=(8, 6))

    patches=[]
    for st_log in styled_logs:
        style=st_log['style']
        log=st_log['log']
        
        #find normalization constants
        if normalize:
            all_pred=[]
            for i in range(len(log)):
                X=log[i]
                y_pred=X['y_pred']
                all_pred.append(y_pred)
            all_pred=concatenate(all_pred)
            _mean=mean(all_pred)
            _std=std(all_pred)
        else:
            _mean=0
            _std=1

        for i in range(len(log)):
            X=log[i]
            y_pred=X['y_pred']
            y_test=X['y_test']
            y_pred=(y_pred-_mean)/_std
            thresholds = sorted(np.unique(np.round(y_pred, 2)))
            error_pos, error_neg = get_error_values(y_pred, y_test, thresholds)
            neg_line, = plot(thresholds,error_neg,style[0],lw=0.5)
            pos_line, = plot(thresholds,error_pos,style[1],lw=0.5)
        patch = mpatches.Patch(color=st_log['label_color'], label=st_log['label'])
        patches.append(patch)
    grid(linestyle='-', linewidth='0.5', color='gray')
    plt.xlabel('Score')
    plt.ylabel('Error %')

    legend(handles=patches)
    if title:
        plt.title(title)
