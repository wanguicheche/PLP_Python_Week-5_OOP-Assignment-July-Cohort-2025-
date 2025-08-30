# Create a Book class to represent general book attributes.
class Book:
    # The constructor method (__init__) initializes the object with specific values.
    # 'self' refers to the instance of the object itself.
    def __init__(self, title, author, genre, page_count):
        self.title = title
        self.author = author
        self.genre = genre
        self.page_count = page_count

    # A method to display the book's details.
    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Page Count: {self.page_count}")

# SheReadsTruthBook inherits from the Book class, gaining all its attributes and methods.
# This demonstrates inheritance.
class SheReadsTruthBook(Book):
    # The constructor for the child class calls the parent's constructor using 'super()'.
    def __init__(self, title, author, genre, page_count, format_type, is_bible_study):
        super().__init__(title, author, genre, page_count)
        self.format_type = format_type  # e.g., "Paperback," "Hardcover"
        self.is_bible_study = is_bible_study  # Boolean value (True or False)

    # A method unique to the SheReadsTruthBook class.
    def describe_study(self):
        if self.is_bible_study:
            print(f"This is a Bible study book in {self.format_type} format.")
        else:
            print(f"This is a general Christian book in {self.format_type} format.")
    
# Create an instance of the SheReadsTruthBook class for "God's Presence."
# Provide unique values for each attribute.
gods_presence = SheReadsTruthBook(
    title="God's Presence",
    author="She Reads Truth",
    genre="Christian/Bible Study",
    page_count=208,
    format_type="Hardcover",
    is_bible_study=True
)

# Call the methods to see the class in action.
print("--- My Favorite Book ---")
gods_presence.display_details()
gods_presence.describe_study()