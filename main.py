def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

operations = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide,             
}
def calculator():
  n1 = float(input("Enter the number: "))
  
  for op in operations:
    print(op)
  
  decision_flag = True
  
  while decision_flag:
    operation_symbol = input("Pick an operation: ")
    n2 = float(input("Enter the next number: "))
  
    calculate_fuction = operations[operation_symbol]
    answer = calculate_fuction(n1, n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")
    
    decision = input(f"Type 'y' to continue with {answer} or type 'n' to start again: ")
    if decision == 'y':
      n1 = answer
     
    elif decision == 'n':
      decision_flag = False
      calculator()
      
calculator()