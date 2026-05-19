"""
Module 2: RouteAnalyzer - Simple Line-of-Sight check
"""
import numpy as np

class RouteAnalyzer:
    def __init__(self, radio_params):
        self.radio = radio_params
        self.drone_alt_agl = 80  # meters above ground

    def compute_los(self, distances, ground_elevations, start_height=2):
        """
        Simple LOS check.
        Returns list of booleans: True if visible from start.
        """
        los = []
        start_elev = ground_elevations[0] + start_height
        
        for i in range(len(distances)):
            drone_height = ground_elevations[i] + self.drone_alt_agl
            # Simple linear interpolation check
            expected_height = start_elev + (drone_height - start_elev) * (distances[i] / distances[-1] if distances[-1] > 0 else 0)
            
            # Check if terrain blocks
            terrain_at_point = ground_elevations[i]
            if expected_height > terrain_at_point + 5:  # 5m margin
                los.append(True)
            else:
                los.append(False)
        return los

    def find_shadow_zones(self, los):
        """Find segments where LOS is lost"""
        shadows = []
        in_shadow = False
        start_idx = 0
        for i, visible in enumerate(los):
            if not visible and not in_shadow:
                in_shadow = True
                start_idx = i
            elif visible and in_shadow:
                shadows.append((start_idx, i))
                in_shadow = False
        if in_shadow:
            shadows.append((start_idx, len(los)-1))
        return shadows