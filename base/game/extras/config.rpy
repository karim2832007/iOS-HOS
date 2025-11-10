init:
    $ config.font_replacement_map["DejaVuSans.ttf", False, True] = ("DejaVuSans-Oblique.ttf", False, False)
    
    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
            }
        
            def __init__(self, start, child, dist, peak_time=0.5, smoothness=2.0):
                if start is None:
                    start = child.get_placement()
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                self.peak_time = peak_time  # Time at which shake reaches peak intensity (0.0 to 1.0)
                self.smoothness = smoothness  # Higher values make the shake less violent
                
            def __call__(self, t, sizes):
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                # Modified intensity calculation
                if t < self.peak_time:
                    intensity = (t / self.peak_time) * self.dist
                else:
                    intensity = ((1 - t) / (1 - self.peak_time)) * self.dist
                
                angle = t * self.smoothness * math.pi * 2
                nx = xpos + intensity * math.sin(angle)
                ny = ypos + intensity * math.cos(angle)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, peak_time=0.5, smoothness=2.0, **properties):
            move = Shaker(start, child, dist=dist, peak_time=peak_time, smoothness=smoothness)
        
            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)