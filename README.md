# simple-ai-app

A simple application using an AI model trained on the CIFAR-10 dataset can classify images into 10 categories sucha as airplanes, cars, birds, cats, deers, dogs, frogs, horse, ships, trucks. The app allows user to upload an image, processes it using a lightweight convolutional neural network, and displays the predicted category.

<img width="800" alt="Zrzut ekranu 2024-12-9 o 14 56 15" src="https://github.com/user-attachments/assets/ad002139-a3b6-437d-8b47-1e693ca2e58e">

## Model architecture and training results

| Layer (type)               | Output Shape          | Param #     |
|----------------------------|-----------------------|-------------|
| **conv2d (Conv2D)**        | (None, 30, 30, 32)   | 896         |
| **batch_normalization**    | (None, 30, 30, 32)   | 128         |
| **conv2d_1 (Conv2D)**      | (None, 28, 28, 64)   | 18,496      |
| **batch_normalization_1**  | (None, 28, 28, 64)   | 256         |
| **conv2d_2 (Conv2D)**      | (None, 26, 26, 128)  | 73,856      |
| **batch_normalization_2**  | (None, 26, 26, 128)  | 512         |
| **flatten (Flatten)**      | (None, 86528)        | 0           |
| **dense (Dense)**          | (None, 64)           | 5,537,856   |
| **batch_normalization_3**  | (None, 64)           | 256         |
| **dense_1 (Dense)**        | (None, 10)           | 650         |

---

**Total Parameters**: 5,632,906  
**Trainable Parameters**: 5,632,330  
**Non-Trainable Parameters**: 576

### Training Results

| **Epoch** | **Training Loss** | **Training Accuracy** | **Validation Loss** | **Validation Accuracy** |
|-----------|-------------------|-----------------------|---------------------|-------------------------|
| 1         | 1.2107            | 57.44%               | 2.4382              | 23.13%                 |
| 2         | 0.7618            | 73.53%               | 0.9650              | 67.32%                 |
| 1         | 1.0810            | 62.06%               | 1.2267              | 59.38%                 |
| 2         | 0.9799            | 65.57%               | 0.8815              | 69.57%                 |
| 3         | 0.9100            | 67.97%               | 0.8877              | 69.23%                 |
| 4         | 0.8698            | 69.42%               | 0.8668              | 70.06%                 |
| 5         | 0.8388            | 70.50%               | 0.8094              | 72.30%                 |
| 6         | 0.8072            | 71.87%               | 0.7768              | 72.79%                 |
| 7         | 0.7803            | 72.63%               | 0.7646              | 73.69%                 |
| 8         | 0.7599            | 73.39%               | 0.8375              | 72.25%                 |
| 9         | 0.7448            | 73.86%               | 0.7193              | 75.14%                 |
| 10        | 0.7281            | 74.64%               | 0.6975              | 76.31%                 |
| 11        | 0.7092            | 75.17%               | 0.6660              | 76.96%                 |
| 12        | 0.6913            | 75.92%               | 0.8552              | 72.58%                 |
| 13        | 0.6816            | 76.25%               | 0.8275              | 72.69%                 |
| 14        | 0.6719            | 76.50%               | 0.7484              | 75.41%                 |
| 15        | 0.6545            | 77.20%               | 0.7072              | 77.03%                 |
| 16        | 0.6538            | 77.11%               | 0.6546              | 78.29%                 |
| 17        | 0.6425            | 77.52%               | 0.7131              | 76.28%                 |
| 18        | 0.6364            | 77.71%               | 0.5873              | 80.05%                 |
| 19        | 0.6242            | 78.10%               | 0.6367              | 78.99%                 |
| 20        | 0.6103            | 78.61%               | 0.6292              | 79.64%                 |
| 1         | 0.3582            | 87.63%               | 0.4839              | 83.45%                 |
| 2         | 0.1634            | 95.44%               | 0.5235              | 82.73%                 |
| 3         | 0.0532            | 99.18%               | 0.6033              | 82.41%                 |
| 4         | 0.0166            | 99.92%               | 0.5939              | 82.44%                 |
| 5         | 0.0073            | 99.99%               | 0.5908              | 83.83%                 |

**Final Accuracy**: **83.83%**
