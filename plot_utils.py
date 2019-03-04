import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve


def plot_roc_curve(fpr, tpr):
    plt.plot(fpr, tpr, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()


def classification_info(x_test, y_test, clf):
    probs = clf.predict_proba(x_test)
    y_pred = clf.predict(x_test)
    
    probs = probs[:, 1]

    auc = roc_auc_score(testy, probs)
    print('AUC: %.2f' % auc)

    fpr, tpr, thresholds = roc_curve(testy, probs)
    plot_roc_curve(fpr, tpr)
