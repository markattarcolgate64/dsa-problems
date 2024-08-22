from container import Container

def main():

    cont = Container()

    cont.add(2)
    cont.add(5)
    cont.add(8)
    cont.add(2)
    cont.add(9)
    cont.add(14)
    cont.add(3)
    
    print(cont.get_median())

    cont.add(6)
    cont.add(10)
    cont.add(5)
    print(cont.get_median())


if __name__ == "__main__":
    main()

    

    

