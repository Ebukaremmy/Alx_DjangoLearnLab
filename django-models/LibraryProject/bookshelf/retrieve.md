
---

## 2️⃣ FILE: `retrieve.md`

📍 **Path**:  
`LibraryProject/bookshelf/retrieve.md`

📄 **Content (COPY EVERYTHING BELOW):**

```md
## Retrieve Book

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book
