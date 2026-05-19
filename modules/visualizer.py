"""
Module 4: Visualizer - Maps and plots
"""

import folium

class Visualizer:
    def create_map(self, route, relays=None):
        """Create interactive Folium map"""
        print("[Visualizer] Creating map...")
        m = folium.Map(location=[48.5, 38.0], zoom_start=10)
        return m
    
    def plot_elevation_profile(self, distances, elevations):
        """Plot terrain profile with matplotlib"""
        print("[Visualizer] Plotting elevation profile...")