
---

## 4️⃣ FILE: `delete.md`

📍 **Path**:  
`LibraryProject/bookshelf/delete.md`

📄 **Content (COPY EVERYTHING BELOW):**

```md
## Delete Book

```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()
