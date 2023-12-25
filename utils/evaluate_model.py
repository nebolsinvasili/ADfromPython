import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

from utils.plot import cm


def evaluate(model, features, target):
    predict = model.predict(features)

    plt.figure(figsize=cm(inch=[45, 8]))
    plt.style.use('default')
    plt.plot(target.index, target, label='test')
    plt.plot(target.index, predict, label='predict')
    plt.legend()
    plt.xlabel('Time, pt')
    plt.show()

    #Соотношение ответов
    plt.scatter(target,predict)
    plt.xlabel('Правильные значения')
    plt.ylabel('Предсказания')
    plt.axis('equal')
    plt.xlim(plt.xlim())
    plt.ylim(plt.ylim())
    plt.plot([-10, 10],[-10, 10])
    plt.show()

    print('MSE: ', mean_squared_error(y_true=target, y_pred=predict).round(3))
    print('R2: ', r2_score(y_true=target, y_pred=predict).round(3))