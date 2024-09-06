'''
Purpose: A digit classifier made in Python using a neural network.

Owen Colley
9/3/24
'''

def main():
  inputs = [1, 2, 3, 2.5]
  weights = [0.2, 0.8, -0.5, 1.0]
  bias = 2.0
  
  output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] + bias
  print(output)

if __name__ == "__main__":
  main()