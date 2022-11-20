from paramiko import Agent


def hello():
    print("Hello Adalab")

def hello(name):
    print(f"Hello {name}")

def hello(name,age):
    year=2022-age
    print(f"hello {name} you were born in {year}")

def hello2(name):
    print(f"hello {name}")
    return
    print("Welcome to Adalab")

def hello3(name):
    return f"Hello {name}"

def my_country(name,country="Uganda"):
    return f"Hello{name} from {country}"
    

def  hello_multi(*names):
       for name in names:
           print(f"hello {name}")


def greet(name,age):
    year=2022-age
    print(f"Hello {name} you were born in {year}")


def greet_multiple(**kwargs):
    keys=kwargs.keys()
    if "names" in keys:
        print("hello{kwargs['name']}")

    elif "country" in keys:
          print("hello from{kwargs['country']}")

    else: print("hello anonymous")

def sum_end_greet(*args,**kwargs):
        print(args) 
        print(kwargs)


        
        

               
           
            

        
    
