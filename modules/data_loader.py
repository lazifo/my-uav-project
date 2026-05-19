"""
Module 1: DataLoader - Synthetic terrain + sample route for demo
"""
import numpy as np

class DataLoader:
    def __init__(self):
        pass

    def generate_synthetic_route(self, num_points=50, total_distance_km=30):
        """Generate a simple route with hills for testing"""
        distances = np.linspace(0, total_distance_km, num_points)
        # Simple terrain with hills
        elevations = 200 + 150 * np.sin(distances / 8) + 80 * np.sin(distances / 3)
        elevations = np.clip(elevations, 50, 500)
        
        # Fake coordinates (around Donbas area)
        lats = np.linspace(48.9, 48.3, num_points)
        lons = np.linspace(38.0, 37.5, num_points)
        
        route = list(zip(lats, lons))
        return route, distances, elevations

    def get_elevation_profile(self, route):
        """For real use: would load from DEM. Here returns synthetic."""
        _, distances, elevations = self.generate_synthetic_route(len(route))
        return distances, elevations