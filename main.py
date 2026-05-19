#!/usr/bin/env python3
"""
FPV UAV Route Planner - Main Pipeline
"""

import json

def main():
    print("=== FPV UAV Route Planner ===")
    
    with open('config.json') as f:
        config = json.load(f)
    
    print("Config loaded successfully.")
    print("\nPipeline ready. Next: implement modules one by one.")
    
if __name__ == "__main__":
    main()