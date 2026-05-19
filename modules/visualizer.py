"""
Module 4: Visualizer - Text report + simple plot
"""
import matplotlib.pyplot as plt

import folium

class Visualizer:
    def create_map(self, route, relays=None):
        """Create simple Folium map"""
        if not route:
            return None
        center = route[len(route)//2]
        m = folium.Map(location=[center[0], center[1]], zoom_start=11)
        
        # Add route
        folium.PolyLine(route, color='blue', weight=3, popup='Route').add_to(m)
        
        if relays:
            for r in relays:
                folium.Marker(
                    location=[r[0], r[1]], 
                    popup='Relay',
                    icon=folium.Icon(color='red', icon='broadcast-tower', prefix='fa')
                ).add_to(m)
        return m

    def plot_profile(self, distances, ground_elev, los, relays=None, save_path='profile.png'):
        """Plot elevation profile"""
        plt.figure(figsize=(12, 6))
        plt.plot(distances, ground_elev, label='Terrain', color='brown')
        
        # Drone height
        drone_h = ground_elev + 80
        plt.plot(distances, drone_h, '--', label='Drone path (80m AGL)', color='blue')
        
        plt.title('Terrain Profile & Line of Sight')
        plt.xlabel('Distance (km)')
        plt.ylabel('Elevation (m)')
        plt.legend()
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path)
            print(f"Profile saved to {save_path}")
        plt.close()