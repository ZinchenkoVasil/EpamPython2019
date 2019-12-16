# Программа клиента для отправки приветствия серверу и получения ответа
import argparse
import sys
import os
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-model', dest='model', action='store', type=str, required=False, help='model name (DT, RF, GBoost)', default='Gboost')
    parser.add_argument('-count_trees', dest='count_trees', action='store', type=int, required=False, help='count of trees', default=20)
    parser.add_argument('-max_deepth', dest='max_deepth', action='store', type=int, required=False, help='max deepth of tree', default=10)
    parser.add_argument('-max_count_leafs', dest='max_count_leafs', action='store', type=int, required=False, help='max count of leafs', default=10)
    parser.add_argument('-train', dest='train_dataset', action='store', type=str, required=False, help='input CSV file (train dataset)', default='train.csv')
    parser.add_argument('-test', dest='test_dataset', action='store', type=str, required=False, help='input CSV file (test dataset)', default='test.csv')
    parser.add_argument('-out', dest='out_storage', action='store', type=str, required=False, help='storage for saving model', default='out')

    args = parser.parse_args(sys.argv[1:])
    train_dataset = args.train_dataset
    test_dataset = args.test_dataset
    if not os.path.exists(train_dataset):
        raise ValueError("Train dataset file not found!")
    if not os.path.exists(test_dataset):
        raise ValueError("Test dataset file not found!")
    out_storage = args.out_storage
    if os.path.exists(out_storage) and os.path.isdir(out_storage):
        pass
    else:
        urls = re.findall("(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?",out_storage)
        if urls:
            out_storage = urls[0]
        else:
            raise ValueError("out storage not found!")

    if (args.model == 'DT') or (args.model == 'dt'):
        max_deepth = args.max_deepth
        max_count_leafs = args.max_count_leafs
    elif (args.model == 'RF') or (args.model == 'rf') or (args.model == 'RandomForest'):
        max_deepth = args.max_deepth
        count_trees = args.count_trees
    elif (args.model == 'GBoost') or (args.model == 'gboost') or (args.model == 'Gboost'):
        count_trees = args.count_trees
    else:
        raise ValueError("Model aren't supported")


