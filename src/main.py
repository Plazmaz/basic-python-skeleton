import click
import logging


logging.basicConfig(format='%(asctime)s %(message)s')
logging.getLogger().setLevel(logging.INFO)

@click.command()
def main_command():
    pass

if __name__ == '__main__':
    main_command()
