RS = int(input("Enter Number of red T Shirts: "))
BS = int(input("Enter Number of Blue T Shirts: "))
WS = int(input("Enter Number of White T Shirts: "))

total = RS+BS+WS

prob_a = BS/total
prob_b = RS/total

prob_bga = prob_b
prob_a_and_b = prob_a*prob_b

print("Probability that the second T shirt is red given that the first shirt is blue: ")
print(round((prob_bga),3))


print("Probability that the second T shirt is red and first shirt is blue: ")
print(round((prob_a_and_b),3))