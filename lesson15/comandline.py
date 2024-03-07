
def hellow(name, lang):
    greetings = {
        "English":"Hellow",
        "Spanish":"Hola",
        "German":"Hallo",
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)

if __name__ == "__main__":


    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal argument"
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True, help= "The name of the person to greet"
    )

    parser.add_argument(
        "-l","--lang",metavar="lenguage",
        required=True, choices=["English","Spanish","German"],
        help="The lenguage of the greeting."
    )

    args = parser.parse_args()

    hellow(args.name, args.lang)

    
