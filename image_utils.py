from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    clean_image - suppress_noise(image_array)
    edges = detect_edges(clean_image)
    binary_edges = convert_to_binary(edges, threshold=50)
    save_binary_image(binary_edges, 'my_edges.png')

def edge_detection(image):
    edges = edge_detection(clean_image)
    return edges
