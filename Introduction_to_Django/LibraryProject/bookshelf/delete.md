
📄 **DELETE EVERYTHING inside this file**  
Then **PASTE THIS EXACTLY** 👇

```md
## Delete Book

```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
