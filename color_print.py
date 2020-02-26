from termcolor import colored

def _get_accuracy_color(accuracy):
    # TODO find a continuous mapping in rgb/hex space
    if accuracy > .75:
        color = 'green'
    elif accuracy > .5:
        color = 'yellow'
    else:
        color = 'red'
    return color
    # print(colored('{}_accuracy: {}'.format(name, accuracy), color))

def print_training_acc(train_acc, test_acc):
    train_msg = colored('train_acc: {}'.format(train_acc), _get_accuracy_color(train_acc))
    test_msg = colored('test_acc: {}'.format(test_acc), _get_accuracy_color(test_acc))
    print('{} {}'.format(train_msg, test_msg))

    ''' TODO
    this format is kind of cool
    Epoch 24/24
    ----------
    train Loss: 0.3255 Acc: 0.8443
    val Loss: 0.2181 Acc: 0.9085

    '''

