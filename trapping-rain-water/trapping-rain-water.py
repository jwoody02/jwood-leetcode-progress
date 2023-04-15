class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        _current_water_height = 0 # keeps track of how tall the water is
        _current_puddle = 0 # for nullifying last puddle if applicable
        for i, column in enumerate(height):
            if i == len(height) - 1 and _current_water_height != 0 and column < _current_water_height:
                # we need to nullify this last puddle
                # total_water -= _current_puddle
                continue
            if _current_water_height == 0:
                if i < len(height) - 1:
                    # new puddle
                    if height[i+1] < column:
                        _current_water_height = column
                        if max(height[i + 1:]) < column:
                            _current_water_height = max(height[i + 1:])
                        _current_puddle = 0
            else:
                if column >= _current_water_height:
                    # done with this puddle
                    _current_water_height = 0
                    _current_puddle = 0
                    if i < len(height) - 1 and height[i+1] < column:
                        _current_water_height = column
                        if max(height[i + 1:]) < column:
                            _current_water_height = max(height[i + 1:])
                        _current_puddle = 0
                else:
                    # add to water
                    total_water += (_current_water_height - column)
                    _current_puddle += _current_water_height - column

        return total_water
