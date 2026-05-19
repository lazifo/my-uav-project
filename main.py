#!/usr/bin/env python3
"""
FPV UAV Route Planner - Minimal Working Demo
"""
import json
from modules.data_loader import DataLoader
from modules.route_analyzer import RouteAnalyzer
from modules.relay_optimizer import RelayOptimizer
from modules.visualizer import Visualizer


def main():
    print("=== FPV UAV Route Planner - Minimal Working Version ===\n")

    # Load config
    with open('config.json', encoding='utf-8') as f:
        config = json.load(f)

    # 1. Load / generate route and terrain
    loader = DataLoader()
    route, distances, ground_elev = loader.generate_synthetic_route(num_points=60, total_distance_km=35)
    print(f"Generated synthetic route: {len(route)} points, ~{distances[-1]:.1f} km")

    # 2. Analyze LOS
    analyzer = RouteAnalyzer(config.get('radio', {}))
    los = analyzer.compute_los(distances, ground_elev)
    shadows = analyzer.find_shadow_zones(los)
    print(f"LOS segments: {sum(los)} visible, {len(shadows)} shadow zones detected")

    # 3. Optimize relays
    optimizer = RelayOptimizer(config)
    relay_indices = optimizer.optimize_relays(distances, ground_elev, los)
    relay_positions = optimizer.get_relay_positions(route, relay_indices)
    print(f"Recommended relays: {len(relay_indices)} positions")

    # 4. Visualize
    viz = Visualizer()
    print("\nGenerating visualization...")
    viz.plot_profile(distances, ground_elev, los, relay_indices, save_path='elevation_profile.png')

    # Create map
    m = viz.create_map(route, relay_positions)
    if m:
        m.save('route_map.html')
        print("Interactive map saved to route_map.html")

    print("\n=== Demo completed successfully! ===")
    print("Open elevation_profile.png and route_map.html to see results.")


if __name__ == "__main__":
    main()