from game_project.cyberpunk.engine.character.abc_player import IPlayer
from game_project.cyberpunk.engine.map.abc_map import IMap
from game_project.cyberpunk.engine.map.map_generator.generator import PlaceGenerator


class MapController:
    map: IMap

    def move(self, player, direction):
        pass
        # place_coord = self.map.locations[player.current_position[1]].places[player.current_position[2]]
        # place_cord = {x, y, z}
        # place_to_visit_cord = {x+1, y, z}
        # place_to_visit = self.map.locations[player.current_position[1]].places[place_to_visit_cord]

        # if place.render_path:
        #     pass # load place if has render path
        # else:
        #     PlaceGenerator.generate_place(location= "")
        # TODO: change coordinates, if place has no render path - generate place
