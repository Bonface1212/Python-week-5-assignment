# Parent Class
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def read(self):
        print(f"Reading '{self.title}' by {self.author}...")

    def get_description(self):
        return f"'{self.title}' is a {self.genre} book written by {self.author}."

# Child Class (Inheritance)
class AudioBook(Book):
    def __init__(self, title, author, genre, narrator):
        super().__init__(title, author, genre)
        self.narrator = narrator

    def listen(self):
        print(f"Listening to '{self.title}' narrated by {self.narrator}.")

    # Example of polymorphism
    def read(self):
        print(f"Playing the audiobook '{self.title}' narrated by {self.narrator}...")

# Example usage
normal_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
audio_book = AudioBook("Becoming", "Michelle Obama", "Memoir", "Michelle Obama")

normal_book.read()
print(normal_book.get_description())

audio_book.read()
audio_book.listen()
print(audio_book.get_description())
