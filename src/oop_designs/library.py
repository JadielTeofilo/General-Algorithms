"""

Design A library Management System



Library has only books

people can checkout the books and checkin books

people can stay with the book for 1 week

search a book


Library 
    - books
    - users


    + search 
    + checkout 
    + checkin
    + add_book
    + update_book

Borrow
    - book_item

User
    - borrows

Book
    - book_items

BookItem



"""
import dataclass
from typing import Iterator, Dict
import uuid


@dataclasses.dataclass
class Book:
    name: str
    year: int
    _borrowed_copies: List[BookCopy]
    _available_copies: List[BookCopy] 
    uid: str = uuid.uuid4().hex

    def get_available_copy(self) -> Optional[BookCopy]:
        if not self._available_copies:
            return
        self._borrowed_copies.append(
                self._available_copies.pop()
        )
        return self._borrowed_copies[-1]
        

@dataclasses.dataclass
class BookCopy:
    book: Book
    uid: str = uuid.uuid4().hex


@dataclasses.dataclass
class Borrow:
    book_copy: BookCopy
    _created_at: datetime.datetime = datetime.datetime.now()
    uid: str = uuid.uuid4().hex


class User:
    uid: str = uuid.uuid4().hex
    borrows: Dict[str, Borrow] = dict()


class Library:
    def __init__(self) -> None:
        self._books: Dict[str, Book] = dict()
        self._users: Dict[str, User] = dict()
        self._borrows: Dict[str, Borrow] = dict()

    def search(self, text: str) -> Iterator[Book]:
        for book in self._books:
            if re.search(text.lower(), book.name.lower()):
                yield book

    def checkout(self, book: Book, user: User) -> Borrow:
        book_copy: Optional[BookCopy] = book.get_available_copy()
        if not book_copy:
            raise ValueError('No Copy Available')
        new_borrow: Borrow = Borrow(book_copy)
        user.borrows.append(new_borrow)
        self._borrows[new_borrow.uid] = new_borrow

    def checkin(self, borrow: Borrow, user: User) -> bool:
        self._borrows.pop(borrow.uid)
        user.remove_borrow(borrow)  #TODO
        borrow.free_book() # TODO









