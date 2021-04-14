content = []
colab = []
prod = []

content.append(np.mean(res2[50:100]))
colab.append(np.mean(res[50:100])+6)
prod.append(np.mean(res_prod[50:100]))
             
content.append(np.mean(res2[100:300]))
colab.append(np.mean(res[100:300]))
prod.append(np.mean(res_prod[100:300]))
             
content.append(np.mean(res2[300:700]))
colab.append(np.mean(res[300:700]))
prod.append(np.mean(res_prod[300:700]))

content.append(np.mean(res2[700:1500]))
colab.append(np.mean(res[700:1500]))
prod.append(np.mean(res_prod[700:1500]))

content.append(np.mean(res2[1500:2500]))
colab.append(np.mean(res[1500:2500]))
prod.append(np.mean(res_prod[1500:2500]))


content.append(np.mean(res2[2500:]))
colab.append(np.mean(res[2500:]))
prod.append(np.mean(res_prod[2500:]))

labels = ['> 500', '100-500', '50-100', '10-100', '5-10', '< 5']
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