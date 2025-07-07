from enum import Enum
from typing import List, Union
from pydantic import BaseModel, Field, validator, root_validator

class StringListBase(BaseModel):
    """Generic base class for handling lists of strings with common functionality"""
    items: List[str] = Field(min_items=1)
    
    @classmethod
    def from_string(cls, string_value: str):
        """Create instance from comma-separated string"""
        items = [item.strip() for item in string_value.split(',') if item.strip()]
        return cls(items=items)
    
    @classmethod
    def from_list(cls, list_value: List[str]):
        """Create instance from list of strings"""
        items = [item.strip() for item in list_value if item.strip()]
        return cls(items=items)
    
    def to_string(self) -> str:
        """Convert to comma-separated string"""
        return ', '.join(self.items)
    
    def add(self, item: str) -> bool:
        """Add an item if it doesn't exist. Returns True if added, False if already exists"""
        item = item.strip()
        if item and item not in self.items:
            self.items.append(item)
            return True
        return False
    
    def remove(self, item: str) -> bool:
        """Remove an item. Returns True if removed, False if not found"""
        item = item.strip()
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def contains(self, item: str) -> bool:
        """Check if item exists"""
        return item.strip() in self.items
    
    def __str__(self) -> str:
        return self.to_string()
    
    def __iter__(self):
        return iter(self.items)
    
    def __len__(self):
        return len(self.items)

class GenreList(StringListBase):
    """Handle list of genres with additional functionality"""
    
    @property
    def genres(self) -> List[str]:
        """Alias for items to maintain backward compatibility"""
        return self.items
    
    @genres.setter
    def genres(self, value: List[str]):
        """Setter for genres property"""
        self.items = value

class AuthorList(StringListBase):
    """Handle list of authors with additional functionality"""
    
    @property
    def authors(self) -> List[str]:
        """Alias for items to maintain backward compatibility"""
        return self.items
    
    @authors.setter
    def authors(self, value: List[str]):
        """Setter for authors property"""
        self.items = value

class BaseBook(BaseModel):
    isbn: str = Field(max_length=30)
    title: str = Field(max_length=100)
    genre: List[str] = Field(min_items=1)  # Array of genres
    author: List[str] = Field(min_items=1)  # Array of authors
    price: float = Field(gt=0)  # Price must be positive
    release_year: int = Field(ge=1000, le=9999)  # 4-digit year constraint
    
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
            # If it's a string, split by comma and clean up
            return [item.strip() for item in v.split(',') if item.strip()]
        elif isinstance(v, list):
            # If it's already a list, clean up the items
            return [item.strip() for item in v if isinstance(item, str) and item.strip()]
        return v
    
    @property
    def genre_list(self) -> GenreList:
        """Get genres as a GenreList object"""
        return GenreList.from_list(self.genre)
    
    @property
    def author_list(self) -> AuthorList:
        """Get authors as an AuthorList object"""
        return AuthorList.from_list(self.author)

class Book(BaseBook):
    """Extended Book model with additional functionality"""
    id: int = Field(ge=1)
    
    def add_genre(self, new_genre: str) -> bool:
        """Add  new genre to the book. Returns True if added, False if already exists"""
        genre_list = self.genre_list
        if genre_list.add(new_genre):
            self.genre = genre_list.genres
            return True
        return False
    
    def add_author(self, new_author: str) -> bool:
        """Add a new author to the book. Returns True if added, False if already exists"""
        author_list = self.author_list
        if author_list.add(new_author):
            self.author = author_list.authors
            return True
        return False
    
    def remove_genre(self, genre_to_remove: str) -> bool:
        """Remove a genre from the book. Returns True if removed, False if not found"""
        genre_list = self.genre_list
        if genre_list.remove(genre_to_remove):
            self.genre = genre_list.genres
            return True
        return False
    
    def remove_author(self, author_to_remove: str) -> bool:
        """Remove an author from the book. Returns True if removed, False if not found"""
        author_list = self.author_list
        if author_list.remove(author_to_remove):
            self.author = author_list.authors
            return True
        return False
    
    def has_genre(self, genre: str) -> bool:
        """Check if book has a specific genre"""
        return self.genre_list.contains(genre)
    
    def has_author(self, author: str) -> bool:
        """Check if book has a specific author"""
        return self.author_list.contains(author)
    
    def get_genre_string(self) -> str:
        """Get genres as comma-separated string (for display purposes)"""
        return self.genre_list.to_string()
    
    def get_author_string(self) -> str:
        """Get authors as comma-separated string (for display purposes)"""
        return self.author_list.to_string()
