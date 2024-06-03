import numpy as np


def create_new_labels(model, train_images, train_labels, test_labels):
    """
    Calculate the mean outputs for each digit and create new labels for the training and test images.

    Parameters:
    model (tf.keras.Model): The trained model used for predictions.
    train_images (np.ndarray): Array of training images.
    train_labels (np.ndarray): Array of training labels.
    test_labels (np.ndarray): Array of test labels.

    Returns:
    np.ndarray: New training labels based on mean outputs.
    np.ndarray: New test labels based on mean outputs.
    """
    # Determine the unique labels
    unique_labels = np.unique(train_labels)

    # Initialize an array to hold the mean outputs for each label
    mean_outputs_per_label = []

    # Loop over each unique label
    for label in unique_labels:
        # Filter out the images corresponding to the current label
        label_images = train_images[train_labels == label]

        # Predict the outputs for the current label images
        label_outputs = model.predict(label_images)

        # Calculate the mean of each index across all output arrays for the current label
        mean_label_output = np.mean(label_outputs, axis=0)

        # Append the mean output to the array
        mean_outputs_per_label.append(mean_label_output)

    # Convert the list to a NumPy array for better handling (optional)
    mean_outputs_per_label = np.array(mean_outputs_per_label)

    # Create new labels for the training images based on mean outputs
    new_train_labels = np.array([mean_outputs_per_label[label] for label in train_labels])
    new_test_labels = np.array([mean_outputs_per_label[label] for label in test_labels])

    return new_train_labels, new_test_labels
