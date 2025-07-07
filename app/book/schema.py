from typing import List
from pydantic import BaseModel, Field, validator

class BaseBook(BaseModel):
    """Base book model with core fields and list manipulation functionality"""
    
    isbn: str = Field(max_length=30)
    title: str = Field(max_length=100)
    genre: List[str] = Field(min_items=1)
    author: List[str] = Field(min_items=1)
    price: float = Field(gt=0)
    release_year: int = Field(ge=1000, le=9999)
    
    @validator('release_year')
    def validate_year_format(cls, v):
        """Ensure year is exactly 4 digits"""
        if not (1000 <= v <= 9999):
            raise ValueError('Release year must be a 4-digit number')
        return v
    
    @validator('genre', 'author', pre=True)
    def validate_string_arrays(cls, v):
        """Convert comma-separated strings to arrays if needed"""
        if isinstance(v, str):
            return [item.strip() for item in v.split(',') if item.strip()]
        elif isinstance(v, list):
            return [item.strip() for item in v if isinstance(item, str) and item.strip()]
        return v
    
    # Generic helper methods for list operations
    def _add_to_list(self, target_list: List[str], item: str) -> bool:
        """Generic method to add item to a list if it doesn't exist"""
        item = item.strip()
        if item and item not in target_list:
            target_list.append(item)
            return True
        return False
    
    def _remove_from_list(self, target_list: List[str], item: str) -> bool:
        """Generic method to remove item from a list"""
        item = item.strip()
        if item in target_list:
            target_list.remove(item)
            return True
        return False
    
    def _has_in_list(self, target_list: List[str], item: str) -> bool:
        """Generic method to check if item exists in list"""
        return item.strip() in target_list
    
    def _list_to_string(self, target_list: List[str]) -> str:
        """Generic method to convert list to comma-separated string"""
        return ", ".join(target_list)
    
    # Genre management methods
    def add_genre(self, new_genre: str) -> bool:
        """Add a genre if it doesn't exist. Returns True if added, False if already exists"""
        return self._add_to_list(self.genre, new_genre)
    
    def remove_genre(self, genre_to_remove: str) -> bool:
        """Remove a genre. Returns True if removed, False if not found"""
        return self._remove_from_list(self.genre, genre_to_remove)
    
    def has_genre(self, genre: str) -> bool:
        """Check if book has a specific genre"""
        return self._has_in_list(self.genre, genre)
    
    def get_genre_string(self) -> str:
        """Get genres as comma-separated string"""
        return self._list_to_string(self.genre)
    
    # Author management methods
    def add_author(self, new_author: str) -> bool:
        """Add an author if it doesn't exist. Returns True if added, False if already exists"""
        return self._add_to_list(self.author, new_author)
    
    def remove_author(self, author_to_remove: str) -> bool:
        """Remove an author. Returns True if removed, False if not found"""
        return self._remove_from_list(self.author, author_to_remove)
    
    def has_author(self, author: str) -> bool:
        """Check if book has a specific author"""
        return self._has_in_list(self.author, author)
    
    def get_author_string(self) -> str:
        """Get authors as comma-separated string"""
        return self._list_to_string(self.author)


class Book(BaseBook):
    """Extended Book model with ID and additional functionality"""
    
    id: int = Field(ge=1)
    
    # Utility methods specific to the Book class
    def __str__(self) -> str:
        return f"{self.title} by {self.get_author_string()} ({self.release_year})"
    
    def __repr__(self) -> str:
        return f"Book(id={self.id}, title='{self.title}', isbn='{self.isbn}')"
    
    def summary(self) -> str:
        """Get a detailed summary of the book"""
        return (f"Book #{self.id}: {self.title}\n"
               f"Authors: {self.get_author_string()}\n"
                f"Genres: {self.get_genre_string()}\n"
                f"ISBN: {self.isbn}\n"
                f"Price: ${self.price}\n"
                f"Year: {self.release_year}")
