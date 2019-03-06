import matplotlib.pyplot as plt


form sklearn.model_selection import cross_validate
from sklearn.metrics import roc_curve, cros
from sklearn.metrics import confusion_matrix, classification_report

from mlxtend.plotting import plot_confusion_matrix


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
    # y_pred = clf.predict(x_test)

    probs = probs[:, 1]

    auc = roc_auc_score(y_test, probs)
    print(f'AUC: {auc}')

    fpr, tpr, thresholds = roc_curve(y_test, probs)
    plot_roc_curve(fpr, tpr)


def print_confmat(x_test, y_test, clf):
    y_pred = clf.predict(x_test)

    matrix = confusion_matrix(y_test, y_pred)

    print(matrix)
    print(classification_report(y_test, y_pred))

    fig, ax = plot_confusion_matrix(conf_mat=matrix,
                                    show_absolute=True,
                                    show_normed=True,
                                    colorbar=True)

    plt.show()
    print(roc_auc_score(y_test, y_pred))


def crossval(scoring=None, clf, X, y, plot=False):
    if not scoring:
        scoring = ['precision_macro', 'recall_macro', 'f1', 'average_precision']

    scores = cross_validate(clf, X, y, scoring=scoring,
                            cv=10, return_train_score=False)

    score_df = pd.DataFrame(scores)

    if plot:
        sns.lineplot(data=score_df.drop(['fit_time', 'score_time'], axis=1))

    return score_df

    
