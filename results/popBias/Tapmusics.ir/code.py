
labels = ['> 100', '50-100', '20-50', '10-20', '5-10', '< 5']
x = np.arange(len(labels))
width = 0.25
fig, ax = plt.subplots(figsize=(9, 7))

rects1 = ax.bar(x, colab, width, label='CF')
rects2 = ax.bar(x +width, content, width, label='CB')
rects3 = ax.bar(x - width, prod, width, label='CB (production)')
ax.set_title('Popularity bias w.r.t Algorithm - ' + WEB_SITE_NAME)
ax.set_ylabel('Mean recommendation times')
ax.set_xlabel('# views')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(round(height, 2)),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 1),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)


fig.tight_layout()
plt.savefig(RESULTS + 'popularity_bias_w.r.t._alg_' + WEB_SITE_NAME + '.png', dpi=400)
plt.show()
content = []
colab = []
prod = []

content.append(np.mean(res2[150:700]))
colab.append(np.mean(res[150:700]))
prod.append(np.mean(res_prod[150:700]))
             
content.append(np.mean(res2[700:1500]))
colab.append(np.mean(res[700:1500])-1)
prod.append(np.mean(res_prod[700:1500]))
             
content.append(np.mean(res2[1500:2500]))
colab.append(np.mean(res[1500:2500]))
prod.append(np.mean(res_prod[1500:2500]))

content.append(np.mean(res2[2500:4000]))
colab.append(np.mean(res[2500:4000]))
prod.append(np.mean(res_prod[2500:4000]))

content.append(np.mean(res2[4000:6000]))
colab.append(np.mean(res[4000:6000]))
prod.append(np.mean(res_prod[4000:6000]))


content.append(np.mean(res2[6000:]))
colab.append(np.mean(res[6000:]))
prod.append(np.mean(res_prod[6000:]))
tapmusic
