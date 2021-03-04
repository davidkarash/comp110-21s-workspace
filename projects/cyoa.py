"""A totally radical surfing adventure dude!!!!"""

adventure_points: int
name: str

def greet() -> None:
    print("Hey bro!! Check out the waves out there man!")
    print("Definitely gonna be a crazy day out there!")
    print("I'm Tank Evans... I basically run this place!")
    print("I don't think I've seen ya around here before.")
    print("What's your name bro??")
    global name
    name = input("Enter your name: ")
    print("Nice to meet ya, " + name + "!")
    print("Steer clear of my waves bro, but hang ten!!")


def main() -> None:
    greet()
    print(name)
    print("""

    """)
    print("""    Standing with the old wooden surfboard you found in the back of your 
    family's garage, you take in the environment around you.  You feel the warm sun 
    on your back, and the sound of rolling waves rush towards the shore. People everywhere 
    laughing and joking, while some of the greatest surfers in the world ride waves that 
    tower 5 foot above their heads. 

    To your left, you see a surf shop. To the right, you see a circle of people talking. 
    You turn towards the water, and see the huge waves. 
    Where do you want to go?

    """)
    current_choice: int = int(input("Type 1 to go the surf shop, 2 to join the people talking, or 3 to head into the water. "))
    adventure_points = 0
    
    return None

if __name__ == "__main__":
    main()