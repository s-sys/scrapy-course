from scrapy.item import Item, Field


class GameItem(Item):
    name = Field()
    developer = Field()
    publisher = Field()
    supported_systems = Field()
    in_game = Field()
    rating = Field()
    store_url = Field()
    source_url = Field()
    day_player_peak = Field()
    all_time_player_peak = Field()
