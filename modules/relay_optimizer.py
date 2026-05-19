"""
Module 3: RelayOptimizer - Greedy relay placement
"""

class RelayOptimizer:
    def __init__(self, config):
        self.config = config
        self.relay_height = config.get('relay', {}).get('mast_height_m', 5)

    def optimize_relays(self, distances, ground_elevations, los):
        """
        Greedy algorithm: place relay when LOS is lost.
        Returns list of relay indices.
        """
        relays = []
        current_base = 0  # index of current transmitter
        
        for i in range(1, len(los)):
            if not los[i]:
                # Place relay at last good point
                relay_idx = i - 1
                if relay_idx > current_base:
                    relays.append(relay_idx)
                    current_base = relay_idx
        return relays

    def get_relay_positions(self, route, relays):
        """Return coordinates of relays"""
        return [route[idx] for idx in relays]