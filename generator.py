import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Load the generator model
generator = tf.keras.models.load_model('generator.h5')

# Function to generate and display images
def generate_images(generator, input_dim, num_images, labels=None):
    # Generate random noise
    random_noise = np.random.normal(0, 1, (num_images, input_dim))
    
    # If the generator is conditional, concatenate the noise with the labels
    if labels is not None:
        random_noise = np.concatenate([random_noise, labels], axis=1)
    
    # Generate images
    generated_images = generator.predict(random_noise)
    
    # Plot the generated images
    for i in range(num_images):
        plt.subplot(1, num_images, i + 1)
        plt.imshow((generated_images[i] * 127.5 + 127.5).astype(np.uint8))
        plt.axis('off')
    plt.show()

# Example usage:
input_dim = 100  # Assuming the generator takes a 100-dimensional noise vector
num_images = 5  # Number of images to generate
generate_images(generator, input_dim, num_images)
