#read ExplorSummary.txt
#and get the run with the least time and the least iterations 

def get_best_run():
    with open('ExplorSummary.txt') as f:
        lines = f.readlines()
    best_time = 1000
    best_iter = 10000000
    best_run = 0
    for i in range(len(lines)):
        line = lines[i]
        time = float(line.split()[3])
        iter = int(line.split()[5])
        if time < best_time:
            best_time = time
            best_iter = iter
            best_run = i
        elif time == best_time:
            if iter < best_iter:
                best_time = time
                best_iter = iter
                best_run = i
    return best_run, best_time, best_iter

best_run, best_time, best_iter = get_best_run()
print(f"Best run: {best_run + 1} Time: {best_time} Iterations: {best_iter}")



