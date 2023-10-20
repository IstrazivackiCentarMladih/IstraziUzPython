import random, string
import matplotlib.pyplot as plt
import time 

def generate_strings(file_name, num_strings, length):
    s = []
    for _i in range(num_strings):
        s.append(''.join(random.choice(string.ascii_lowercase) for _j in range(length)))

    with open(file_name, 'w') as f:
        for i in s:
            f.write(i + '\n')

def read_strings(file_name):
    with open(file_name, 'r') as f:
        return f.read().splitlines()

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2)) / len(s1)

def calculate_distances(strings):
    distances = []
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            distances.append(hamming_distance(strings[i], strings[j]))
    return distances

def plot_histogram(data, num_bins):
    plt.hist(data, num_bins, facecolor='blue')
    plt.title("Hamming Distance Histogram")
    plt.xlabel('Hamming Distance')
    plt.ylabel('Frequency')
    plt.show()

def main():
    start_time = time.time()
    generate_strings('strings.txt', 1000, 10)
    strings = read_strings('strings.txt')
    distances = calculate_distances(strings)
    end_time = time.time()
    print("Time taken: ", end_time - start_time)

    plot_histogram(distances, 100)
    


if __name__ == '__main__': 
    main()