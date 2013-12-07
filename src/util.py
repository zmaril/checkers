import matplotlib.pyplot as plt 
from IPython.display import display

rd = 0.25
def draw_game(B,R,n):
    fig = plt.gcf()
    fig.set_size_inches(5,5)
    ax = plt.gca()
    ax.grid(True)
    ax.set_xlim((0,n))
    ax.set_ylim((0,n))
    ax.get_xaxis().set_ticklabels([])
    ax.get_yaxis().set_ticklabels([])
    plt.title((B,R,n))
    if B == range(0,n):
        fig.patch.set_facecolor('green')
    if len(B) == 2*n:
        fig.patch.set_facecolor('blue')
    elif B == range(0,n)[::-1]:
        fig.patch.set_facecolor('yellow')

    for i in range(0,n):
        r = R[i]
        b = B[i]
        if (r == b):
            ax.add_artist(plt.Circle((0.65+i,n-(0.35+R[i])),rd,color='red'))
            ax.add_artist(plt.Circle((0.35+i,n-(0.65+B[i])),rd,color='black'))
        else:
            ax.add_artist(plt.Circle((0.5+i,n-(0.5+R[i])),rd,color='red'))
            ax.add_artist(plt.Circle((0.5+i,n-(0.5+B[i])),rd,color='black'))
    plt.figure()
