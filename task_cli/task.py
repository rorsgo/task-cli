import typer
import utils.tools as tools

a = {
    'paullo': 16,
    'Rodrigo': 21,
}

def main():
    b = {}
    key = tools.extract_keys_and_values(a)
    print(key)


if __name__ == "__main__":
    typer.run(main)
