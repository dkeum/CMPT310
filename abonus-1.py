# abonus.py

# template for Bonus Assignment, Artificial Intelligence Survey, CMPT 310 D200
# Spring 2021, Simon Fraser University

# author: Jens Classen (jclassen@sfu.ca)

from learning import *

def generate_restaurant_dataset(size=100):
    """
    Generate a data set for the restaurant scenario, using a numerical
    representation that can be used for neural networks. Examples will
    be newly created at random from the "real" restaurant decision
    tree.
    :param size: number of examples to be included
    """

    numeric_examples = None
    
    ### YOUR CODE HERE ###
    Restaurant_dataset = SyntheticRestaurant(size);
    #print(len(Restaurant_dataset.examples))
    #print(Restaurant_dataset.examples[0])
    #print(Restaurant_dataset.examples[0][1])
   
    for i in range(len(Restaurant_dataset.examples)):
        # append 3 values for distributed encoding
        Restaurant_dataset.examples[i].append('encoding1')
        Restaurant_dataset.examples[i].append('encoding2')
        Restaurant_dataset.examples[i].append('encoding3')
        
        #ALT 
        if(Restaurant_dataset.examples[i][0] == 'No'):
            Restaurant_dataset.examples[i][0]= 0
        if(Restaurant_dataset.examples[i][0] == 'Yes'):
            Restaurant_dataset.examples[i][0]= 1
        #BAR
        if(Restaurant_dataset.examples[i][1] == 'No'):
            Restaurant_dataset.examples[i][1]= 0
        if(Restaurant_dataset.examples[i][1] == 'Yes'):
            Restaurant_dataset.examples[i][1]= 1
        #FRI
        if(Restaurant_dataset.examples[i][2] == 'No'):
            Restaurant_dataset.examples[i][2]= 0
        if(Restaurant_dataset.examples[i][2] == 'Yes'):
            Restaurant_dataset.examples[i][2]= 1
        #Hun    
        if(Restaurant_dataset.examples[i][3] == 'No'):
            Restaurant_dataset.examples[i][3]= 0
        if(Restaurant_dataset.examples[i][3] == 'Yes'):
            Restaurant_dataset.examples[i][3]= 1
        
        #Pat
        if(Restaurant_dataset.examples[i][4] == 'Full'):
            Restaurant_dataset.examples[i][4]= 2
        if(Restaurant_dataset.examples[i][4] == 'Some'):
            Restaurant_dataset.examples[i][4]= 1
        if(Restaurant_dataset.examples[i][4] == 'None'):
            Restaurant_dataset.examples[i][4]= 0
        
        #Price
        if(Restaurant_dataset.examples[i][5] == '$$$'):
            Restaurant_dataset.examples[i][5]= 2
        if(Restaurant_dataset.examples[i][5] == '$$'):
            Restaurant_dataset.examples[i][5]= 1
        if(Restaurant_dataset.examples[i][5] == '$'):
            Restaurant_dataset.examples[i][5]= 0
        
        #Rain
        if(Restaurant_dataset.examples[i][6] == 'No'):
            Restaurant_dataset.examples[i][6]= 0
        if(Restaurant_dataset.examples[i][6] == 'Yes'):
            Restaurant_dataset.examples[i][6]= 1
        
        #Res
        if(Restaurant_dataset.examples[i][7] == 'No'):
            Restaurant_dataset.examples[i][7]= 0
        if(Restaurant_dataset.examples[i][7] == 'Yes'):
            Restaurant_dataset.examples[i][7]= 1
        
        
        #Est
        if(Restaurant_dataset.examples[i][9] == '0-10'):
            Restaurant_dataset.examples[i][12]= 0
        if(Restaurant_dataset.examples[i][9] == '10-30'):
            Restaurant_dataset.examples[i][12]= 1
        if(Restaurant_dataset.examples[i][9] == '30-60'):
            Restaurant_dataset.examples[i][12]= 2
        if(Restaurant_dataset.examples[i][9] == '>60'):
            Restaurant_dataset.examples[i][12]= 3
            
        #WillWait
        if(Restaurant_dataset.examples[i][10] == 'No'):
            Restaurant_dataset.examples[i][13]= 0
        if(Restaurant_dataset.examples[i][10] == 'Yes'):
            Restaurant_dataset.examples[i][13]= 1
  
       
        
        #Type
        if(Restaurant_dataset.examples[i][8] == 'Thai'):
            Restaurant_dataset.examples[i][8]= 0
            Restaurant_dataset.examples[i][9]= 0
            Restaurant_dataset.examples[i][10]= 0
            Restaurant_dataset.examples[i][11]= 1
            
        if(Restaurant_dataset.examples[i][8] == 'French'):
            Restaurant_dataset.examples[i][8]= 0
            Restaurant_dataset.examples[i][9]= 1
            Restaurant_dataset.examples[i][10]= 0
            Restaurant_dataset.examples[i][11]= 0
        
        if(Restaurant_dataset.examples[i][8] == 'Burger'):
            Restaurant_dataset.examples[i][8]= 1
            Restaurant_dataset.examples[i][9]= 0
            Restaurant_dataset.examples[i][10]= 0
            Restaurant_dataset.examples[i][11]= 0
     
        if(Restaurant_dataset.examples[i][8] == 'Italian'):
            Restaurant_dataset.examples[i][8]= 0
            Restaurant_dataset.examples[i][9]= 0
            Restaurant_dataset.examples[i][10]= 1
            Restaurant_dataset.examples[i][11]= 0
        
        
    #print(Restaurant_dataset.examples[0])
    numeric_examples = Restaurant_dataset.examples 

    return DataSet(name='restaurant_numeric',
                   target='Wait',
                   examples=numeric_examples,
                   attr_names='Alternate Bar Fri/Sat Hungry Patrons Price Raining Reservation Burger French Italian Thai WaitEstimate Wait')

def nn_cross_validation(dataset, hidden_units, epochs=100, k=10):
    """
    Perform k-fold cross-validation. In each round, train a
    feed-forward neural network with one hidden layer. Returns the
    error ratio averaged over all rounds.
    :param dataset:      the data set to be used
    :param hidden_units: the number of hidden units (one layer) of the neural nets to be created
    :param epochs:       the maximal number of epochs to be performed in a single round of training
    :param k:            k-parameter for cross-validation 
                         (do k many rounds, use a different 1/k of data for testing in each round) 
    """
   
    
    error = 0

    ### YOUR CODE HERE ###
    
    k_subset = len(dataset.examples)
    step = k_subset/k
#    print("this is step value: " + str(step))
#    print("this is k_subset value: " + str(k_subset))
    
    hidden_unitss = [0];
    hidden_unitss[0] = hidden_units
    
    
    examples = dataset.examples
    
    for i in range(k):
        start_index = (step*i)
        end_index = (i+1)*step
        #print(str(start_index) + " also " + str(end_index))
        train,val = train_test_split(dataset, start=start_index, end=end_index, test_split=(1/k))
        dataset.examples = train
        predict = NeuralNetLearner(dataset, hidden_layer_sizes= hidden_unitss, learning_rate=0.01, epochs=epochs, activation=sigmoid)  
        error += err_ratio(predict, dataset, examples=val)
        dataset.examples = examples    
    
    return error/k






############## TESTING BELOW ####################



N          = 300   # number of examples to be used in experiments
k          =  10   # k parameter
epochs     = 100   # maximal number of epochs to be used in each training round
size_limit =  7  # maximal number of hidden units to be considered

# generate a new, random data set
# use the same data set for all following experiments
dataset = generate_restaurant_dataset(N)

# try out possible numbers of hidden units
for hidden_units in range(1,size_limit+1):
    
    # print("LEN " + str(len(dataset.examples)))
    # do cross-validation
    error = nn_cross_validation(dataset=dataset,
                                hidden_units=hidden_units,
                                epochs=epochs,
                                k=k)
    # report size and error ratio
    print("Size " + str(hidden_units) + ":", error)
