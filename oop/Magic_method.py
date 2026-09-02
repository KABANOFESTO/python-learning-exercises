class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.num_pages}"

    def __eq__(self, other):
        if isinstance(other, Book):
            return (
                self.title == other.title
                and self.author == other.author
                and self.num_pages == other.num_pages
            )
        return False

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.num_pages < other.num_pages
        return NotImplemented


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("1984", "George Orwell", 328)

print(
    book1
)  # Returns "Title: The Great Gatsby, Author: F. Scott Fitzgerald, Pages: 180"
print(book1 == book2)  # Returns False
