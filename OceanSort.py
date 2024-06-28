
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def ocean_sort(arr):
    n = len(arr)  # Get the length of the array
    mid = n // 2  # Calculate the midpoint of the array
    wave_range = n // 2  # Initialize the range of the wave to half of the array length

    sorted = False  # Flag to track if the array is sorted
    frames = []  # List to store frames for the animation

    while not sorted:  # Continue until the array is sorted
        sorted = True  # Assume the array is sorted, will set to False if we make a swap

        # Forward wave-motion phase
        for i in range(mid - wave_range, mid + wave_range):
            if i + 1 < n and arr[i] > arr[i + 1]:               # If the current element is greater than the next element
                arr[i], arr[i + 1] = arr[i + 1], arr[i]         # Swap the elements
                sorted = False                                  # Set sorted to False since we made a swap
                frames.append((arr.copy(), 'Forward Phase'))    # Store the current state of the array

        # Backward retreat phase
        for i in range(mid + wave_range, mid - wave_range, -1):
            if i < n and i - 1 >= 0 and arr[i] < arr[i - 1]:    # If the current element is less than the previous element
                arr[i], arr[i - 1] = arr[i - 1], arr[i]         # Swap the elements
                sorted = False                                  # Set sorted to False since we made a swap
                frames.append((arr.copy(), 'Backward Phase'))   # Store the current state of the array

        wave_range -= 1      # Reduce the range of the wave
        if wave_range == 0:  # If the wave range is 0, break the loop
            break

    return arr, frames  # Return the sorted array and the frames

def visualize_frame(frame):
    arr, phase = frame                           # Unpack the frame
    plt.clf()                                    # Clear the current figure
    plt.bar(range(len(arr)), arr, color='blue')  # Create a bar chart with the current state of the array
    plt.title(f'Ocean Sort - {phase}')           # Set the title of the chart
    plt.xlabel('Index')                          # Label the x-axis
    plt.ylabel('Value')                          # Label the y-axis

if __name__ == "__main__":
    # Generate a random array of integers between 1 and 100 with 30 elements
    array = np.random.randint(1, 100, 30)

    print("Unsorted array:")
    print(array)

    sorted_array, frames = ocean_sort(array)  # Sort the array and get the frames for animation

    fig = plt.figure()  # Create a new figure
    ani = animation.FuncAnimation(fig, visualize_frame, frames=frames, interval=200, repeat=False)  # Create the animation

    # Save the animation
    ani.save('ocean_sort_animation.mp4', writer='ffmpeg', dpi=300)  

    print("Sorted array:")
    print(sorted_array)
