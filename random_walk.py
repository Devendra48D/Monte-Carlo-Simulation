import random

def random_walk(n):
    """Return coordinates after 'n' block random walk"""
    x, y = 0, 0
    for _ in range(n):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x, y = x + dx, y + dy
    return (x, y)


number_of_walks = 20000

for walk_length in range(1, 61):
    no_transport = 0 #number of walks less than 6 blocks 
    number_of_lyft_rides = 0
    for i in range(number_of_walks):
        x, y = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance < 6:
            no_transport += 1
        else:
            number_of_lyft_rides += 1
    no_transport_percentage = 100 * (float(no_transport)/number_of_walks)
    print "Walk size = ", walk_length, ", % of no transport = ", no_transport_percentage, 
    print ", Total cost of Lyft rides", 10*number_of_lyft_rides,
    print ", Cost to blocks ratio", 10 * number_of_lyft_rides / float(walk_length)
    
