"""
图片数据的小批量加载
"""

import os
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import torch
from typing import Any, Tuple
import matplotlib.pyplot as plt


class CaptchaDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        self.imgs = os.listdir(data_dir)

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        img_path = os.path.join(self.data_dir, self.imgs[idx])
        str_label = self.imgs[idx].split("_")[0]
        img = Image.open(img_path)
        if self.transform:
            img = self.transform(img)
        else:
            # 将 img 转为 tensor
            img = transforms.ToTensor()(img)

        label = torch.tensor(list(map(int, str_label)), dtype=torch.long)
        return (img, label)


if __name__ == '__main__':
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.Grayscale(num_output_channels=1),
        transforms.ToTensor()
    ])

    dataset = CaptchaDataset("./data/train", transform=None)
    train_loader = DataLoader(dataset, batch_size=8, shuffle=True)

    def show_img(imgs: list[torch.Tensor], labels):
        import matplotlib.pyplot as plt
        total = len(imgs)
        print(f'total: {total}')
        for i in range(total):
            plt.subplot(2, total // 2, i + 1)
            img = imgs[i]
            label = labels[i]
            label = ''.join(map(str, label.tolist()))
            img = img.numpy().transpose((1, 2, 0))
            plt.imshow(img)
            plt.axis('off')
            plt.title(label)

        plt.show()

    for epoch in range(1):
        print(f'epoch = {epoch}')
        for batch_idx, (imgs, labels) in enumerate(train_loader):
            show_img(imgs, labels)
            break
        print('---')
