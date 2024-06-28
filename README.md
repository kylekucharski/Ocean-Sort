# Ocean Sort

Ocean Sort is an innovative sorting algorithm designed to help people understand the fundamental concepts of data structures. Inspired by the natural sorting action of ocean waves, Ocean Sort provides a unique approach to sorting an array, emphasizing visualization and educational value over computational efficiency.

## Table of Contents

- [Introduction](#introduction)
- [Algorithm Description](#algorithm-description)
- [Features](#features)
- [Usage](#usage)
- [Visualization](#visualization)
- [Installation](#installation)


## Introduction

Ocean Sort is a visually engaging sorting algorithm that mimics the behavior of ocean waves sorting sand on the shoreline. The algorithm consists of two main phases: the forward wave-motion phase and the backward retreat phase. Through these phases, elements in the array are gradually sorted, providing an intuitive understanding of sorting processes.

## Algorithm Description

Ocean Sort works by iteratively performing two main operations:

1. **Forward Wave-Motion Phase**: The algorithm moves from the midpoint of the array to the edges, swapping elements that are out of order.
2. **Backward Retreat Phase**: The algorithm moves back from the edges to the midpoint, swapping elements that are out of order.

The range of these waves decreases over time, similar to how waves recede on a shoreline, until the entire array is sorted.

## Features

- Unique wave-inspired sorting algorithm
- Educational visualization of the sorting process
- Animated output for better understanding of sorting mechanics

## Usage

To use the Ocean Sort algorithm, you can run the provided Python script. The script generates a random array of integers, sorts it using Ocean Sort, and saves an animation of the sorting process.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def ocean_sort(arr):
    n = len(arr)
    mid = n // 2
    wave_range = n // 2

    sorted = False
    frames = []

    while not sorted:
        sorted = True

        # Forward wave-motion phase
        for i in range(mid - wave_range, mid + wave_range):
            if i + 1 < n and arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
                frames.append((arr.copy(), 'Forward Phase'))

        # Backward retreat phase
        for i in range(mid + wave_range, mid - wave_range, -1):
            if i < n and i - 1 >= 0 and arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                sorted = False
                frames.append((arr.copy(), 'Backward Phase'))

        wave_range -= 1
        if wave_range == 0:
            break

    return arr, frames

def visualize_frame(frame):
    arr, phase = frame
    plt.clf()
    plt.bar(range(len(arr)), arr, color='blue')
    plt.title(f'Ocean Sort - {phase}')
    plt.xlabel('Index')
    plt.ylabel('Value')

if __name__ == "__main__":
    array = np.random.randint(1, 100, 30)

    print("Unsorted array:")
    print(array)

    sorted_array, frames = ocean_sort(array)

    fig = plt.figure()
    ani = animation.FuncAnimation(fig, visualize_frame, frames=frames, interval=200, repeat=False)
    ani.save('ocean_sort_animation.mp4', writer='ffmpeg', dpi=300)

    print("Sorted array:")
    print(sorted_array)


## Visualization

The `ocean_sort` function not only sorts the array but also captures each step of the sorting process. The `visualize_frame` function uses Matplotlib to create an animation, helping users visualize how the algorithm works.

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/ocean_sort.git
    cd ocean_sort
    ```

2. **Install the required packages**:

    ```sh
    pip install matplotlib numpy
    ```

3. **Run the script**:

    ```sh
    python ocean_sort.py
    ```


