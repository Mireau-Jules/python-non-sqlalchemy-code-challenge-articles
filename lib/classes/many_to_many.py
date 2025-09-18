# lib/classes/many_to_many.py

class Article:
    all = []  

    def __init__(self, author, magazine, title):
        
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not (5 <= len(title.strip()) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")

        self._title = title
        self._author = author
        self._magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, _):
        return

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from classes.many_to_many import Author 
        if not isinstance(value, Author):
            raise TypeError("Author must be an Author instance.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from classes.many_to_many import Magazine
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be a Magazine instance.")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name.strip()) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        # only set once
        if not hasattr(self, "_name"):
            self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _):
        return

    def articles(self):
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        return list({a.magazine for a in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        return list({m.category for m in mags}) if mags else None


class Magazine:
    def __init__(self, name, category):

        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return
        if not (2 <= len(value) <= 16):
            return
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            return
        if len(value.strip()) == 0:
            return
        self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        titles = [a.title for a in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        counts = {}
        for a in self.articles():
            counts[a.author] = counts.get(a.author, 0) + 1
        result = [author for author, cnt in counts.items() if cnt > 2]
        return result if result else None
