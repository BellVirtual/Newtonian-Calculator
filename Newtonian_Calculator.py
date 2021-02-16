print("Hello I can calculate \n 1.Force given the mass and accleration. \n 2. Acceleration given the force and the mass \n 3. Mass given the force and accleration")
p = input("Please enter the number that correlates to your problem: ")
if p == "1":
    m = input("Give Mass: ")
    a = input("Give Acceleration: ")
    result = ( float(a) * float(m) )
    print(result)
if p == "2":
    f = input("Give Force: ")
    m = input("Give Mass: ")
    result = ( float(f) / float(m) )
    print(result)
if p == "3":
    f = input("Give Force: ")
    m = input("Give Acceleration: ")
    result = ( float(f) / float(m) )
    print(result)
