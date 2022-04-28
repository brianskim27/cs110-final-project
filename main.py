import src.controller

def main():
    team = {"lead": "Brian Kim", "backend": "Andy Luna", "frontend": "Sung Chan Kang"}
    
    print("Software Lead is:", team["lead"])
    print("Backend is:", team["backend"])
    print("Frontend is:" , team["frontend"])

    game = src.controller.Controller()
    game.mainLoop()

main()