import random
import datetime

def generate_parent(length):
    return random.sample(range(0,length),length)

def get_fitness(genes):
    # Optimal value will be zero
    fitness=0
    length = len(genes)
    for ridx1 in range(0,length-1):
        for ridx2 in range(ridx1+1,length):
            # Checks for diagonal conflict
            # Left diagonal in 2D matrix will increase or decrease in multiples of 11
            # (1,1),(2,2) --> 22 - 11 = 11 -- Diagonal conflict
            # Right diagonal in 2D matrix will increase or decrease in multiples of 9
            # (2,2),(3,1) --> 31 - 22 = 9 -- Diagonal conflict
            diff2 = abs(((ridx1+1)*10+genes[ridx1])-((ridx2+1)*10+genes[ridx2]))
            diff1 = abs(genes[ridx1]-genes[ridx2])

            fitness+= 1 if diff2 == diff1 * 9 or diff2 == diff1 * 11 else 0
    return(fitness)

def crossover(parent1, parent2):
        length = len(parent1)
        crossover_index = random.randrange(0,length)
        child = parent1[0:crossover_index]
        child.extend(parent2[crossover_index:length])
        ## Remove horizontal conflict created by crossover
        ## Inputs (Parent1, Parent2) : [6, 7, 1, 3, 5, 4, 0, 2], [0, 7, 2, 3, 6, 1, 4, 5]
        ## Output from crossover     : [6, 7, 1, 3, 6, 1, 4, 5]
        ## Output from below logic   : [6, 7, 1, 3, 2, 0, 4, 5]
        l=list(range(0,length))
        z=[]
        for x in child:
            if x in l:
                z.append(1)
                l.remove(x)
            else:
                z.append(0)
        for i in range(0,length):
              if z[i] == 0:
                child[i]= l.pop()
        return child
                
def mutate(parent):
    child = parent    
    Gene1, Gene2 = random.sample(range(0,len(child)),2)
    child[Gene1],child[Gene2] = child[Gene2],child[Gene1]
    return child

def find_sequence(optimalFitness, length):
    parent1 = generate_parent(length)
    parent1Fitness = get_fitness(parent1)
    parent2 = generate_parent(length)
    parent2Fitness = get_fitness(parent2)
    #print(parent1,parent1Fitness,parent2,parent2Fitness)

    while True:
        child = crossover(parent1, parent2)
        child = mutate(child)
        childFitness = get_fitness(child)
        if parent1Fitness < childFitness:
            if parent2Fitness < childFitness:
                continue
            else:
                parent2Fitness = childFitness
                parent2 = child
        else:
            parent1Fitness = childFitness
            parent1 = child
        #print('p',parent1,parent1Fitness,parent2,parent2Fitness)
        if parent1Fitness == optimalFitness:
            print(' '.join(map(str,parent1)))
            return parent1Fitness
        if parent2Fitness == optimalFitness:
            print(' '.join(map(str,parent2)))
            return parent2Fitness
            
if __name__ == '__main__':
    startTime=datetime.datetime.now()
    optimalFitness = 0
    length = 8
    find_sequence(optimalFitness, length)
    #print('Time taken : ' + str(datetime.datetime.now() - startTime))