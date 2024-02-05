from PySide6 import QtWidgets, QtGui, QtCore
from movie import get_movies
from movie import Movie
class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cine Club")
        self.setup_ui()
        self.populate_movies()
        
        self.setup_connections()

        self.resize(400, 500)

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.title = QtWidgets.QLineEdit()
        self.btn_add_movie = QtWidgets.QPushButton("Ajouter un film")
        self.movie_List = QtWidgets.QListWidget()
        self.btn_remove_movies = QtWidgets.QPushButton("Supprimer le(s) film(s)")
    
       
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_add_movie)
        self.layout.addWidget(self.movie_List)
        self.layout.addWidget(self.btn_remove_movies)

    def setup_connections(self):
        self.title.returnPressed.connect(self.add_movie)
        self.btn_add_movie.clicked.connect(self.add_movie)
        self.btn_remove_movies.clicked.connect(self.remove_movie)
        

            
    def populate_movies(self):
        movies = get_movies()

        for movie in movies: 
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.movie_List.addItem(lw_item)

    def add_movie(self):
        movie_title = self.title.text()
        if not movie_title:
            return False
        movie = Movie(title=movie_title)
        resultat = movie.add_to_movies()
        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.movie_List.addItem(lw_item)

        self.title.setText("")

    def remove_movie(self):
        for selected_item in self.movie_List.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.movie_List.takeItem(self.movie_List.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()