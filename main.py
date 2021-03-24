#!/usr/bin/python
# -*- coding: UTF-8 -*-
import torch.nn.functional as F
import torch
import torch
import torch.nn as nn
from torch.autograd import Variable
import torchvision.models as models
from torchvision import transforms, utils
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import numpy as np
import torch.optim as optim
from data_load_treatment import MyDataset, devide_test_train, default_loader


def main():
    # 设置数据集大小
    devide_test_train(2000)
    train_data = MyDataset(txt='train.txt', transform=transforms.ToTensor())
    test_data = MyDataset(txt='test.txt', transform=transforms.ToTensor())
    # 然后就是调用DataLoader和刚刚创建的数据集，来创建dataloader，这里提一句，loader的长度是有多少个batch，所以和batch_size有关
    train_loader = DataLoader(
        dataset=train_data,
        batch_size=6,
        shuffle=True,
        num_workers=4
    )
# dataset：Dataset类型，从其中加载数据
# batch_size：int，可选。每个batch加载多少样本
# shuffle：bool，可选。为True时表示每个epoch都对数据进行洗牌
# sampler：Sampler，可选。从数据集中采样样本的方法。
# num_workers：int，可选。加载数据时使用多少子进程。默认值为0，表示在主进程中加载数据。
# collate_fn：callable，可选。
# pin_memory：bool，可选
# drop_last：bool，可选。True表示如果最后剩下不完全的batch, 丢弃。False表示不丢弃。
    test_loader = DataLoader(
        dataset=test_data,
        batch_size=6,
        shuffle=False,
        num_workers=4
    )
    print('num_of_trainData:', len(train_data))
    print('num_of_testData:', len(test_data))
    return 0


if __name__ == '__main__':
    # pil_img = Image.open("F:\化学人的大创\开始github\pic_of_molecules\\500.png")
    # img = np.array(pil_img)
    main()
