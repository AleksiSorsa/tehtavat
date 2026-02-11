kuha = int(input("Kuinka pitkä kikkelisi on?: "))
if kuha <37:
    puute = (37-kuha)
    print("Kikkelisi on ",puute,"cm liian pieni")
    print("lakse kuha takaisin ääliö!")
elif kuha >37:
    print("pidä kuhasi ja tee hyvää ruokaa.")