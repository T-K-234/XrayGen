# XRayGen – Synthetic Chest X-Ray Image Generation using ACGAN

## Project Overview

**XRayGen** is a deep learning project that generates **synthetic chest X-ray images** using **Auxiliary Classifier Generative Adversarial Networks (ACGANs)**. The goal of the project is to **enhance pneumonia detection datasets by generating realistic synthetic medical images**.

Medical imaging datasets are often limited and imbalanced, especially in healthcare applications. XRayGen addresses this challenge by creating **high-quality synthetic X-ray images classified as either Normal or Pneumonia**, helping improve dataset balance and machine learning model performance.

The generated images can be used to **augment training datasets**, improving the **generalization ability of medical image classification models**.

---

# Introduction

Chest X-ray imaging is widely used for diagnosing lung diseases such as **pneumonia**. However, many deep learning models require large datasets to achieve high accuracy.

Medical datasets often suffer from:

* Limited data availability
* Class imbalance between normal and disease samples
* Privacy restrictions in healthcare data

Generative models such as **Generative Adversarial Networks (GANs)** provide an effective solution by creating realistic synthetic images.

This project uses **Auxiliary Classifier GAN (ACGAN)** to generate labeled chest X-ray images, allowing better dataset augmentation for pneumonia detection models.

---

# Key Features

• Synthetic chest X-ray image generation
• Class-conditioned image generation (Normal / Pneumonia)
• Dataset augmentation for medical imaging
• Improved training data balance
• Deep learning–based generative modeling

---

# Dataset

The model was trained on a **Chest X-ray dataset containing Normal and Pneumonia images**.

### Classes

* Normal
* Pneumonia

The dataset was used to train the **ACGAN generator and discriminator networks** to learn realistic patterns from chest radiographs.

---

# What is ACGAN?

**Auxiliary Classifier Generative Adversarial Network (ACGAN)** is an extension of GAN that generates images **conditioned on class labels**.

Unlike traditional GANs, ACGAN includes a **class prediction mechanism in the discriminator**.

### Components

1. **Generator**

   * Generates synthetic chest X-ray images from random noise and class labels.

2. **Discriminator**

   * Determines whether the image is real or fake.
   * Predicts the class label of the image.

This allows the model to generate **class-specific synthetic medical images**.

---

# Model Architecture

The ACGAN model consists of two neural networks:

### Generator

The generator takes two inputs:

* Random noise vector
* Class label (Normal / Pneumonia)

It produces synthetic chest X-ray images.

### Discriminator

The discriminator performs two tasks:

1. Real vs Fake image classification
2. Disease class prediction

This dual objective helps improve the quality and control of generated images.

---

# Workflow

1. Load chest X-ray dataset.
2. Train the ACGAN generator and discriminator networks.
3. The generator creates synthetic chest X-ray images.
4. The discriminator evaluates image authenticity and class label.
5. Generated images are saved and used for **dataset augmentation**.

---

# Results

The trained ACGAN model successfully generated **high-quality synthetic chest X-ray images** belonging to:

* Normal class
* Pneumonia class

These synthetic images help:

* Increase dataset size
* Improve model generalization
* Reduce class imbalance

---

# Applications

• Medical dataset augmentation
• Pneumonia detection research
• Training deep learning models with limited data
• Healthcare AI development

---

# Technologies Used

• Python
• PyTorch / TensorFlow
• GAN Architecture
• ACGAN
• NumPy
• OpenCV

---

# Future Improvements

• Generate higher resolution medical images
• Train models on larger chest X-ray datasets
• Integrate synthetic data into pneumonia classification models
• Explore advanced GAN architectures (StyleGAN, Diffusion Models)

---

# Author

**Tharun Kumar**

