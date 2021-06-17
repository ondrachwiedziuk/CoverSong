def read_data(adress):
    data = open(adress, encoding='utf8')
    songs = list()
    for line in data:
        song = line.split("\",\"")
        song = [row.replace('\"', '') for row in song]
        songs.append(Song(song))
    return songs

class Song:
    def __init__(self, info):
        self.cz_name = info[0]
        self.cz_singer = info[1]
        self.cz_translator = info[2]
        try:
            self.cz_year = int(info[3])
        except ValueError:
            self.cz_year = 0
        self.name = info[4]
        self.singer = info[5]
        try:
            self.year = int(info[6])
        except ValueError:
            self.year = 0
        self.lang = info[7]
        self.lang = 'en' if self.lang == '' else self.lang

    def search_by_name(self, text, where=None):
        if where is None:
            if text.lower() in self.cz_name.lower():
                return [self.name, self.singer, self.year, self.lang]
            elif text.lower() in self.name.lower():
                return [self.cz_name, self.cz_singer, self.cz_translator, self.cz_year]
        return None

    def song_by_year(self, year):
        if year == self.year:
            return [self.name, self.singer, self.year, self.lang]
        elif year == self.cz_year:
            return [self.cz_name, self.cz_singer, self.cz_translator, self.cz_year]
        else:
            return None
