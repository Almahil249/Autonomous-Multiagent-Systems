import heapq

def parse_dataset(filename):
    runs = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('Run'):
                parts = line.split()
                run_id = int(parts[1][:-1])
                time = float(parts[3])
                iterations = int(parts[5])
                distance = float(parts[7])
                runs.append((run_id, distance, time, iterations))
    return runs    

def find_best_run(runs, weight_distance=1.8, weight_time=0.85, weight_iterations=0.80):
    pq = []
    for run in runs:
        run_id, distance, time, iterations = run
        cost = (weight_distance * distance) + (weight_time * time) + (weight_iterations * iterations)
        heapq.heappush(pq, (cost, run))
    
    best_run = heapq.heappop(pq)
    return best_run , best_run[1][0]


def get_best_run_details(id):
    file = open("path.txt", "r")
    lines = file.readlines()
    file.close()
    points = []
    currnt_run = 0
    for line in lines:
        if "!!Run" in line:
            currnt_run += 1
        elif "!T:" in line:
            if currnt_run == id:
                break
        else:
            if currnt_run == id:
                points.append(line)
    #save the best run details to a file
    file = open("shortest_path.txt.txt", "w")
    for run in points:
        for point in run:
            file.write(point)





# Main function
def main():
    filename = 'ExplorSummary.txt'
    runs = parse_dataset(filename)
    best_run, best_run_id = find_best_run(runs)
    print("Best run:", best_run_id)
    get_best_run_details(best_run_id)

    print("Best run:", best_run)

# Run the main function
if __name__ == "__main__":
    main()
