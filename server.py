from src import app

from src.routes.Leitores.leitores import *
from src.routes.Livros.livros import *

if __name__ == '__main__':
    app.run(
        debug=True,
        port=1111
    )