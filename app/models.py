class Sources:
    """
    sources clss to define sources objects
    """

    def __init__(self, id, name, description, url, category, country, language):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language


class Articles:
    """
    class articles that define articles classes
    """

    def __init__(self, id, author, title, description, url, image, date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date
