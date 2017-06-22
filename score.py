# initialize the scoring logic by loading the model
def init():
    global model
    print("Loading the model")
    # TO DO: load model

# score a row of data
def run(inputString):
    import json
    try:
        input_list = json.loads(inputString)
    except ValueError:
        return "Bad input: expecting a JSON encoded list of lists."

    # TO DO: score model    
    print("Score the model")
    return 42

# test scoring script
if __name__ == '__main__':
    import json
    init()
    score = run(json.dump([[1,2,3,4,5,"data"]]))
    print(score)